#!/usr/bin/env python3

from typing import TypeVar, Mapping, Any, Union

K = TypeVar('K')  # Type variable for the dictionary key
V = TypeVar('V')  # Type variable for the dictionary value

def safely_get_value(dct: Mapping[K, V], key: K, default: Union[V, None] = None) -> Union[V, None]:
    if key in dct:
        return dct[key]
    else:
        return default