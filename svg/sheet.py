from svgwrite.container import Group
from svgwrite.shapes import Rect
from svgwrite.text import Text


def sheet():
    l = {'style': 'stroke:#000000;stroke-opacity:1;fill:none;stroke-width:0.5'}
    g = Group()
    g.add(Rect((10, 10), (190, 277), **l))

    g.add(Rect((10, 297-15-10), (60, 7.5), **l))
    g.add(Rect((10, 297-15-10), (60, 15), **l))
    g.add(Rect((180, 297-15-10), (20, 7.5), **l))
    g.add(Rect((180, 297-15-10), (20, 15), **l))
    g.add(Rect((10, 297-15-10), (190, 15), **l))
    style = "font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:5px;line-height:1.25;font-family:Bariol;-inkscape-font-specification:Bariol;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.26012909"
    g.add(Text(f"Koszó Norbert", (15, 297-15-10+15/4.0), text_anchor="start", alignment_baseline="middle", style=style))
    g.add(Text(f"2020. január 06.", (15, 297-15-10+3*15/4.0), text_anchor="start", alignment_baseline="middle", style=style))
    g.add(Text(f"Valami megnevezés", (15 + 60, 297-15-10+2*15/4.0), text_anchor="start", alignment_baseline="middle", style=style))
    g.add(Text(f"1:5", (182, 297-15-10+1*15/4.0), text_anchor="start", alignment_baseline="middle", style=style))
    g.add(Text(f"2019/62", (182, 297-15-10+3*15/4.0), text_anchor="start", alignment_baseline="middle", style=style))

    return g

