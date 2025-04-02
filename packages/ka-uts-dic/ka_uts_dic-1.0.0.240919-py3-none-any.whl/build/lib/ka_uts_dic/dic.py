# import builtins
# from json_normalize import json_normalize

from ka_uts_arr.aod import AoD
from ka_uts_arr.aod2p import AoD2P
from ka_uts_obj.num import Num
from ka_uts_obj.obj import Obj

from typing import Any, Callable, Dict, Iterator, List, Tuple

T_Arr = List[Any]
T_Callable = Callable
T_Dic = Dict[Any, Any]
T_AoD = List[T_Dic]
T_IterAny = Iterator[Any]
T_Tup = Tuple[Any, ...]
T_ArrTup = T_Arr | T_Tup
T_ToD = Tuple[T_Dic, ...]

TN_Any = None | Any
TN_AoD = None | T_AoD
TN_Arr = None | T_Arr
TN_ArrTup = None | T_Arr | T_Tup
TN_Bool = None | bool
TN_Callable = None | T_Callable
TN_Dic = None | T_Dic


class Dic:
    """ Manage Dictionary
    """
    @staticmethod
    def sh_d_filter(key: str, value: Any, method: str = 'df') -> T_Dic:
        d_filter = {}
        d_filter['key'] = key
        d_filter['value'] = value
        d_filter['method'] = method
        return d_filter

    @staticmethod
    def sh_d_index_d_values(dic: T_Dic, d_pivot: T_Dic) -> T_ToD:
        a_index: T_Arr = d_pivot.get('index', [])
        a_values: T_Arr = d_pivot.get('values', [])
        d_index: T_Dic = {}
        d_values: T_Dic = {}
        if len(a_values) == 1:
            for key, value in dic.items():
                print(f"len(a_values) == 1 key = {key}")
                print(f"len(a_values) == 1 value = {value}")
                if key in a_index:
                    d_index[key] = value
                else:
                    key0 = key
                    key1 = a_values[0]
                    print(f"len(a_values) == 1 key not in a_index key0 = {key0}")
                    print(f"len(a_values) == 1 key not in a_index key1 = {key1}")
                    if key0 not in d_values:
                        d_values[key0] = {}
                    d_values[key0][key1] = value
            print("*************************************************")
            print(f"len(a_values) == 1 dic = {dic}")
            print(f"len(a_values) == 1 d_values = {d_values}")
            print(f"len(a_values) == 1 a_index = {a_index}")
            print(f"len(a_values) == 1 a_values = {a_values}")
            print("*************************************************")
        else:
            for key, value in dic.items():
                if key in a_index:
                    d_index[key] = value
                else:
                    a_key = key.split("_")
                    key1 = a_key[0]
                    key0 = a_key[1]
                    if key0 in a_values:
                        if key0 not in d_values:
                            d_values[key0] = {}
                        d_values[key0][key1] = value
                    else:
                        print(f"ERROR key0 = {key0} no in a_values = {a_values}")
            print(f"len(a_values) != 1 d_values = {d_values}")
        return d_index, d_values

    @staticmethod
    def merge(dic0: TN_Dic, dic1: TN_Dic) -> TN_Dic:
        if dic0 is None:
            if dic1 is None:
                return None
            else:
                return {**dic1}
        else:
            if dic1 is None:
                return {**dic0}
            else:
                return {**dic0, **dic1}

    @staticmethod
    def sh_d_vals_d_cols(dic):
        d_cols = {}
        d_vals = {}
        for key, value in dic.items():
            a_key = key.split("_")
            if len(a_key) == 1:
                key0 = a_key[0]
                d_vals[key0] = value
            else:
                key0 = a_key[0]
                key1 = a_key[1]
                if key1 not in d_cols:
                    d_cols[key1] = {}
                d_cols[key1][key0] = value
        return d_vals, d_cols

    @staticmethod
    def round_value(dic: T_Dic, keys: TN_Arr, kwargs: T_Dic) -> T_Dic:
        round_digits: int = kwargs.get('round_digits', 2)
        if not dic:
            msg = f"Parameter dic = {dic} is undefined"
            raise Exception(msg)
        if not keys:
            return dic
        dic_new: T_Dic = {}
        for key, value in dic.items():
            if value is None:
                dic_new[key] = value
            else:
                if key in keys:
                    dic_new[key] = round(value, round_digits)
                else:
                    dic_new[key] = value
        return dic_new

    @staticmethod
    def show_sorted_keys(dic: TN_Dic) -> T_Arr:
        if not dic:
            return []
        a_key = list(dic.keys())
        # print(f"a_key = {a_key}")
        a_key.sort()
        return a_key

    @staticmethod
    def set_format_value(
            dic: TN_Dic, key: Any, fmt: Any) -> None:
        """ format value of dictionary key using the format string
            and replace the value by the formatted value
        """
        if not dic:
            return
        if key in dic:
            dic[key] = fmt.format(dic[key])

    @staticmethod
    def set_divide(
            dic: TN_Dic, key: Any, key1: Any, key2: Any) -> None:
        """ divide value of key1 by value of key2 and
            assign this value to the key
        """
        # Dictionary is None or empty
        if not dic:
            return
        if key1 in dic and key2 in dic:
            _val1 = dic[key1]
            _val2 = dic[key2]
            dic[key] = Num.divide(_val1, _val2)
        else:
            dic[key] = None

    @staticmethod
    def set_multiply_with_factor(
            dic: TN_Dic, key_new: Any, key: Any, factor: Any) -> None:
        """ multipy dictionary value with factor
        """
        # Dictionary is None or empty
        if not dic:
            return
        if key not in dic:
            return
        if dic[key] is None:
            dic[key_new] = None
        else:
            dic[key_new] = dic[key] * factor

    @staticmethod
    def rename_key(
            dic: TN_Dic, kwargs: T_Dic) -> TN_Dic:
        """ rename old dictionary key with new dictionary key
        """
        # Dictionary is None or empty
        if not dic:
            return dic
        _key_old = kwargs.get("key_old")
        _key_new = kwargs.get("key_new")
        _dic_new = {}
        for _k, _v in dic.items():
            if _k == _key_old:
                _dic_new[_key_new] = _v
            else:
                _dic_new[_k] = _v
        return _dic_new

    @staticmethod
    def set_by_div(
            dic: TN_Dic, key: str, key1: str, key2: str) -> None:
        """ assign division of key1-value by key2-value to key-value
        """
        # Dictionary is None or empty
        if not dic:
            return
        if key1 in dic and key2 in dic:
            _val1 = dic[key1]
            _val2 = dic[key2]
            if (isinstance(_val1, (int, float)) and
               isinstance(_val2, (int, float)) and
               _val2 != 0):
                dic[key] = _val1/_val2
            else:
                dic[key] = None
        else:
            dic[key] = None

    @staticmethod
    def copy(
            dic_target: TN_Dic, dic_source: None | T_Dic,
            keys: TN_Arr = None) -> None:
        """ copy values for keys from source to target dictionary
        """
        # Dictionary is None or empty
        if not dic_target:
            return
        if not dic_source:
            return
        if keys is None:
            keys = list(dic_source.keys())
        for key in keys:
            dic_target[key] = dic_source[key]

    @classmethod
    def append(
            cls, dic: TN_Dic, keys: TN_Any, value: Any, item0: TN_Any = None) -> None:
        """ append item to dictionary value for last key of key list
            the value must be an appendable value
        """
        # Dictionary is None or empty
        if not dic or not keys:
            return
        if item0 is None:
            item0 = []
        if not isinstance(keys, (list, tuple)):
            keys = [keys]

        _dic = cls.locate(dic, keys[:-1])
        if not _dic:
            return
        # last element
        key_last = keys[-1]
        if key_last not in _dic:
            _dic[key_last] = item0

        if isinstance(_dic[key_last], (list, tuple)):
            _dic[key_last].append(value)

    @classmethod
    def extend(
            cls, dic: TN_Dic, keys: TN_Any, value: Any, item0: TN_Any = None) -> None:
        """ extend item to dictionary value for last key of key list
            the item must be able to extend the extendable value
        """
        # Dictionary is None or empty
        if not dic or not keys:
            return
        if item0 is None:
            item0 = []
        if not isinstance(keys, (list, tuple)):
            keys = [keys]
        if not isinstance(value, (list, tuple)):
            value = [value]

        _dic = cls.locate(dic, keys[:-1])
        if not _dic:
            return
        # last element
        key_last = keys[-1]
        if key_last not in _dic:
            _dic[key_last] = item0

        if isinstance(_dic[key_last], (list, tuple)):
            _dic[key_last].extend(value)

    @classmethod
    def new(
            cls, keys: Any, value: Any) -> TN_Dic:
        """ create a new dictionary from keys and values
        """
        if keys is None:
            return None
        if value is None:
            return None
        dic_new: T_Dic = {}
        if isinstance(keys, str):
            dic_new[keys] = value
            return dic_new
        cls.set(dic_new, keys, value)
        return dic_new

    @staticmethod
    def flatten_keys(
            arr: TN_Arr, d_flatten: TN_Dic) -> Any:
        if arr is None:
            return arr
        if d_flatten is not None:
            sw = d_flatten.get('sw')
            sep: Any = d_flatten.get('sep', '.')
        if sw:
            return sep.join(arr)
        else:
            return arr[-1]

    @classmethod
    def flatten_merge_arr_to_aod(
            cls, arr: T_Arr, keys: Any, aod: T_AoD, d_flatten: TN_Dic) -> T_AoD:
        if not arr:
            return aod
        _aod_list: T_AoD = []
        _aod_dict: T_AoD = []
        _aod_else: T_AoD = []
        for _item in arr:
            if isinstance(_item, list):
                _aod: T_AoD = []
                _aod = cls.flatten_merge_arr_to_aod(_item, keys, _aod, d_flatten)
                _aod_list.extend(_aod)
            elif isinstance(_item, dict):
                _aod = []
                _aod = cls.flatten_to_aod(_item, keys, _aod, d_flatten)
                _aod_dict.extend(_aod)
            else:
                _key = cls.flatten_keys(keys, d_flatten)
                _dic = {_key : _item}
                _aod = AoD.merge_dic(aod, _dic)
                _aod_else.extend(_aod)

        aod = AoD.join_aod(aod, _aod_list)
        aod = AoD.join_aod(aod, _aod_dict)
        aod = AoD.join_aod(aod, _aod_else)

        return aod

    @classmethod
    def flatten_to_aod(
            cls, dic: TN_Dic, keys: Any, aod: T_AoD, d_flatten: TN_Dic) -> T_AoD:
        if not dic:
            return aod
        _dic_else: T_Dic = {}
        for _key, _val in dic.items():
            if isinstance(_val, dict):
                _keys = keys.copy()
                _keys.append(_key)
                _aod: T_AoD = []
                _aod = cls.flatten_to_aod(_val, _keys, _aod, d_flatten)
                aod = AoD.join_aod(aod, _aod)
            elif isinstance(_val, list):
                _keys = keys.copy()
                _keys.append(_key)
                aod = cls.flatten_merge_arr_to_aod(_val, _keys, aod, d_flatten)
            else:
                _dic_else[_key] = _val

        aod = AoD.merge_dic(aod, _dic_else)
        return aod

    @classmethod
    def flatten(cls, dic: TN_Dic, d_flatten: TN_Dic) -> T_AoD:
        _aod: T_AoD = []
        if not dic:
            return _aod
        _keys: T_Arr = []
        _aod = cls.flatten_to_aod(dic, _keys, _aod, d_flatten)
        _aod = cls.apply_function(d_flatten, _aod)
        return _aod

    @staticmethod
    def apply_function(d_flatten: TN_Dic, aod: T_AoD) -> T_AoD:
        if not d_flatten:
            return aod
        _fnc: TN_Callable = d_flatten.get("fnc")
        if not _fnc:
            return aod
        _kwargs: TN_Dic = d_flatten.get("kwargs")
        _aod = AoD.apply_function(aod, _fnc, _kwargs)
        return _aod

    @classmethod
    def flatten_using_d2p(
            cls, dic: TN_Dic,
            d_meta: TN_Dic,
            d_flatten: TN_Dic) -> TN_AoD:
        if d_meta is not None:
            meta_key = d_meta['key']
            d_meta_kv = d_meta['kv']
            aod2p, d_other = cls.split_by_key(dic, meta_key)
            dic = AoD2P.to_dic_by_dic(aod2p, d_meta_kv)
            aod = cls.flatten(d_other, d_flatten)
            return AoD.merge_dic(aod, dic)
        else:
            aod = cls.flatten(dic, d_flatten)
            return aod

    @staticmethod
    def locate(dic: T_Dic, a_key: T_ArrTup) -> Any:
        """ locate the value using keys in a nested dictionary
        """
        if not dic:
            msg = f"Parameter dic = {dic} should be a dictionary but is not defined"
            raise Exception(msg)
        if not a_key:
            msg = f"Parameter a_key = {a_key} should be an array but is not defined"
            raise Exception(msg)

        _dic = dic
        for key in a_key:
            if key not in _dic:
                _dic[key] = {}
            _dic = _dic[key]
        return _dic

    @classmethod
    def sh_bool(cls, dic: T_Dic, a_key: T_ArrTup, switch: bool = False) -> bool:
        """ locate the value using keys in a nested dictionary
        """
        value = cls.locate(dic, a_key)
        if value is None:
            return switch
        if isinstance(value, bool):
            return value
        return switch

    @staticmethod
    def sh_value(
            dic: T_Dic, keys: Any, default: Any = None) -> Any:
        """ locate the value using keys in a nested dictionary
        """
        if not dic or not keys:
            return dic
        if not isinstance(keys, (list, tuple)):
            if keys not in dic:
                return default
            return dic[keys]

        _dic = dic
        for key in keys:
            if key not in _dic:
                return default
            _dic = _dic[key]
        return _dic

    @staticmethod
    def sh_dic(dic: T_Dic) -> T_Dic:
        dic_new = {}
        for key, value in dic.items():
            f_key = frozenset(key.split(','))
            dic_new[f_key] = value
        return dic_new

    @staticmethod
    def replace_keys(
            dic: T_Dic, old: Any, new: Any) -> T_Dic:
        dic_new = {}
        for key, value in dic.items():
            key_ = key.replace(old, new)
            dic_new[key_] = value
        return dic_new

    @classmethod
    def set(cls, dic: T_Dic, keys: Any, value: Any) -> None:
        if not isinstance(keys, (list, tuple)):
            dic[keys] = value
            return
        _keys: T_ArrTup = keys[:-1]
        _dic = cls.locate(dic, _keys)
        if not _dic:
            return
        key_last = keys[-1]
        _dic[key_last] = value

    @classmethod
    def set_by_keys(cls, dic: T_Dic, keys: Any, value: Any) -> None:
        """ assign value to last key of a nested dictionary defined by keys
        """
        if not isinstance(keys, (list, tuple)):
            dic[keys] = value
            return
        _keys = keys[:-1]
        _dic = cls.locate(dic, _keys)
        if not _dic:
            return
        key_last = keys[-1]
        _dic[key_last] = value

    @staticmethod
    def set_by_key_pair(dic: T_Dic, src_key: Any, tgt_key: Any) -> None:
        """ assign value to last key of a nested dictionary defined by keys
        """
        if src_key in dic and tgt_key in dic:
            dic[tgt_key] = dic[src_key]

    @classmethod
    def cnt(
            cls, dic: T_Dic, keys: Any, counter: Any = None) -> None:
        if counter is None:
            counter = 1
        if not isinstance(keys, (list, tuple)):
            if keys not in dic:
                dic[keys] = 0
            dic[keys] = dic[keys] + counter
            return

        _dic = cls.locate(dic, keys[:-1])
        if not _dic:
            return
        key_last = keys[-1]
        if key_last not in _dic:
            _dic[key_last] = 0
        _dic[key_last] = _dic[key_last] + counter

    @classmethod
    def set_if_none(cls, dic: T_Dic, keys: Any, value_last: Any) -> None:
        if not isinstance(keys, (list, tuple)):
            keys = [keys]
        _dic = cls.locate(dic, keys[:-1])
        if not _dic:
            return
        # last element
        key_last = keys[-1]
        if key_last not in _dic:
            _dic[key_last] = value_last

    @staticmethod
    def increment(
            dic: TN_Dic, keys: None | T_ArrTup, item0: Any = 1) -> None:
        if dic is None:
            return
        if keys is None:
            return
        if not isinstance(keys, (list, tuple)):
            keys = [keys]
        dic_ = dic

        # all element except the last one
        for key in keys[:-1]:
            if key not in dic_:
                dic_[key] = {}
            dic_ = dic_[key]

        # last element
        key = keys[-1]

        if key not in dic_:
            dic_[key] = item0
        else:
            dic_[key] += 1

    @staticmethod
    def lstrip_keys(
            dic: T_Dic, str: str) -> T_Dic:
        dic_new: T_Dic = {}
        for k, v in dic.items():
            k_new = k.replace(str, "", 1)
            dic_new[k_new] = v
        return dic_new

    @staticmethod
    def is_not(dic: T_Dic, key: str) -> TN_Bool:
        if key in dic:
            return not dic[key]
        else:
            return None

    @staticmethod
    def nvl(dic: None | T_Dic) -> T_Dic:
        """ nvl function similar to SQL NVL function
        """
        if dic is None:
            return {}
        return dic

    @staticmethod
    def sh_prefixed(dic: T_Dic, prefix: str) -> T_Dic:
        dic_new: T_Dic = {}
        for k, v in dic.items():
            dic_new[f"{prefix}_{k}"] = v
        return dic_new

    @staticmethod
    def sh_value2keys(dic: T_Dic) -> T_Dic:
        dic_new: T_Dic = {}
        for key, value in dic.items():
            if value not in dic_new:
                dic_new[value] = []
            if key not in dic_new[value]:
                dic_new[value].extend(key)
        return dic_new

    class Names:

        @staticmethod
        def sh(d_data: T_Dic, key: str = 'value') -> Any:
            try:
                return Obj.extract_values(d_data, key)
            except Exception:
                return []

        @classmethod
        def sh_item0(cls, d_names: T_Dic) -> Any:
            names = cls.sh(d_names)
            if not names:
                return None
            return names[0]

        @classmethod
        def sh_item0_if(cls, string: str, d_names: T_Dic) -> Any:
            names = cls.sh(d_names)
            if not names:
                return None
            if string in d_names[0]:
                return names[0]
            return None

    class Key:

        @staticmethod
        def change(
                dic: T_Dic, source_key: T_Dic, target_key: T_Dic) -> T_Dic:
            if source_key in dic:
                dic[target_key] = dic.pop(source_key)
            return dic

    class Value:

        @staticmethod
        def get(
                dic: T_Dic, keys: Any, default: Any = None):
            if keys is None:
                return dic
            if not isinstance(keys, (list, tuple)):
                keys = [keys]
            if len(keys) == 0:
                return dic
            value = dic
            for key in keys:
                if key not in value:
                    return default
                value = value[key]
                if value is None:
                    break
            return value

        @classmethod
        def set(
                cls, dic: TN_Dic, keys: TN_ArrTup,
                value: Any) -> None:
            if value is None:
                return
            if dic is None:
                return
            if keys is None:
                return

            if not isinstance(keys, (list, tuple)):
                keys = [keys]

            value_curr = cls.get(dic, keys[:-1])
            if value_curr is None:
                return
            last_key = keys[-1]
            if last_key in value_curr:
                value_curr[last_key] = value

        @staticmethod
        def is_empty_value(
                value: Any) -> bool:
            if value is None:
                return True
            elif isinstance(value, str):
                if value == '':
                    return True
            elif isinstance(value, (list, tuple)):
                if value == []:
                    return True
            elif isinstance(value, dict):
                if value == {}:
                    return True
            return False

        @classmethod
        def is_empty(
                cls, dic: TN_Dic, keys: T_ArrTup) -> bool:
            if dic is None:
                return True
            if not isinstance(keys, (tuple, list)):
                keys = [keys]
            if isinstance(keys, (list, tuple)):
                value = cls.get(dic, keys)
                return cls.is_empty_value(value)
            return False

        @classmethod
        def is_not_empty(
                cls, dic: TN_Dic, keys: T_ArrTup) -> bool:
            return not cls.is_empty(dic, keys)

    @staticmethod
    def change_keys_with_keyfilter(
            dic: T_Dic, keyfilter: T_Dic) -> T_Dic:
        dic_new: T_Dic = {}
        for key, value in dic.items():
            key_new = keyfilter.get(key)
            if key_new is None:
                continue
            dic_new[key_new] = value
        return dic_new

    @staticmethod
    def yield_values_with_keyfilter(
            dic: T_Dic, keyfilter: T_Dic) -> T_IterAny:
        for key, value in dic.items():
            if key in keyfilter:
                yield value

    @staticmethod
    def get(
            dic: T_Dic, keys: T_ArrTup) -> TN_Any:
        # Dictionary is None or empty
        if not dic:
            return None
        _dic = dic
        value = None
        if not isinstance(keys, (list, tuple)):
            return dic.get(keys)
        for _key in keys:
            value = _dic.get(_key)
            if value is None:
                return None
            if not isinstance(value, dict):
                return value
            _dic = value
        return value

    @staticmethod
    def split_by_key(
            dic: TN_Dic, key: TN_Any) -> T_Tup:
        # Dictionary is None or empty
        if not dic or not key:
            return dic, None
        dic_new = {}
        obj_new = None
        for k, v in dic.items():
            if k == key:
                obj_new = v
            else:
                dic_new[k] = v
        return obj_new, dic_new

    @staticmethod
    def split_by_value(
            dic: T_Dic, value: Any) -> TN_Any:
        # Dictionary is None or empty
        if not dic:
            return dic, dic
        dic0 = {}
        dic1 = {}
        for k, v in dic.items():
            if v == value:
                dic0[k] = v
            else:
                dic1[k] = v
        return dic0, dic1

    @staticmethod
    def split_by_value_endswith(
            dic: T_Dic, value: Any) -> TN_Any:
        # Dictionary is None or empty
        if not dic:
            return dic, dic
        dic0 = {}
        dic1 = {}
        for k, v in dic.items():
            if v.endswith(value):
                dic0[k] = v
            else:
                dic1[k] = v
        return dic0, dic1

    @staticmethod
    def split_by_value_is_int(
            dic: T_Dic) -> TN_Any:
        # Dictionary is None or empty
        if not dic:
            return dic, dic
        dic0 = {}
        dic1 = {}
        for k, v in dic.items():
            if v.isdigit():
                dic0[k] = v
            else:
                dic1[k] = v
        return dic0, dic1

    @staticmethod
    def dic2aod(
            dic: T_Dic, key_name: Any, value_name: Any) -> T_AoD:
        # Dictionary is None or empty
        if not dic:
            aod = [dic, dic]
        aod = []
        _dic = {}
        for k, v in dic.items():
            _dic[key_name] = k
            _dic[value_name] = v
            aod.append(_dic)
            _dic = {}
        return aod
