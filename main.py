from dovetail import DoveTail

from svg.dovetail import dovetail_tail_end, dovetail_pin_end, dovetail_tail_face, dovetail_tail_face_helpers, dovetail_diagonals
import svg.chamfered
import svg.domino
import svg.sheet
from svg.dimension import dimension as dimension
from svg.util import R
import svg.lines as LineStyles

import svgwrite
from svgwrite.path import Path
from svgwrite.shapes import Rect, Line, Circle, Ellipse
from svgwrite.container import Group

dashed_line = {}
invisible_line = {}
solid_line = {}
dimension_line = {}
helper_line = {}
segment_line = {}

import math

dovetail = DoveTail(10, 100, 3)


def reset_linestyles():
    global dashed_line
    global invisible_line
    global solid_line
    global dimension_line
    global helper_line
    global segment_line

    dashed_line = LineStyles.dashed_line
    invisible_line = LineStyles.invisible_line
    solid_line = LineStyles.solid_line
    dimension_line = LineStyles.dimension_line
    helper_line = LineStyles.helper_line
    segment_line = LineStyles.segment_line

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


def cabinet_front(left_dashed=False):
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


def cabinet_top(left_in_view=False):
    invisible_or_dashed = invisible_line if left_in_view else dashed_line
    g = Group()

    #back hangers
    g.add(halved_line((5+5, 4), (5+5+320, 4), invisible_or_dashed, dashed_line))
    g.add(halved_line((5+5, 19), (5+5+320, 19), invisible_or_dashed, dashed_line))

    dovetail_left = Group()
    dovetail_left.add(dovetail_diagonals(dovetail, **dashed_line))
    dovetail_left.add(Line((0, dovetail.w), (dovetail.l, dovetail.w), **dashed_line))
    dovetail_left.add(Line((0, 0), (dovetail.l, 0), **dashed_line))
    dovetail_left.rotate(90)
    dovetail_left.translate(0, -20)
    if not left_in_view:
        g.add(dovetail_left)
        g.add(svg.domino.side(11, 120-40-21, **dashed_line))
        g.add(svg.domino.side(11, 120-75-21, **dashed_line))

    dovetail_right = Group()
    dovetail_right.add(dovetail_diagonals(dovetail, **dashed_line))
    dovetail_right.add(Line((0, dovetail.w), (dovetail.l, dovetail.w), **dashed_line))
    dovetail_right.add(Line((0, 0), (dovetail.l, 0), **dashed_line))
    dovetail_right.rotate(-90)
    dovetail_right.translate(-dovetail.l, 330-dovetail.w)
    g.add(dovetail_right)

    g.add(svg.domino.side(340-20+6, 120-40-21, **dashed_line))
    g.add(svg.domino.side(340-20+6, 120-75-21, **dashed_line))

    # g.add(Rect(*R(x1=5, y1=0, w=330, h=100), **dashed_line))
    g.add(Line((5, 0), (5, 100), **invisible_or_dashed))
    g.add(halved_line((5, 100), (335, 100), invisible_or_dashed, dashed_line))
    g.add(Line((335, 0), (335, 100), **dashed_line))
    g.add(Rect(*R(x1=0, y1=0, w=340, h=120), **solid_line))
    return g


def dt():
    g = Group()
    g.add(dovetail_tail_face(dovetail, **dashed_line))
    g.add(dovetail_pin_end(dovetail, **solid_line))
    g.add(dovetail_tail_face_helpers(dovetail, angle=math.pi/10, **helper_line))
    return g


def formaterv():
    reset_linestyles()
    global dashed_line
    dashed_line = LineStyles.invisible_line
    g = Group()
    cab_front = cabinet_front(left_dashed=True)
    cab_front.add(dimension((335, 0), (0, 275), 3, -30, **dimension_line))
    cab_front.add(dimension((5, 255+16), (330, 0), 3, 42, **dimension_line))
    cab_front.translate(200,0)
    g.add(cab_front)

    cab_side = cabinet_side()
    cab_side.add(dimension((20, 255+16), (100, 0), 3, **dimension_line))
    g.add(cab_side)

    door_s = door_side()
    door_s.add(dimension((0, 255), (18, 0), 3, **dimension_line))
    door_s.translate(1, 16)
    g.add(door_s)

    door_f = door_front()
    door_f.translate(200 + 5 + 2, 16)
    door_f.add(dimension((0, 255), (162, 0), 3, **dimension_line))
    g.add(door_f)

    cab_top = cabinet_top()
    cab_top.add(dimension((0, 0), (0, 120), 3, **dimension_line))
    cab_top.add(dimension((0, 120), (340, 0), 3, **dimension_line))
    cab_top.translate(200, 340)
    g.add(cab_top)

    door_t1 = door_left_top(full_dashed=True)
    door_t1.translate(200 + 5 + 2, 340+100+1)
    g.add(door_t1)

    door_t2 = door_left_top(full_dashed=True)
    door_t2.translate(200 + 5 + 2 + 2 + 162 + 162, 340+100+1)
    door_t2.scale(-1,1)
    g.add(door_t2)

    g.scale(0.25, 0.25)

    return g


def dash_it(insert, size, d, **extra):
    x, y = insert
    width, height = size
    g = Group()
    for i in range(d, width + height, d):
        line_start = (x + i, y) if i <= width else (x + width, y + i - width)
        line_end = (x + i - height, y + height) if i >= height else (x, y + i)
        g.add(Line(line_start, line_end, **extra))
    return g


def end_grain_mark(insert, size, **extra):
    x, y = insert
    width, height = size
    g = Group()
    rx = 2 * width
    ry = height * 3
    g.add(Path(f'M{x} {y+1*height/3} a {rx} {ry} 0 0 0 {width} 0', **extra))
    g.add(Path(f'M{x} {y+2*height/3} a {rx} {ry} 0 0 0 {width} 0', **extra))

    center_x = width / 2
    center_y = (rx**2 - width**2 / 4.0)**(1.0/2.0)
    for i in range(0,8):
        l1x = i * width / 7
        l1y = 7*height/8
        m = (center_y + l1y) / (center_x - l1x)
        g.add(Line((x+l1x, y+l1y), (x+l1x+height/2/m, y+height/4), **extra))
    return g


def rotate_group(g, *args, **kwargs):
    g.rotate(*args, **kwargs)
    return g


def jellegrajz():
    reset_linestyles()
    g = Group()
    cab_front = cabinet_front(left_dashed=True)
    cab_front.add(Line((170, -10), (170, 285), **segment_line))
    cab_front.add(dash_it((170, 0), (170, 15), 8, **helper_line))
    cab_front.add(dash_it((320, 15), (15, 260), 8, **helper_line))
    cab_front.add(dash_it((170, 260), (150, 15), 8, **helper_line))
    cab_front.add(Circle((340-20+7.5, 30), 40, **dashed_line))
    cab_front.add(Circle((340-20+7.5, 137.5 + 20), 40, **dashed_line))
    cab_front.translate(200, 0)
    g.add(cab_front)

    cab_side = cabinet_side()
    cab_side.add(end_grain_mark((2, 0), (26, 15), **helper_line))
    cab_side.add(Line((30, 0), (30, 15), **helper_line))
    cab_side.add(rotate_group(end_grain_mark((32, 0), (26, 15), **helper_line), 180, (32+26/2, 7.5)))
    cab_side.add(Line((60, 0), (60, 15), **helper_line))
    cab_side.add(end_grain_mark((62, 0), (26, 15), **helper_line))
    cab_side.add(Line((90, 0), (90, 15), **helper_line))
    cab_side.add(rotate_group(end_grain_mark((92, 0), (22, 15), **helper_line), 180, (92+22/2, 7.5)))

    cab_side.add(end_grain_mark((22, 260), (29, 15), **helper_line))
    cab_side.add(Line((22+29+2, 260), (22+29+2, 275), **helper_line))
    cab_side.add(rotate_group(end_grain_mark((22+29+4, 260), (29, 15), **helper_line), 180, (22+29+4+29/2, 267.5)))
    cab_side.add(Line((22+2*(29+2)+2, 260), (22+2*(29+2)+2, 275), **helper_line))
    cab_side.add(end_grain_mark((22+2*(29+2)+4, 260), (25, 15), **helper_line))

    cab_side.add(rotate_group(end_grain_mark((120-4-7.5-20, 15+20-7.5), (40, 15), **helper_line), 90, (120-4-7.5, 15+20)))
    cab_side.add(rotate_group(end_grain_mark((120-4-7.5-20, 137.5+20-7.5), (40, 15), **helper_line), 90, (120-4-7.5, 137.5+20)))

    cab_side.add(Line((117.5, 5), (117.5, 270), **helper_line))
    cab_side.add(Line((118.5, 5), (118.5, 270), **helper_line))

    cab_side.add(Ellipse((60, 27), (80, 50), **dashed_line))
    g.add(cab_side)

    door_s = door_side()
    door_s.translate(1, 16)
    g.add(door_s)

    door_f = door_front()
    door_f.add(Circle((25, 230), 45, **dashed_line))
    door_f.translate(200 + 5 + 2, 16)
    g.add(door_f)

    cab_top = cabinet_top(left_in_view=True)
    cab_top.add(Line((340/2, -10), (340/2, 130), **segment_line))
    cab_top.add(Path(f'M-10 125 l180 0 l0 -30 l180 0', **segment_line))
    cab_top.translate(200, 340)
    g.add(cab_top)

    # door_t1 = door_left_top(full_dashed=True)
    # door_t1.translate(200 + 5 + 2, 340+100+1)
    # g.add(door_t1)

    door_t2 = door_left_top(full_dashed=True)
    door_t2.add(end_grain_mark((2, -1), (28, 18), **helper_line))
    door_t2.add(end_grain_mark((132, -1), (28, 18), **helper_line))
    door_t2.add(Circle((16, 7.5), 30, **dashed_line))
    door_t2.translate(200 + 5 + 2 + 2 + 162 + 162, 340+100+1)
    door_t2.scale(-1,1)
    g.add(door_t2)

    g.scale(0.25, 0.25)

    return g

outdir = '/d/tmp/a'
reset_linestyles()
dwg = svgwrite.Drawing('%s/sheet.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
mm15 = 'l4 0 l2 -1.4 l2 2.8 l2 -1.4 l4 0'
dwg.add(Path('M20 20 ' + mm15, **solid_line))
dwg.add(Path('M20 30 ' + mm15, **dashed_line))

mm18 = 'l6 0 l2 -1.4 l2 2.8 l2 -1.4 l6 0'
dwg.add(Path('M40 20 ' + mm18, **solid_line))
dwg.add(Path('M40 30 ' + mm18, **dashed_line))

mm40 = 'l7 0 l2 -1.4 l2 2.8 l2 -1.4 l14 0 l2 -1.4 l2 2.8 l3 -1.4 l7 0'
dwg.add(Path('M60 20 ' + mm40, **solid_line))
dwg.add(Path('M60 30 ' + mm40, **dashed_line))

dwg.add(svg.sheet.sheet())
dwg.save()
# #p = Path(**dashed_line)
# #p.push('M 100 100')
# #p.push('100 200 200 200')
#

if False:
    dwg = svgwrite.Drawing('%s/door_front.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
    dwg.add(door_front())
    dwg.add(dimension((0, 258), (30, 0), **dimension_line))
    dwg.add(dimension((30, 258), (10, 0), **dimension_line))
    dwg.add(dimension((30, 258-30), (0, 30), **dimension_line))
    dwg.add(dimension((17, 258), (0, -55), offset=0, **dimension_line))
    dwg.add(dimension((17, 258), (0, -55), offset=0, **dimension_line))
    dwg.add(dimension((0, 258-55), (17, 0), offset=0, **dimension_line))
    dwg.add(dimension((31, 258-55), (100, 0), offset=0, **dimension_line))
    dwg.add(dimension((31, 258-20+0.7*8), (162-2*31, 0), offset = 0, **dimension_line))
    dwg.add(dimension((40, 258-20), (162-2*40, 0), offset = 0, **dimension_line))
    dwg.save()

if False:
    dwg = svgwrite.Drawing('%s/door_side.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
    dwg.add(dimension((0, 80), (6.5, 0), offset=0, **dimension_line))
    dwg.add(dimension((6.5, 80), (5, 0), offset=0, **dimension_line))
    dwg.add(dimension((11.5, 80), (6.5, 0), offset=0, **dimension_line))
    dwg.add(dimension((18, 55), (-13, 0), offset=0, **dimension_line))
    dwg.add(dimension((7, 15), (4, 0), offset=0, **dimension_line))
    dwg.add(door_side())
    dwg.save()

# dwg = svgwrite.Drawing('%s/door_left_top.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
# dwg.add(door_left_top())
# dwg.save()
#
dwg = svgwrite.Drawing('%s/cabinet_front.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(cabinet_front(left_dashed=True))

# 1. csomópont
dwg.add(dimension((320, 0), (0, 15), **dimension_line))
dwg.add(dimension((320, 70), (15, 0), **dimension_line))
dwg.add(dimension((320, 55), (10, 0), **dimension_line))
dwg.add(dimension((320, 55), (0, -2), offset=24.5, leg_difference=10, **dimension_line))
dwg.add(dimension((320, 15), (0, 40), 0.8, 10, **dimension_line))
dwg.add(dimension((335, 15), (5, 0), **dimension_line))
dwg.add(dimension((320, 15), (4.5, 0), **dimension_line))
dwg.add(dimension((335-4.5, 15), (4.5, 0), **dimension_line))
dwg.add(dimension((340-5-4.5, 5+37), (0, -37), 0.8, 14, **dimension_line))

# 2. csomópont
dwg.add(dimension((320, 120), (15, 0), **dimension_line))
dwg.add(dimension((320, 137.5), (0, 40), 0.8, 10, **dimension_line))
dwg.add(dimension((320, 137.5+2), (0, -2), offset=20, leg_difference=-10, **dimension_line))
dwg.add(dimension((320, 137.5+40), (0, -2), offset=20, leg_difference=10, **dimension_line))
dwg.add(dimension((320, 137.5+40), (10, 0), **dimension_line))
dwg.save()

reset_linestyles()
dwg = svgwrite.Drawing('%s/cabinet_side.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-20 -20 410 584')
dwg.add(cabinet_side())
dwg.add(dimension((120, 0), (-120, 0), **dimension_line))
dwg.add(dimension((0, 15), (0, -15), **dimension_line))
dwg.add(dimension((120-4, 62), (4, 0), offset=0, **dimension_line))
dwg.add(dimension((20, 70), (100, 0), offset=0, **dimension_line))

# dominos
dwg.add(dimension((20, 25), (20, 0), offset=0, **dimension_line))
dwg.add(dimension((41, 25), (19, 0), offset=0, **dimension_line))
dwg.add(dimension((40, 42), (21, 0), **dimension_line))
dwg.add(dimension((20, 42), (75-20, 0), offset=12, **dimension_line))
dwg.add(dimension((40+21, 42), (0, -27), **dimension_line))
dwg.add(dimension((40+21, 42-27), (0, -10), **dimension_line))
dwg.add(dimension((40+21, 42-27-10), (0, -5), **dimension_line))
dwg.add(dimension((85, 41), (0, -35), offset=0, **dimension_line))

# hanger
dwg.add(dimension((120-19, 15+20), (19, 0), offset=0, **dimension_line))
dwg.add(dimension((120, 15+40), (0, -40), **dimension_line))
dwg.add(dimension((120, 15), (0, -10), **dimension_line))
dwg.add(dimension((120, 5), (0, -5), **dimension_line))
dwg.save()
#
dwg = svgwrite.Drawing('%s/cabinet_bottom.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-20 -20 410 584')
dwg.add(dimension((5, 100), (5, 0), **dimension_line))
dwg.add(dimension((10, 100), (10, 0), **dimension_line))
dwg.add(cabinet_bottom())
dwg.save()
#
# dwg = svgwrite.Drawing('%s/cabinet_top.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
# dwg.add(cabinet_top())
# dwg.save()

if False:
    dwg = svgwrite.Drawing('%s/formaterv.svg' % outdir, profile='tiny', size=('594mm', '840mm'), viewBox='-100 -100 584 840')
    dwg.add(formaterv())
    dwg.save()

if False:
    dwg = svgwrite.Drawing('%s/jellegrajz.svg' % outdir, profile='tiny', size=('594mm', '840mm'), viewBox='-100 -100 584 840')
    dwg.add(jellegrajz())
    dwg.save()
