from svgwrite.container import Group
from svgwrite.shapes import Rect


def sheet():
    l = {'style': 'stroke:#000000;stroke-opacity:1;fill:none;stroke-width:0.5'}
    g = Group()
    g.add(Rect((10, 10), (190, 277), **l))

    g.add(Rect((10, 10), (60, 7.5), **l))
    g.add(Rect((10, 10), (60, 15), **l))
    g.add(Rect((180, 10), (20, 7.5), **l))
    g.add(Rect((180, 10), (20, 15), **l))
    g.add(Rect((10, 10), (190, 15), **l))
    return g

