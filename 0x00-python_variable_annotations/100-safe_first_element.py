#!/usr/bin/env python3
""" 100. Safe first element! """

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a list."""
    if lst:
        return lst[0]
    else:
        return None
