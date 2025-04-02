# coding=utf-8

from typing import Any, Dict, Iterator, List, Tuple

T_Arr = List[Any]
T_Tup = Tuple[Any, ...]
T_Dic = Dict[Any, Any]
T_D3V = Dict[Any, Dict[Any, T_Dic]]

T_IterTup = Iterator[T_Tup]


class D3V:

    @staticmethod
    def set(d3v: T_D3V, keys: T_Arr, value: Any) -> T_D3V:
        if keys is None or len(keys) != 3:
            return d3v
        key0 = keys[0]
        key1 = keys[1]
        key2 = keys[2]
        if key0 not in d3v:
            d3v[key0] = {}
        if key1 not in d3v[key0]:
            d3v[key0][key1] = {}
        d3v[key0][key1][key2] = value
        return d3v

    @staticmethod
    def yield_values(d3v: T_D3V) -> T_IterTup:
        if d3v is None:
            return
        for key0, d2v in d3v.items():
            for key1, d1v in d2v.items():
                for key2, value in d1v.items():
                    if isinstance(value, (list, tuple)):
                        yield (key0, key1, key2, *value)
                    else:
                        yield (key0, key1, key2, value)
