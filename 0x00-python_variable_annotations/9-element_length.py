#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    The function `element_length` takes an iterable of
    sequences and returns a list of tuples where each
    tuple contains a sequence from the input along with
    its length.

    Args:
      lst (Iterable[Sequence]): iterable containing sequences.

    Returns:
      list of tuples.
    """
    return [(i, len(i)) for i in lst]
