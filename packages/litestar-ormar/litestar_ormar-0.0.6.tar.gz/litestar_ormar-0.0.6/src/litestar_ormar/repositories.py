from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

import ormar
from litestar.repository import AbstractAsyncRepository, NotFoundError, RepositoryError
from litestar.repository.filters import (
    BeforeAfter,
    CollectionFilter,
    LimitOffset,
    NotInCollectionFilter,
    NotInSearchFilter,
    OnBeforeAfter,
    OrderBy,
    SearchFilter,
)
from ormar.queryset.clause import FilterGroup


if TYPE_CHECKING:
    from litestar.repository.filters import FilterTypes
    from typing import TypeVar

    T = TypeVar("T", bound=ormar.Model)
    CollectionT = ormar.QuerySet


def ensure_type(f):
    def checker(self, *args, **kwargs):
        data = args[0]
        if not isinstance(data, list):
            data = [data]
        if not all(isinstance(obj, self.model_type) for obj in data):
            raise TypeError("Mismatched data type!")
        return f(self, *args, **kwargs)

    return checker


class OrmarRepository(AbstractAsyncRepository):
    def _get_queryset(self, kwargs):
        select_related: None | str | list[str] = kwargs.pop("select_related", None)
        prefetch_related: None | str | list[str] = kwargs.pop("prefetch_related", None)
        qs = self.model_type.objects
        if select_related:
            qs = qs.select_related(select_related)
        if prefetch_related:
            qs = qs.prefetch_related(prefetch_related)
        return qs

    def model_from_dict(self, **kwargs):
        data = {
            field_name: kwargs[field_name]
            for field_name in self.model_type.extract_db_own_fields()
        }
        return self.model_type(**data)

    def _apply_filters(self, qs, *filters: FilterTypes) -> CollectionT:
        real_filters = []
        for f in filters:
            if isinstance(f, LimitOffset):
                qs = qs.limit(f.limit).offset(f.offset)
            elif isinstance(f, OrderBy):
                prefix = "-" if f.sort_order == "desc" else ""
                qs = qs.order_by(f"{prefix}{f.field_name}")
            else:
                real_filters.append(self._translate_filter(f))
        if real_filters:
            qs = qs.filter(*real_filters)
        return qs

    def _translate_filter(self, litestar_filter: FilterTypes) -> FilterGroup:
        field_name = litestar_filter.field_name
        params = {}
        if isinstance(litestar_filter, BeforeAfter):
            if litestar_filter.before:
                params[f"{field_name}__lt"] = litestar_filter.before
            if litestar_filter.after:
                params[f"{field_name}__gt"] = litestar_filter.after
        elif isinstance(litestar_filter, OnBeforeAfter):
            if litestar_filter.before:
                params[f"{field_name}__lte"] = litestar_filter.on_or_before
            if litestar_filter.after:
                params[f"{field_name}__gte"] = litestar_filter.on_or_after
        elif isinstance(litestar_filter, CollectionFilter | NotInCollectionFilter):
            params[f"{field_name}__in"] = litestar_filter.values
            if isinstance(litestar_filter, NotInCollectionFilter):
                params["_exclude"] = True
        elif isinstance(litestar_filter, SearchFilter | NotInSearchFilter):
            suffix = "__icontains" if litestar_filter.ignore_case else "__contains"
            params[f"{field_name}__{suffix}"] = litestar_filter.value
            if isinstance(litestar_filter, NotInSearchFilter):
                params["_exclude"] = True

        return FilterGroup(**params)

    @ensure_type
    async def add(self, data: T) -> T:
        return await data.save()

    @ensure_type
    async def add_many(self, data: list[T]) -> list[T]:
        await self.model_type.objects.bulk_create(data)
        return data

    async def count(self, *filters: FilterTypes, **kwargs: Any) -> int:
        qs = self._apply_filters(self.model_type.objects, *filters)
        return await qs.filter(**kwargs).count()

    async def delete(self, item_id: Any) -> T:
        try:
            obj = await self.model_type.objects.get(id=item_id)
        except ormar.NoMatch as e:
            raise NotFoundError("No item found when one was expected") from e
        await obj.delete()
        return obj

    async def delete_many(self, item_ids: list[Any]) -> list[T]:
        params = {f"{self.id_attribute}__in": item_ids}
        qs = self.model_type.objects.filter(**params)
        result = await qs.all()
        await qs.delete()
        return result

    async def exists(self, *filters: FilterTypes, **kwargs: Any) -> bool:
        qs = self._apply_filters(self.model_type.objects, *filters)
        return await qs.filter(**kwargs).exists()

    async def get(self, item_id: Any, **kwargs: Any) -> T:
        params = {f"{self.id_attribute}": item_id}
        queryset = self._get_queryset(kwargs)
        try:
            return await queryset.get(**params, **kwargs)
        except ormar.NoMatch as e:
            raise NotFoundError("No item found when one was expected") from e

    async def get_one(self, **kwargs: Any) -> T:
        queryset = self._get_queryset(kwargs)
        try:
            return await queryset.first(**kwargs)
        except ormar.NoMatch as e:
            raise NotFoundError("No item found when one was expected") from e

    async def get_or_create(self, **kwargs: Any) -> tuple[T, bool]:
        queryset = self._get_queryset(kwargs)
        return await queryset.get_or_create(**kwargs)

    async def get_one_or_none(self, **kwargs: Any) -> T | None:
        queryset = self._get_queryset(kwargs)
        return await queryset.get_or_none(**kwargs)

    @ensure_type
    async def update(self, data: T) -> T:
        data_id = getattr(data, f"{self.id_attribute}")
        params = {f"{self.id_attribute}": data_id}
        if data_id is None or (
            isinstance(data_id, UUID)
            and not await self.model_type.objects.filter(**params).exists()
        ):
            raise NotFoundError("No item found when one was expected")
        return await data.update()

    @ensure_type
    async def update_many(self, data: list[T]) -> list[T]:
        result = []
        async with self.model_type.ormar_config.database.transaction():
            for obj in data:
                await obj.save_related(follow=True)
                result.append(await self.update(obj))
        # TODO: find way to use: await self.model_type.objects.bulk_update(data)
        return result

    @ensure_type
    async def upsert(self, data: T) -> T:
        data_id = getattr(data, f"{self.id_attribute}")

        if data_id is None or isinstance(data_id, UUID):
            return await data.upsert()
        else:
            return await self.update(data)

    @ensure_type
    async def upsert_many(self, data: list[T]) -> list[T]:
        result = []
        async with self.model_type.ormar_config.database.transaction():
            for obj in data:
                result.append(await self.upsert(obj))
        return result

    async def list_and_count(
        self, *filters: FilterTypes, **kwargs: Any
    ) -> tuple[list[T], int]:
        result = await self.list(*filters, **kwargs)
        return result, len(result)

    async def list(self, *filters: FilterTypes, **kwargs: Any) -> list[T]:
        queryset = self._get_queryset(kwargs)
        queryset = self._apply_filters(queryset, *filters)
        return await queryset.all(**kwargs)

    def filter_collection_by_kwargs(
        self, collection: CollectionT, /, **kwargs: Any
    ) -> CollectionT:
        if unknown_fields := set(self.model_type.model_fields) - set(kwargs):
            raise RepositoryError(f"Unknown field(s): {', '.join(unknown_fields)}")
        return collection.filter(**kwargs)
