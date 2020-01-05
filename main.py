from dovetail import DoveTail

from svg.dovetail import dovetail_tail_end, dovetail_pin_end, dovetail_tail_face, dovetail_tail_face_helpers, dovetail_diagonals
import svg.chamfered
import svg.domino
from svg.util import R

import svgwrite
from svgwrite.path import Path
from svgwrite.shapes import Rect, Line, Circle
from svgwrite.container import Group
from svgwrite.text import Text

import math

dashed_line = {'style': 'stroke:#000000;stroke-opacity:1;fill:none;stroke-width:0.4;stroke-dasharray:1.0,1.0'}
solid_line = {'style': 'stroke:#000000;stroke-opacity:1;fill:none;stroke-width:0.4'}
helper_line = {'style': 'stroke:#606060;stroke-opacity:1;fill:none;stroke-width:0.25'}

dovetail = DoveTail(10, 100, 3)


def door_front():
    w = 162
    h = 260
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


def door_left_top():
    w = 162
    c = 2
    g = Group()
    g.add(Path(f'M0 0 l40 0 l0 6.5 l-10 0 l0 5 l10 0 l0 {6.5-c} l{-c} {c} l{2*c-40} 0 l{-c} {-c} Z', **solid_line))
    g.add(Path(f'M{w} 0 l-40 0 l0 6.5 l10 0 l0 5 l-10 0 l0 {6.5-c} l{c} {c} l{40-2*c} 0 l{c} {-c} Z', **solid_line))
    g.add(Path(f'M40 0 l{w-2*40} 0 l0 6.5 l9 0 l0 5 l-9 0 l0 {6.5-c} l{-c} {c} l{-w+2*40+2*c} 0 l{-c} {-c} l0 {-6.5+c} '
               f'l-9 0 l0 -5 l9 0 Z', **solid_line))
    g.add(Rect((31, 7), (100, 4), **dashed_line))
    #g.add(Rect((0, 7), (30, 4), **dashed_line)
    #g.add(Rect((h-30, 7), (30, 4), **dashed_line))
    #g.add(Rect((0, 6.5), (h, 5), **dashed_line))
    g.add(Rect((4, 0), (26, 13), **dashed_line))
    #g.add(Rect((18-13, h-53-13), (13, 26), **dashed_line))
    #g.add(Path(f'M2 0 L18 0 L18 {h} L2 {h} L0 {h-2} L0 2 Z', **solid_line))
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


def dimension(insert, size, **kwargs):
    l = math.sqrt(size[0] ** 2 + size[1] ** 2)
    e = 1
    endtick = lambda i: ((i[0]-e, i[1]+e), (i[0]+e, i[1]-e))
    g = Group()
    g.add(Line(*endtick(insert), **kwargs))
    g.add(Line(*endtick(((insert[0] + size[0]), (insert[1] + size[1]))), **kwargs))
    g.add(Line(insert, (insert[0] + size[0], insert[1] + size[1]), **kwargs))
    g.add(Text(f"{int(l) if l.is_integer() else l}", (insert[0] + l/2.0, insert[1]-e), text_anchor="middle", alignment_baseline="after-edge",
          style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:2.77471018px;line-height:1.25;font-family:Bariol;-inkscape-font-specification:Bariol;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.26012909"))
    g.rotate(-90, center=insert)
    return g


outdir = '/d/tmp/a'
dwg = svgwrite.Drawing('%s/test.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
#dwg.add(sheet())
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
top = cabinet_top()
top.scale(0.2, 0.2)
dwg.add(top)
dwg.save()

dwg = svgwrite.Drawing('%s/test.svg' % outdir, profile='tiny', size=('420mm', '594mm'), viewBox='-10 -10 410 584')
dwg.add(dimension((50, 100), (100, 0), **solid_line))
dwg.save()

