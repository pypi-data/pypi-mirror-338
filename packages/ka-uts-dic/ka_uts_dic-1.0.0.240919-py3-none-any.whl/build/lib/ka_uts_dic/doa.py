# coding=utf-8
import pandas as pd

from ka_uts_arr.arr import Arr
from ka_uts_dic.dic import Dic

from typing import Callable, Dict, List, Tuple, Any
T_Arr = List[Any]
T_Dic = Dict[Any, Any]
T_Tup = Tuple[Any, ...]
T_ArrTup = T_Arr | T_Tup
T_DoA = Dict[Any, T_Arr]
TN_Any = None | Any
T_AoD = List[T_Dic]
T_DoAoD = Dict[Any, T_AoD]
T_DoPdDf = Dict[Any, pd.DataFrame]


class DoA:
    """
    Manage Dictionary of Array
    """
    @staticmethod
    def sh_d_pddf(d_aod: T_DoAoD) -> T_DoPdDf:
        d_df = {}
        for key, aod in d_aod.items():
            df = pd.DataFrame(aod)
            d_df[key] = df
        return d_df

    @staticmethod
    def apply(
            fnc: Callable, doa: T_Dic, keys: T_Arr,
            item: Any, item0: TN_Any) -> None:
        """
        assign item to dictionary defined as value
        for the given keys.
        """
        if item0 is None:
            item0 = []
        if isinstance(keys, str):
            keys = [keys]
        elif not isinstance(keys, (list, tuple)):
            return

        _doa = doa
        # all elements of keys except the last
        for key in keys[:-1]:
            if key not in _doa:
                _doa[key] = []
            _doa = _doa[key]

        # last element of keys
        key = keys[-1]
        Dic.set(_doa, key, item0)
        _doa[key].append(item)
        fnc(_doa[key], item)

    @staticmethod
    def append(
            doa: T_Dic, keys: T_ArrTup, item: TN_Any,
            item0: TN_Any = None) -> None:
        """
        assign item to dictionary defined as value
        for the given keys.
        """
        if item0 is None:
            item0 = []
        if isinstance(keys, str):
            keys = [keys]
        elif not isinstance(keys, (list, tuple)):
            return

        _doa = doa
        # all keys elements except the last
        for key in keys[:-1]:
            if key not in _doa:
                _doa[key] = {}
            _doa = _doa[key]

        # last keys element
        key = keys[-1]
        if key not in _doa:
            _doa[key] = item0

        _doa[key].append(item)

    @staticmethod
    def append_unique(
            doa: T_Dic, keys: T_ArrTup,
            item: Any, item0: TN_Any = None) -> None:
        """
        assign item to dictionary defined as value
        for the given keys.
        """
        if item0 is None:
            item0 = []
        if isinstance(keys, str):
            keys = [keys]
        elif not isinstance(keys, (list, tuple)):
            return

        _doa = doa
        # all keys elements except the last
        for key in keys[:-1]:
            if key not in _doa:
                _doa[key] = {}
            _doa = _doa[key]

        # last keys element
        key = keys[-1]
        if key not in _doa:
            _doa[key] = item0

        Arr.append_unique(_doa[key], item)

    @staticmethod
    def extend(
            doa: T_Dic, keys: T_ArrTup, item: Any) -> None:
        """
        assign item to dictionary defined as value
        for the given keys.
        """
        if isinstance(keys, str):
            keys = [keys]
        if not isinstance(keys, (list, tuple)):
            return
        _doa = doa

        # all keys elements except the last
        for key in keys[:-1]:
            if key not in _doa:
                _doa[key] = {}
            _doa = _doa[key]

        # last keys element
        key = keys[-1]
        if isinstance(item, str):
            item = [item]
        if key not in _doa:
            _doa[key] = item
        else:
            _doa[key].extend(item)

    @staticmethod
    def set(
            doa: T_Dic, keys: T_ArrTup, item0: TN_Any = None) -> None:
        """
        assign item to dictionary defined as value
        for the given keys.
        """
        if item0 is None:
            item0 = []
        if isinstance(keys, str):
            keys = [keys]
        elif not isinstance(keys, (list, tuple)):
            return
        _doa = doa

        # all keys elements except the last
        for key in keys[:-1]:
            if key not in _doa:
                _doa[key] = {}
            _doa = _doa[key]

        # last keys element
        key = keys[-1]
        if key not in _doa:
            _doa[key] = item0

    @staticmethod
    def sh_union(
            doa: T_DoA) -> T_Arr:
        arr_new = []
        for _key, _arr in doa.items():
            arr_new.extend(_arr)
        return arr_new
