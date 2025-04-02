# coding=utf-8

from typing import Any, Dict, Iterator, List, Tuple

T_Arr = List[Any]
T_Tup3 = Tuple[Any, Any, Any]
T_Dic = Dict[Any, Any]

T_DoA = Dict[Any, T_Arr]
T_D2A = Dict[Any, T_DoA]
T_D2V = Dict[Any, T_Dic]

T_IterTup3 = Iterator[T_Tup3]


class D2V:
    @classmethod
    def sh_union(cls, d2a: T_D2A) -> T_Arr:
        arr_new = []
        for _key1, _key2, arr in cls.yield_values(d2a):
            arr_new.extend(arr)
        return arr_new

    @staticmethod
    def append(d2v: T_D2V, keys: T_Arr, value: Any) -> T_D2V:
        key0 = keys[0]
        key1 = keys[1]
        if key0 not in d2v:
            d2v[key0] = {}
        if key1 not in d2v[key0]:
            d2v[key0][key1] = []
        d2v[key0][key1].append(value)
        return d2v

    @staticmethod
    def set(d2v: T_D2V, keys: T_Arr, value: Any) -> T_D2V:
        key0 = keys[0]
        key1 = keys[1]
        if key0 not in d2v:
            d2v[key0] = {}
        d2v[key0][key1] = value
        return d2v

    @staticmethod
    def sh_key2values(d2v: T_D2V) -> T_D2V:
        dic: T_Dic = {}
        for key0, dov in d2v.items():
            if key0 not in dic:
                dic[key0] = {}
            for key1, _dummy in dov.items():
                dic[key0].append(key1)
        return dic

    @staticmethod
    def yield_values(d2v: T_D2V) -> T_IterTup3:
        for key0, dov in d2v.items():
            for key1, value in dov.items():
                yield (key0, key1, value)
