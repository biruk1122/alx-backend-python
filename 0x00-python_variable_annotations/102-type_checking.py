#!/usr/bin/env python3

from typing import Tuple, List, Any

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)  # Use tuple instead of list

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Use integer instead of float
