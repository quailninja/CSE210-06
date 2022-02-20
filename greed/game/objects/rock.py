from game.objects.object import Object
import random as r


class Rock(Object):
    def __init__(self, img, scale, radius, width, height, max, low):
        super().__init__(img)
        self._radius = radius
        self._scale = scale
        self._center._x = r.randint(self._radius * 2, width - self._radius * 2)
        self._center._y = height - self._radius * 2
        self._velocity._dy = r.randint(max, low)

    def hit(self):
        return -10
