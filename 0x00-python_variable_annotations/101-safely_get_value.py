#!/usr/bin/env python3
""" 101. Safely get value! """

from typing import Mapping, Any, Union, TypeVar

# Define a type variable for the return type
T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to look up in the dictionary.
        default (Optional[T], optional): The default value to
            return if the key is not found in the dictionary.
            Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if it
        exists in the dictionary, or the default value otherwise.
    """
    if key in dct:
        return dct[key]
    else:
        return default
