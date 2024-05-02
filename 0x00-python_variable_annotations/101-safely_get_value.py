#!/usr/bin/env python3

from typing import TypeVar, Dict, Any, Optional

K = TypeVar('K')  # Type variable for the dictionary key
V = TypeVar('V')  # Type variable for the dictionary value

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    if key in dct:
        return dct[key]
    else:
        return default
