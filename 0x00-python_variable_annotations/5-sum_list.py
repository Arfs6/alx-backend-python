#!/usr/bin/env python3
"""A function that sum a list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Adds all element of @input_list an returns the result."""
    result = 0.0
    for num in input_list:
        result += num
    return result
