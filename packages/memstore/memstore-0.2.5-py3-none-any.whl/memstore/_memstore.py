from __future__ import annotations

import collections
import functools
import itertools
import operator
import typing


class MemStore:
    def __init__(
            self,
            indexes: list[typing.Any] | None = None,
    ) -> None:
        self._data: dict[int, dict[typing.Any, typing.Any]] = {}
        self._indexes: dict[
            typing.Any,
            dict[typing.Any, set[int]],
        ] = collections.defaultdict(lambda: collections.defaultdict(set))
        self._ident_counter: itertools.count = itertools.count()
        if indexes is not None:
            [self.add_index(index) for index in indexes]

    def add(
            self,
            values: dict,
    ) -> int:
        ident = next(self._ident_counter)
        self._data[ident] = values
        [index[values[field]].add(ident) for field, index in self._indexes.items() if field in values]
        return ident

    def get(self, ident: int) -> dict[typing.Any, typing.Any] | None:
        return self._data.get(ident)

    def filter(
            self,
            values: dict[typing.Any, typing.Any],
    ) -> list[tuple[int, dict[typing.Any, typing.Any]]]:
        indexes = self._indexes
        result = [(ident, self.get(ident)) for ident in sorted(functools.reduce(operator.and_, (
            indexes[field].get(value, set()) if field in indexes
            else {ident for ident, values in self._data.items() if field in values and values[field] == value}
            for field, value in values.items()
        )))]
        return result

    def islice(self, start=None, stop=None, step=None) -> list[tuple[int, dict[typing.Any, typing.Any]]]:
        data = self._data
        result = list(itertools.islice(data.items(), *slice(start, stop, step).indices(len(data))))
        return result

    def all(self) -> list[tuple[int, dict[typing.Any, typing.Any]]]:
        return list(self._data.items())

    def delete(
            self,
            ident: int,
    ) -> bool:
        data = self._data
        if ident in data:
            values = data[ident]
            for field, index in self._indexes.items():
                if field in values:
                    value = values[field]
                    idents = index[value]
                    if ident in idents:
                        idents.remove(ident)
                        if not idents:
                            del index[value]
            del data[ident]
            result = True
        else:
            result = False
        return result

    def add_index(
            self,
            field: typing.Any,
    ) -> None:
        indexes = self._indexes
        if field not in indexes:
            index = indexes[field]
            [index[values[field]].add(ident) for ident, values in self._data.items() if field in values]

    def drop_index(
            self,
            field: typing.Any,
    ) -> None:
        indexes = self._indexes
        if field in indexes:
            del indexes[field]
