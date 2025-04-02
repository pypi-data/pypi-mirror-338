# coding=utf-8

from typing import Any, Dict, List

T_Arr = List[Any]
T_Dic = Dict[Any, Any]
T_DoD = Dict[Any, T_Dic]

TN_Any = None | Any
TN_Dic = None | T_Dic
TN_ArrStr = None | T_Arr | str
TN_DoD = None | T_DoD


class DoD:
    """ Manage Dictionary of Dictionaries
    """
    @staticmethod
    def sh_value(
            dod: TN_Dic, keys: TN_ArrStr) -> TN_Any:
        if dod is None or not keys:
            return None
        if not isinstance(dod, dict):
            return None
        if isinstance(keys, str):
            keys = [keys]

        _dic = dod
        for key in keys:
            value = _dic.get(key)
            if value is None:
                return value
            if not isinstance(value, dict):
                return value
            _dic = value
        return value

    @staticmethod
    def nvl(dod: TN_DoD) -> TN_DoD:
        """ nvl function similar to SQL NVL function
        """
        if dod is None:
            dod = {}
        return dod

    @classmethod
    def replace_keys(cls, dod: T_DoD, keys: T_Dic) -> T_Dic:
        """ recurse through the dictionary while building a new one
            with new keys from a keys dictionary
        """
        dic_new = {}
        for key in dod.keys():
            key_new = keys.get(key, key)
            if isinstance(dod[key], dict):
                dic_new[key_new] = cls.replace_keys(dod[key], keys)
            else:
                dic_new[key_new] = dod[key]
        return dic_new
