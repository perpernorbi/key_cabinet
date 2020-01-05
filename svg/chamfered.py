from svgwrite.container import Group
from svgwrite.shapes import Rect, Line
from .util import corners

from operator import sub, add


def front(insert, size, c, **extra):
    g = Group()
    g.add(Rect(insert, size, **extra))
    inner_insert, inner_size = tuple(map(add, insert, (c, c))), tuple(map(sub, size, (2*c, 2*c)))
    g.add(Rect(inner_insert, inner_size, **extra))
    for a,b in zip(corners(insert, size), corners(inner_insert, inner_size)):
        g.add(Line(a,b, **extra))
    return g
