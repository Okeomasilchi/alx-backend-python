#!/usr/bin/env python3
""" 102. Type Checking """


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Zooms in on each element in the input tuple by
    repeating it 'factor' times.

    Args:
        lst (Tuple): containing elements to be zoomed in
            on.
        factor (int, optional): The factor by which each
            element should be zoomed in. Defaults to 2.

    Returns:
        Tuple: A new tuple containing the zoomed-in
        elements.
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return tuple(zoomed_in)


array = (12, 72, 91)  # Use a tuple instead of a list

zoom_2x = zoom_array(array)

# Provide an integer value for the factor parameter
zoom_3x = zoom_array(array, 3)
