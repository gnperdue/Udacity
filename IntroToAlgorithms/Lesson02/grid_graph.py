#!/usr/bin/env python
"""
Grid graphs are built from dictionaries keyed by tuples. For example, here
is a 2x2 grid graph:
    {(0, 0): {(0, 1): 1, (1, 0): 1},
     (0, 1): {(0, 0): 1, (1, 1): 1},
     (1, 0): {(0, 0): 1, (1, 1): 1},
     (1, 1): {(0, 1): 1, (1, 0): 1}}
"""
from graph_utils import make_link
import math


def make_grid(n):
    """
    Make a grid graph wih n nodes. This function always returns _sqaure_
    grids.
    """
    G = {}
    side = int(math.sqrt(n))

    # add edges
    for i in range(side):
        for j in range(side):
            if i < side - 1:
                make_link(G, (i, j), (i + 1, j))
            if j < side - 1:
                make_link(G, (i, j), (i, j + 1))

    return G
