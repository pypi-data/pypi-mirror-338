import functools
import operator
import re
from dataclasses import dataclass
from datetime import datetime, date
from functools import reduce
from typing import Literal, get_args, Union, Type, TypeVar, overload, Iterable, Callable

from django.db import models
from django.db.models.query import QuerySet

Value = str | int | float | datetime | date | None
T = TypeVar("T", bound=models.Model)

# TODO: implement Q based querying for inverse lookups
Lookup = Literal[
    "exact",
    "iexact",
    "contains",
    "icontains",
    "in",
    "gt",
    "gte",
    "lt",
    "lte",
    "startswith",
    "istartswith",
    "endswith",
    "iendswith",
    "range",
    "date",
    "year",
    "iso_year",
    "month",
    "day",
    "week",
    "week_day",
    "iso_week_day",
    "quarter",
    "time",
    "hour",
    "minute",
    "second",
    "isnull",
    "isnotnull",  # not a Django filter fyi
    "regex",
    "iregex",
]

class CustomOperators:
    @staticmethod
    def startswith(value, _str):
        return value.startswith(_str)

    @staticmethod
    def istartswith(value, _str):
        return CustomOperators.startswith(value.lower(), _str.lower())

    @staticmethod
    def endswith(value, _str):
        return value.endswith(_str)

    @staticmethod
    def iendswith(value, _str):
        return CustomOperators.endswith(value.lower(), _str.lower())

    @staticmethod
    def range(value, a, b):
        return a < value < b

    @staticmethod
    def isnull(value, *_):
        return value is None

    @staticmethod
    def isnotnull(value, *_):
        return value is not None

    @staticmethod
    def regex(value, regex):
        return bool(re.search(regex, value))

    @staticmethod
    def iregex(value, regex):
        return bool(re.search(regex, value, flags=re.IGNORECASE))

    @staticmethod
    def contains(value, comparator):
        # Custom operator because strings need to be on the left operand
        # and operator.contains is reversed.
        if isinstance(value, str):
            return value in comparator
        return operator.contains(value, comparator)

class OperatorMap:
    _operator_mapping = {
        "exact": operator.eq,
        "iexact": operator.eq,
        "contains": CustomOperators.contains,
        "in": CustomOperators.contains,
        "gt": operator.gt,
        "gte": operator.ge,
        "lt": operator.lt,
        "lte": operator.le,
        "startswith": CustomOperators.startswith,
        "istartswith": CustomOperators.istartswith,
        "endswith": CustomOperators.endswith,
        "iendswith": CustomOperators.iendswith,
        "range": CustomOperators.range,
        "isnull": CustomOperators.isnull,
        "isnotnull": CustomOperators.isnotnull,
        "regex": CustomOperators.regex,
        "iregex": CustomOperators.iregex,
    }

    def __getitem__(self, item):
        if item in self._operator_mapping:
            return self._operator_mapping[item]
        else:
            raise NotImplementedError(item)


@dataclass
class Filter:
    path: str
    operator: Lookup
    value: Value | list[Value]

    def __post_init__(self):
        if self.operator not in get_args(Lookup):
            raise ValueError(f"Invalid Django lookup: {self.operator}")

    @property
    def json(self) -> dict:
        return {f"{self.path.replace('.', '__')}__{self.operator}": self.value}

    @staticmethod
    def merge_to_dict(*filters: Union["Filter", list["Filter"]]) -> dict:
        return reduce(operator.ior, [i.json for sub in filters for i in (sub if isinstance(sub, list) else [sub])], {})

    @staticmethod
    def from_list(*filter_dicts: dict | list[dict]) -> list["Filter"]:
        return [Filter(**_filter) for sub in filter_dicts for _filter in (sub if isinstance(sub, list) else [sub])]

    @property
    def mapped_operator(self) -> Callable:
        return OperatorMap()[self.operator]

    def resolve_attr(self, obj: T):
        return functools.reduce(lambda d, key: getattr(d, key), self.path.split("."), obj)


@dataclass
class FilterSet:
    filters: list[Filter]

    @overload
    def filter(self, model: Type[T]) -> QuerySet[T]:
        """
        Execute a Django queryset against supplied model type.

        :param model: The Django model to query against.
        :type model: Type[models.Model]
        :return: The queryset result.
        """
        ...

    @overload
    def filter(self, model: Iterable[T]) -> list[T]:
        """
        Filter a list of instance objects.

        :param model: The list of objects to filter against.
        :type model: Iterable[models.Model]
        :return: A filtered list of the supplied instance objects.
        """
        ...

    def filter(self, model: Type[T] | Iterable[T]) -> QuerySet[T] | list[T]:
        results = []
        if isinstance(model, list | Iterable):
            for instance in model:
                for _filter in self.filters:
                    value = []
                    if not isinstance(_filter.value, list):
                        value = [_filter.value]
                    else:
                        value.append(_filter.value)

                    if _filter.mapped_operator(*[_filter.resolve_attr(instance), *value]):
                        results.append(instance)
                        continue
            return results
        else:
            if issubclass(model, models.Model):
                return model.objects.filter(**Filter.merge_to_dict(self.filters))
            raise ValueError(f"Invalid Django model type: {model}")

