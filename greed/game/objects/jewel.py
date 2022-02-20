from game.objects.object import Object
import random as r


class Jewel(Object):
    def __init__(self, j_list, radius, scale, height, width, low, max):
        super().__init__(r.choice(j_list))
        self._radius = radius
        self._center._x = r.randint(self._radius * 2, width - self._radius * 2)
        self._center._y = height - self._radius * 2
        self._scale = scale
        self._velocity._dy = r.randint(max, low)

    def hit(self):
        return 2
