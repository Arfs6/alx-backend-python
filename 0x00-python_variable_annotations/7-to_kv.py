#!/usr/bin/env python3
"""Type annotation"""

from typing import Tuple, Optional


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple of @k and @v squared."""
    return k, v ** 2
