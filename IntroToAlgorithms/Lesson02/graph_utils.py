#!/usr/bin/env python
"""
We will model graphs as dictionaries of ndoes where the key is the node
and the value is the number of connections.
"""


def make_link(G, node1, node2):
    """
    `G` is a graph represented as a dictionary. We modify the graph in
    place, so by Pythonic convention, we return `None`.
    """
    if node1 not in G:
        G[node1] = {}
    G[node1][node2] = 1
    if node2 not in G:
        G[node2] = {}
    G[node2][node1] = 1
    return None


def count_nodes(G):
    return len(G)


def count_edges(G):
    return sum([len(G[node]) for node in G.keys()]) / 2
