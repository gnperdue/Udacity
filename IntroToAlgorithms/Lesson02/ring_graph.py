#!/usr/bin/env python
"""
We will model graphs as dictionaries of ndoes where the key is the node and
the value is the number of connections or a dictionary where there are more
than one connection present.

For example, a ring graph with 5 links looks like:
    {0: {1: 1, 4: 1},
     1: {0: 1, 2: 1},
     2: {1: 1, 3: 1},
     3: {2: 1, 4: 1},
     4: {0: 1, 3: 1}}

Node 0 has two links - internally, those links are node 1 with a single link
(1) and node 4 with a single link (1).
"""
from graph_utils import make_link


def make_ring(n):
    """
    Return a ring graph as a dictionary with `n` nodes.
    """
    a_ring = {}
    for i in range(n):
        make_link(a_ring, i, (i + 1) % n)

    return a_ring
