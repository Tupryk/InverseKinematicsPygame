import numpy as np
from segment import Segment

class Arm():
    def __init__(self, seg_count=7, seg_len=50, base=np.array([0, 0])):
        self.segs = []
        self.seg_count = seg_count
        for i in range(seg_count):
            width = i+1
            seg = Segment(300, 200, seg_len, 0, width=width)
            self.segs.append(seg)

        self.base = base

    def update(self, follows):
        self.segs[0].follow(follows)
        self.segs[0].update()

        for i in range(1, self.seg_count):
            self.segs[i].follow(self.segs[i-1].a)
            self.segs[i].update()

        self.segs[-1].set_a(self.base)

        for i in range(self.seg_count-2, -1, -1):
            self.segs[i].set_a(self.segs[i+1].b)

    def draw(self, screen):
        for seg in self.segs:
            seg.draw(screen)
