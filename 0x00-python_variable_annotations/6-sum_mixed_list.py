#!/usr/bin/env python3
"""A function that adds ints and float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of all elements in @mxd_lst"""
    result = 0.0
    for num in mxd_lst:
        result += num
    return result
