#!/usr/bin/env python
"""
Complete graphs are composed of dictionaries keyed by integers that connect
every node to every other node.

For example, a complete graph with five nodes looks like:
    {0: {1: 1, 2: 1, 3: 1, 4: 1},
     1: {0: 1, 2: 1, 3: 1, 4: 1},
     2: {0: 1, 1: 1, 3: 1, 4: 1},
     3: {0: 1, 1: 1, 2: 1, 4: 1},
     4: {0: 1, 1: 1, 2: 1, 3: 1}}
"""
from graph_utils import make_link


def make_complete_graph(n):
    """
    Create a complete graph with `n` nodes.
    """
    G = {}

    for i in range(n):
        for j in range(n):
            if i < j:
                make_link(G, i, j)

    return G
