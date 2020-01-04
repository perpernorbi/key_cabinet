import svgwrite
from svgwrite.path import Path
from svgwrite.shapes import Rect, Line, Circle
from svgwrite.container import Group
from operator import sub, add

dashed_line = {'style': 'stroke:#000000;stroke-opacity:1;fill:none;stroke-width:0.4;stroke-dasharray:1.0,1.0'}
solid_line = {'style': 'stroke:#000000;stroke-opacity:1;fill:none;stroke-width:0.4'}


def R(*, x1=None, x2=None, y1=None, y2=None, w=None, h=None, **kwargs):
    x1 = x2 - w if x1 is None else x1
    y1 = y2 - h if y1 is None else y1
    w = x2 - x1 if w is None else w
    h = y2 - y1 if h is None else h

    if w < 0:
        x1 = x1 + w
        w = -w

    if h < 0:
        y1 = y1 - h
        h = -h

    return Rect((x1, y1), (w, h), **kwargs)




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


def corners(insert, size):
    return ((insert[0], insert[1]),
            (insert[0], insert[1]+size[1]),
            (insert[0]+size[0], insert[1]),
            (insert[0]+size[0], insert[1]+size[1]),
            )


def chamfered_rect_front(insert, size, c, **extra):
    g = Group()
    g.add(Rect(insert, size, **extra))
    inner_insert, inner_size = tuple(map(add, insert, (c, c))), tuple(map(sub, size, (2*c, 2*c)))
    g.add(Rect(inner_insert, inner_size, **extra))
    for a,b in zip(corners(insert, size), corners(inner_insert, inner_size)):
        g.add(Line(a,b, **extra))
    return g


def door_front():
    w = 162
    h = 260
    f = 40
    chamfer = 2
    groove_depth = 10
    g = Group()
    g.add(Line((f - groove_depth, 0), (f - groove_depth, h), **dashed_line))
    g.add(chamfered_rect_front((0, 0), (f, h), chamfer, **solid_line))

    g.add(Rect((f - groove_depth + 1, 0), (w-2*f+2*groove_depth-2, f-groove_depth), **dashed_line))
    g.add(chamfered_rect_front((f, 0), (w-2*f, f), chamfer, **solid_line))

    g.add(Rect((f - groove_depth + 1, h-f+groove_depth), (w-2*f+2*groove_depth-2, f-groove_depth), **dashed_line))
    g.add(chamfered_rect_front((f, h-f), (w-2*f, f), chamfer, **solid_line))

    g.add(Line((w - f + groove_depth, 0), (w - f + groove_depth, h), **dashed_line))
    g.add(chamfered_rect_front((w-f, 0), (f, h), chamfer, **solid_line))

    g.add(Rect((f - groove_depth + 1, f-groove_depth + 1), (w-2*f+2*groove_depth-2, h-2*f+2*groove_depth-2), **dashed_line))

    g.add(Circle((17, 53), 13, **dashed_line))
    g.add(Circle((17, h-53), 13, **dashed_line))
    return g


def door_side():
    h = 260
    g = Group()
    g.add(Rect((7, 0), (4, 30), **dashed_line))
    g.add(Rect((7, h-30), (4, 30), **dashed_line))
    g.add(Rect((6.5, 0), (5, h), **dashed_line))
    g.add(Rect((18-13, 53-13), (13, 26), **dashed_line))
    g.add(Rect((18-13, h-53-13), (13, 26), **dashed_line))
    g.add(Path(f'M2 0 L18 0 L18 {h} L2 {h} L0 {h-2} L0 2 Z', **solid_line))
    return g


def cabinet_front():
    g = Group()
    g.add(Rect((0,0), (340,15), **solid_line))
    g.add(Rect((5,15), (15, 260), **solid_line))
    g.add(Rect((320,15), (15, 260), **solid_line))

    g.add(Rect((20,260), (300, 15), **solid_line))
    g.add(Path('M10 275 l 0 -15 l 10 0', **dashed_line))
    g.add(Path('M330 275 l 0 -15 l -10 0', **dashed_line))

    g.add(Rect((20, 15), (300, 40), **solid_line))
    g.add(Path('M10 15 l0 40 l10 -2', **dashed_line))
    g.add(Path('M330 15 l0 40 l-10 -2', **dashed_line))

    g.add(Rect((20,137.5), (300,40), **solid_line))
    g.add(Path('M10 137.5 l0 40 l10 -2', **dashed_line))
    g.add(Path('M330 137.5 l0 40 l-10 -2', **dashed_line))
    g.add(Path('M10 137.5 l10 2', **dashed_line))
    g.add(Path('M330 137.5 l-10 2', **dashed_line))

    g.add(Rect((9.5, 5), (6, 37), **dashed_line))
    g.add(Line((9.5, 6), (15.5, 6), **dashed_line))
    g.add(Line((9.5, 41), (15.5, 41), **dashed_line))

    g.add(Rect((340-9.5-6, 5), (6, 37), **dashed_line))
    g.add(Line((340-9.5, 6), (340-15.5, 6), **dashed_line))
    g.add(Line((340-9.5, 41), (340-15.5, 41), **dashed_line))
    return g


def domino_face(x, y, **kwargs):
    g = Group()
    g.add(R(x1=x, y1=y, w=21, h=37, **kwargs))
    g.add(R(x1=x+1, y1=y+1, w=19, h=35, **kwargs))
    return g


def cabinet_side():
    g = Group()
    g.add(R(x1=0, y1=0, w=120, h=15, **solid_line))
    g.add(R(x2=120, y1=5, w=4, y2=15+260-5, **dashed_line))
    g.add(R(x2=120, y1=15, w=100, h=260, **solid_line))
    g.add(domino_face(40, 5, **dashed_line))
    g.add(domino_face(75, 5, **dashed_line))

    g.add(R(x2=120, y1=15, w=19, h=40, **dashed_line))
    g.add(Line((120-19, 15+40-2), (120, 15+40-2), **dashed_line))

    g.add(R(x2=120, y1=137.5, w=19, h=40, **dashed_line))
    g.add(Line((120-19, 137.5+40-2), (120, 137.5+40-2), **dashed_line))
    g.add(Line((120-19, 137.5+2), (120, 137.5+2), **dashed_line))
    return g


def cabinet_bottom():
    g = Group()
    g.add(R(x1=0, y1=0, w=340, h=120, **solid_line))
    g.add(R(x1=5, y1=0, w=330, h=100, **solid_line))

    h = 100
    w = 10
    t = 3
    a = h/(3.0*t+1)

    return g


dwg = svgwrite.Drawing('/d/tmp/a/test.svg', profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
#dwg.add(sheet())
#p = Path(**dashed_line)
#p.push('M 100 100')
#p.push('100 200 200 200')
dwg = svgwrite.Drawing('/d/tmp/a/cabinet_front.svg', profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(cabinet_front())
dwg.save()
#dwg.add(door_front())
#dwg.add(door_side())
dwg = svgwrite.Drawing('/d/tmp/a/cabinet_side.svg', profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(cabinet_side())
dwg.save()

dwg = svgwrite.Drawing('/d/tmp/a/cabinet_bottom.svg', profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(cabinet_bottom())
dwg.save()