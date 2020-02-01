from svgwrite.container import Group
from svgwrite.shapes import Rect, Line
from .util import R


def face(x, y, **kwargs):
    g = Group()
    g.add(Rect(*R(x1=x, y1=y, w=21, h=37), **kwargs))
    g.add(Rect(*R(x1=x+1, y1=y+1, w=19, h=35), **kwargs))
    return g


def side(x, y, **kwargs):
    g = Group()
    g.add(Rect(*R(x1=x, y1=y, w=6, h=21), **kwargs))
    g.add(Line((x, y+1), (x+6, y+1), **kwargs))
    g.add(Line((x, y+20), (x+6, y+20), **kwargs))
    return g
