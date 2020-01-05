def corners(insert, size):
    return ((insert[0], insert[1]),
            (insert[0], insert[1]+size[1]),
            (insert[0]+size[0], insert[1]),
            (insert[0]+size[0], insert[1]+size[1]),
            )


def R(*, x1=None, x2=None, y1=None, y2=None, w=None, h=None):
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

    return (x1, y1), (w, h)
