from game.objects.object import Object


class Bag(Object):

    """
    This class generates the bag information that the player controls
    """

    def __init__(self, img, width, radius, scale):
        super().__init__(img)
        self._center._x = width / 2
        self._center._y = radius * 2
        self._scale = scale
        self._radius = radius

    def move_right(self, width, move):
        if self._center._x < width - self._radius * 2:
            self._center._x += move

    def move_left(self, move):
        if self._center._x > self._radius * 2:
            self._center._x -= move
