#!/usr/bin/env python

from graph_utils import make_link
import math
import random


def makeG(n):
    if n == 1:
        return 'n'
    g1 = makeG(n / 2)
    g2 = makeG(n / 2)
    for i in range(int(math.log(n, 2))):
        i1 = random.choice(g1)
        i2 = random.choice(g2)

