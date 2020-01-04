class DoveTail:

    def __init__(self, w, l, t=None):
        self.w = w
        self.l = l
        self.t = round(self.l / 1.5 * self.w) if t is None else t
        self.a = self.l/(3.0*self.t+1)
        self.o = self.w / 12.0

    def tail_inner(self):
        return (((x-1)*self.a + self.o, (x+1)*self.a - self.o) for x in range(2, 3 * self.t, 3))

    def tail_outer(self):
        return (((x-1)*self.a - self.o, (x+1)*self.a + self.o) for x in range(2, 3 * self.t, 3))

    def pin_inner(self):
        yield (0, self.a + self.o)
        for x in range(3, 3*self.t, 3):
            yield (x*self.a - self.o, (x+1)*self.a + self.o)
        yield (3*self.t*self.a - self.o, (3*self.t+1)*self.a)

    def pin_outer(self):
        yield (0, self.a - self.o)
        for x in range(3, 3*self.t, 3):
            yield (x*self.a + self.o, (x+1)*self.a - self.o)
        yield (3*self.t*self.a + self.o, (3*self.t+1)*self.a)
