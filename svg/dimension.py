from svgwrite.text import Text
from svgwrite.container import Group
from svgwrite.shapes import Line

import math


def dimension(insert, size, font_size=0.8, offset=None, leg_difference=0, **kwargs):
    offset = offset if offset is not None else font_size * 7
    x, y = insert[0], insert[1] + offset
    width, height = size
    l = math.sqrt(width ** 2 + height ** 2)
    angle = 90*height/abs(height) if width == 0 \
        else math.degrees(math.atan(height/width))
    if width < 0:
        angle = 180 + angle
    e = 1
    endtick = lambda i: ((i[0]-e, i[1]+e), (i[0]+e, i[1]-e))
    g = Group()
    left_leg_shorter, right_leg_shorter = (leg_difference, 0) if leg_difference > 0 else (0, -leg_difference)
    g.add(Line((insert[0], insert[1] + left_leg_shorter), (x, y), **kwargs))
    g.add(Line((x + l, insert[1] + right_leg_shorter), (x + l, y), **kwargs))
    g.add(Line(*endtick((x, y)), **kwargs))
    g.add(Line(*endtick((x + l, y)), **kwargs))
    g.add(Line((x, y), (x + l, y), **kwargs))

    text_group = Group()
    text = int(l) if l.is_integer() else f'{l:.1f}'
    text_group.add(Text(text, (x + l / 2.0, y - e), text_anchor="middle", alignment_baseline="after-edge",
                        style="font-style:normal;"
                              "font-variant:normal;"
                              "font-weight:normal;"
                              "font-stretch:normal;"
                              f"font-size:{font_size}mm;"
                              "line-height:1.25;"
                              "font-family:Bariol;"
                              "-inkscape-font-specification:Bariol;"
                              "letter-spacing:0px;"
                              "word-spacing:0px;"
                              "fill:#000000;"
                              "fill-opacity:1;"
                              "stroke:none;"
                              "stroke-width:0.26012909"))
    if 45 < angle <= 225:
        text_group.rotate(180, (x+l/2, y))
    g.add(text_group)
    g.rotate(angle, center=insert)
    return g
