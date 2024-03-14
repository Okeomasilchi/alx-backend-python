#!/usr/bin/env python3
""" complex types - list of floats """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by multiplier
    """

    def f(n: float) -> float:
        """
        returns a float
        """
        return n * multiplier

    return f
