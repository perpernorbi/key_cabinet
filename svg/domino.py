from svgwrite.container import Group
from svgwrite.shapes import Rect
from .util import R


def face(x, y, **kwargs):
    g = Group()
    g.add(Rect(*R(x1=x, y1=y, w=21, h=37), **kwargs))
    g.add(Rect(*R(x1=x+1, y1=y+1, w=19, h=35), **kwargs))
    return g

