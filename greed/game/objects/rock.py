from game.objects.object import Object
import random as r


class Rock(Object):
    """Rocks

    This is the model to create all the rocks in the game

    Attributes:
        center._x (int): x axis point
        center._y (int): y axis point
        scale (int): scale of the image from it's original file
        radius (int): radius around the object
        velocity (int): how fast the object will move
    """

    def __init__(self, img, scale, radius, width, height, max, low):
        super().__init__(img)
        self._radius = radius
        self._scale = scale
        self._center._x = r.randint(self._radius * 2, width - self._radius * 2)
        self._center._y = height - self._radius * 2
        self._velocity._dy = r.randint(max, low)

    def hit(self):
        """Used to subtrace points from the user

        Returns:
           Point value
        """
        return -10
