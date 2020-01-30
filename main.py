from dovetail import DoveTail

from svg.dovetail import dovetail_tail_end, dovetail_pin_end, dovetail_tail_face, dovetail_tail_face_helpers, dovetail_diagonals
import svg.chamfered
import svg.domino
import svg.sheet
from svg.dimension import dimension as dimension
from svg.util import R

import svgwrite
from svgwrite.path import Path
from svgwrite.shapes import Rect, Line, Circle
from svgwrite.container import Group


import math

dashed_line = {'style': 'stroke:#000000;stroke-opacity:1;fill:none;stroke-width:0.4;stroke-dasharray:1.0,1.0'}
dashed_line = {'style': 'stroke:#000000;stroke-opacity:0;fill:none;stroke-width:0.4;stroke-dasharray:1.0,1.0'}
solid_line = {'style': 'stroke:#000000;stroke-opacity:1;fill:none;stroke-width:0.6'}
dimension_line = {'style': 'stroke:#202020;stroke-opacity:1;fill:none;stroke-width:0.3'}
helper_line = {'style': 'stroke:#606060;stroke-opacity:1;fill:none;stroke-width:0.25'}

dovetail = DoveTail(10, 100, 3)


def door_front():
    w = 162
    h = 258
    f = 40
    chamfer = 2
    groove_depth = 10
    g = Group()
    g.add(Line((f - groove_depth, 0), (f - groove_depth, h), **dashed_line))
    g.add(svg.chamfered.front((0, 0), (f, h), chamfer, **solid_line))

    g.add(Rect((f - groove_depth + 1, 0), (w-2*f+2*groove_depth-2, f-groove_depth), **dashed_line))
    g.add(svg.chamfered.front((f, 0), (w-2*f, f), chamfer, **solid_line))

    g.add(Rect((f - groove_depth + 1, h-f+groove_depth), (w-2*f+2*groove_depth-2, f-groove_depth), **dashed_line))
    g.add(svg.chamfered.front((f, h-f), (w-2*f, f), chamfer, **solid_line))

    g.add(Line((w - f + groove_depth, 0), (w - f + groove_depth, h), **dashed_line))
    g.add(svg.chamfered.front((w-f, 0), (f, h), chamfer, **solid_line))

    g.add(Rect((f - groove_depth + 1, f-groove_depth + 1), (w-2*f+2*groove_depth-2, h-2*f+2*groove_depth-2), **dashed_line))

    g.add(Circle((17, 55), 13, **dashed_line))
    g.add(Circle((17, h-55), 13, **dashed_line))
    return g


def door_side():
    h = 258
    g = Group()
    g.add(Rect((7, 0), (4, 30), **dashed_line))
    g.add(Rect((7, h-30), (4, 30), **dashed_line))
    g.add(Line((6.5, 0), (6.5, h), **dashed_line))
    g.add(Line((6.5+5, 0), (6.5+5, h), **dashed_line))
    g.add(Rect((18-13, 55-13), (13, 26), **dashed_line))
    g.add(Rect((18-13, h-55-13), (13, 26), **dashed_line))
    g.add(Path('M0 38 l2 2 l16 0', **dashed_line))
    g.add(Path(f'M0 {h-38} l2 -2 l16 0', **dashed_line))
    g.add(Path(f'M2 0 L18 0 L18 {h} L2 {h} L0 {h-2} L0 2 Z', **solid_line))
    return g


def door_left_top(full_dashed = False):
    solid_or_dashed = dashed_line if full_dashed else solid_line

    w = 162
    c = 2
    g = Group()
    g.add(Path(f'M0 0 l40 0 l0 6.5 l-10 0 l0 5 l10 0 l0 {6.5-c} l{-c} {c} l{2*c-40} 0 l{-c} {-c} Z', **solid_or_dashed))
    g.add(Path(f'M{w} 0 l-40 0 l0 6.5 l10 0 l0 5 l-10 0 l0 {6.5-c} l{c} {c} l{40-2*c} 0 l{c} {-c} Z',
               **solid_or_dashed))
    g.add(Path(f'M40 0 l{w-2*40} 0 l0 6.5 l9 0 l0 5 l-9 0 l0 {6.5-c} l{-c} {c} l{-w+2*40+2*c} 0 l{-c} {-c} l0 {-6.5+c} '
               f'l-9 0 l0 -5 l9 0 Z', **solid_or_dashed))
    g.add(Rect((31, 7), (100, 4), **dashed_line))
    g.add(Rect((4, 0), (26, 13), **dashed_line))
    return g


def halved_line(start, end, first, second):
    g = Group()
    midpoint = (start[0] + (end[0] - start[0])/2.0, start[1] + (end[1] - start[1])/2.0)
    g.add(Line(start, midpoint, **first))
    g.add(Line(midpoint, end, **second))
    return g


def cabinet_front(left_dashed = False):
    solid_or_dashed = dashed_line if left_dashed else solid_line
    g = Group()
    g.add(Rect((0,0), (340,15), **solid_line))

    # left side panel
    #g.add(Rect((5,15), (15, 260), **solid_line))
    g.add(Line((5,15), (5, 275), **solid_line))
    g.add(Line((20,15), (20, 275), **solid_or_dashed))
    if left_dashed:
        g.add(Line((20, 15), (20, 16), **solid_line))
        g.add(Line((20, 274), (20, 275), **solid_line))
    g.add(Line((5, 275), (20, 275), **solid_line))

    # right side panel
    g.add(Rect((320,15), (15, 260), **solid_line))

    # bottom panel
    #g.add(Rect((20, 260), (300, 15), **solid_line))
    g.add(halved_line((20,260), (20+300, 260), solid_or_dashed, solid_line))
    g.add(Line((20,275), (20+300, 275), **solid_line))
    g.add(Path('M10 275 l 0 -15 l 10 0', **dashed_line))
    g.add(Path('M330 275 l 0 -15 l -10 0', **dashed_line))

    # upper hanger
    #g.add(Rect((20, 15), (300, 40), **solid_line))
    g.add(halved_line((20, 15+40), (20+300, 15+40), solid_or_dashed, solid_line))
    g.add(Path('M10 15 l0 40 l10 -2', **dashed_line))
    g.add(Path('M330 15 l0 40 l-10 -2', **dashed_line))

    # lower hanger
    #g.add(Rect((20,137.5), (300,40), **solid_line))
    g.add(halved_line((20, 137.5), (20+300, 137.5), solid_or_dashed, solid_line))
    g.add(halved_line((20, 137.5+40), (20+300, 137.5+40), solid_or_dashed, solid_line))
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


def cabinet_side():
    g = Group()
    g.add(Rect(*R(x1=0, y1=0, w=120, h=15), **solid_line))
    g.add(Rect(*R(x2=120, y1=5, w=4, y2=15+260-5), **dashed_line))
    g.add(Rect(*R(x2=120, y1=15, w=100, h=260), **solid_line))
    g.add(svg.domino.face(40, 5, **dashed_line))
    g.add(svg.domino.face(75, 5, **dashed_line))

    g.add(Rect(*R(x2=120, y1=15, w=19, h=40), **dashed_line))
    g.add(Line((120-19, 15+40-2), (120, 15+40-2), **dashed_line))

    g.add(Rect(*R(x2=120, y1=137.5, w=19, h=40), **dashed_line))
    g.add(Line((120-19, 137.5+40-2), (120, 137.5+40-2), **dashed_line))
    g.add(Line((120-19, 137.5+2), (120, 137.5+2), **dashed_line))

    dovetail_end = dovetail_tail_end(dovetail, 15, dashed_line, dashed_line)
    dovetail_end.add(Line((0,0), (96, 0), **dashed_line))
    dovetail_end.translate(20, 260)
    g.add(dovetail_end)
    return g


def cabinet_bottom():
    g = Group()

    #back hangers
    g.add(Rect(*R(x1=5+5, y1=4, w=320, h=15), **dashed_line))

    dovetail_left = Group()
    dovetail_left.add(dovetail_tail_face(dovetail, **dashed_line))
    dovetail_left.add(dovetail_pin_end(dovetail, **solid_line))
    dovetail_left.add(Line((0, dovetail.w), (dovetail.l, dovetail.w), **solid_line))
    dovetail_left.add(dovetail_tail_face_helpers(dovetail, angle=math.pi/12, **helper_line))
    dovetail_left.rotate(90)
    dovetail_left.translate(0, -20)
    g.add(dovetail_left)

    dovetail_right = Group()
    dovetail_right.add(dovetail_tail_face(dovetail, **dashed_line))
    dovetail_right.add(dovetail_pin_end(dovetail, **solid_line))
    dovetail_right.add(Line((0, dovetail.w), (dovetail.l, dovetail.w), **solid_line))
    dovetail_right.rotate(-90)
    dovetail_right.translate(-dovetail.l, 330-dovetail.w)
    g.add(dovetail_right)

    g.add(Rect(*R(x1=0, y1=0, w=340, h=120), **solid_line))
    g.add(Rect(*R(x1=5, y1=0, w=330, h=100), **solid_line))
    return g


def cabinet_top():
    g = Group()

    #back hangers
    #g.add(Rect(*R(x1=5+5, y1=4, w=320, h=15), **dashed_line))
    g.add(Line((5+5, 4), (5+5+320, 4), **dashed_line))
    g.add(Line((5+5, 19), (5+5+320, 19), **dashed_line))

    dovetail_left = Group()
    dovetail_left.add(dovetail_diagonals(dovetail, **dashed_line))
    dovetail_left.add(Line((0, dovetail.w), (dovetail.l, dovetail.w), **dashed_line))
    dovetail_left.add(Line((0, 0), (dovetail.l, 0), **dashed_line))
    dovetail_left.rotate(90)
    dovetail_left.translate(0, -20)
    g.add(dovetail_left)

    dovetail_right = Group()
    dovetail_right.add(dovetail_diagonals(dovetail, **dashed_line))
    dovetail_right.add(Line((0, dovetail.w), (dovetail.l, dovetail.w), **dashed_line))
    dovetail_right.add(Line((0, 0), (dovetail.l, 0), **dashed_line))
    dovetail_right.rotate(-90)
    dovetail_right.translate(-dovetail.l, 330-dovetail.w)
    g.add(dovetail_right)

    g.add(Rect(*R(x1=5, y1=0, w=330, h=100), **dashed_line))
    g.add(Rect(*R(x1=0, y1=0, w=340, h=120), **solid_line))
    return g


def dt():
    g = Group()
    g.add(dovetail_tail_face(dovetail, **dashed_line))
    g.add(dovetail_pin_end(dovetail, **solid_line))
    g.add(dovetail_tail_face_helpers(dovetail, angle=math.pi/10, **helper_line))
    return g


def formaterv():
    g = Group()
    cab_front = cabinet_front(left_dashed=True)
    #cab_front.add(dimension((0, 0), (340, 0), 3, -10, **dimension_line))
    cab_front.add(dimension((335, 0), (0, 275), 3, -30, **dimension_line))
    cab_front.add(dimension((5, 255+16), (330, 0), 3, 42, **dimension_line))
    cab_front.translate(150,0)
    g.add(cab_front)

    cab_side = cabinet_side()
    #cab_side.add(dimension((0, 0), (120, 0), 3, -10, **dimension_line))
    cab_side.add(dimension((20, 255+16), (100, 0), 3, **dimension_line))
    g.add(cab_side)

    door_s = door_side()
    door_s.add(dimension((0, 255), (18, 0), 3, **dimension_line))
    door_s.translate(1, 16)
    g.add(door_s)

    door_f = door_front()
    door_f.translate(150 + 5 + 2, 16)
    door_f.add(dimension((0, 255), (162, 0), 3, **dimension_line))
    g.add(door_f)

    cab_top = cabinet_top()
    cab_top.add(dimension((0, 0), (0, 120), 3, **dimension_line))
    cab_top.add(dimension((0, 120), (340, 0), 3, **dimension_line))
    cab_top.translate(150, 340)
    g.add(cab_top)

    door_t1 = door_left_top(full_dashed=True)
    door_t1.translate(150 + 5 + 2, 300+100+1)
    g.add(door_t1)

    door_t2 = door_left_top(full_dashed=True)
    door_t2.translate(150 + 5 + 2 + 2 + 162 + 162, 300+100+1)
    door_t2.scale(-1,1)
    g.add(door_t2)

    g.scale(0.25, 0.25)

    return g


outdir = '/d/tmp/a'
dwg = svgwrite.Drawing('%s/sheet.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(svg.sheet.sheet())
dwg.save()
#p = Path(**dashed_line)
#p.push('M 100 100')
#p.push('100 200 200 200')

dwg = svgwrite.Drawing('%s/door_front.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(door_front())
dwg.save()

dwg = svgwrite.Drawing('%s/door_side.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(door_side())
dwg.save()

dwg = svgwrite.Drawing('%s/door_left_top.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(door_left_top())
dwg.save()

dwg = svgwrite.Drawing('%s/cabinet_front.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(cabinet_front())
dwg.save()

dwg = svgwrite.Drawing('%s/cabinet_side.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(cabinet_side())
dwg.save()

dwg = svgwrite.Drawing('%s/cabinet_bottom.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(cabinet_bottom())
dwg.save()

dwg = svgwrite.Drawing('%s/cabinet_top.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(cabinet_top())
dwg.save()

dwg = svgwrite.Drawing('%s/formaterv.svg' % outdir, profile='tiny', size=('594mm', '840mm'), viewBox='-100 -100 584 840')
dwg.add(formaterv())
dwg.save()

# dwg = svgwrite.Drawing('%s/test.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
# dwg.add(dimension((50, 100), (0, -55), **solid_line))
# dwg.add(dimension((50, 100), (30, -55), **solid_line))
# dwg.add(dimension((50, 100), (55, -55), **solid_line))
# dwg.add(dimension((50, 100), (55, -25), **solid_line))
#
# dwg.add(dimension((50, 100), (50, 0), **solid_line))
# dwg.add(dimension((50, 100), (50, 20), **solid_line))
# dwg.add(dimension((50, 100), (50, 50), **solid_line))
# dwg.add(dimension((50, 100), (25, 50), **solid_line))
#
# dwg.add(dimension((50, 100), (0, 45), **solid_line))
# dwg.add(dimension((50, 100), (-20, 45), **solid_line))
# dwg.add(dimension((50, 100), (-45, 45), **solid_line))
# dwg.add(dimension((50, 100), (-45, 22.5), **solid_line))
#
# dwg.add(dimension((50, 100), (-40, 0), **solid_line))
# dwg.add(dimension((50, 100), (-40, -15), **solid_line))
# dwg.add(dimension((50, 100), (-40, -40), **solid_line))
# dwg.add(dimension((50, 100), (-20, -40), **solid_line))
#
# dwg.add(Line((120, 100), (160, 80), **dashed_line))
# dwg.add(dimension((120, 100), (40, -20), 1, **solid_line))
#
# dwg.save()

