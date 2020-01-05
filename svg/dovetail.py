from svgwrite.container import Group
from svgwrite.shapes import Polyline, Line
import math


def dovetail_diagonals(d, **kwargs):
    g = Group()
    for i, o in zip(d.tail_inner(), d.tail_outer()):
        g.add(Line((i[1], 0), (o[1], d.w), **kwargs))
        g.add(Line((o[0], d.w), (i[0], 0), **kwargs))
    return g


def dovetail_tail_face(d, **kwargs):
    g = Group()
    for i, o in zip(d.tail_inner(), d.tail_outer()):
        g.add(Polyline([(i[0], 0), (i[1], 0), (o[1], d.w), (o[0], d.w), (i[0], 0)], **kwargs))
    return g


def dovetail_pin_end(d, **kwargs):
    g = Group()
    for i, o in zip(d.pin_inner(), d.pin_outer()):
        g.add(Polyline([(i[0], 0), (i[1], 0), (o[1], d.w), (o[0], d.w), (i[0], 0)], **kwargs))
    return g


def dovetail_tail_end(d, bw, visible, invisible):
    g = Group()
    for o in list(sum(d.tail_inner(), ())):
        g.add(Line((o,0), (o, bw), **invisible))
    for i in list(sum(d.tail_outer(), ())):
        g.add(Line((i,0), (i, bw), **visible))
    return g


def dovetail_tail_face_helpers(d, angle=math.pi/6, **kwargs):
    g = Group()
    g.add(Line((0, d.w/2.0), (d.l, d.w/2.0), **kwargs))
    n = 3*d.t + 1
    for i in range(1, n + 1):
        l = d.l * i / n
        g.add(Line((l, d.w/2.0), (l*math.cos(angle), d.w/2.0+l*math.sin(angle)), **kwargs))
    g.add(Line((0, d.w / 2.0), (d.l * math.cos(angle), d.w / 2.0 + d.l * math.sin(angle)), **kwargs))
    for i in range(4,7):
        g.add(Line((i*d.a, d.w/2), (5*d.a, -6*d.a-d.w/2.0), **kwargs))
    return g
