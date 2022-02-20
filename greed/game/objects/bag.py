from game.objects.object import Object


class Bag(Object):
    """Player controlled object

    This is responsible for keeping track of the bags point.

    Attributes:
        center._x (int): x axis point
        center._y (int): y axis point
        scale (int): scale of the image from it's original file
        radius (int): radius around the object
    """

    def __init__(self, img, width, radius, scale):
        """Updates the message to the given one.

        Args:
            message (string): The given message.
        """
        super().__init__(img)
        self._center._x = width / 2
        self._center._y = radius * 2
        self._scale = scale
        self._radius = radius

    def move_right(self, width, move):
        """Moves bag right

        Args:

        """
        if self._center._x < width - self._radius * 2:
            self._center._x += move

    def move_left(self, move):
        """Moves bag left

        Args:

        """
        if self._center._x > self._radius * 2:
            self._center._x -= move
