from game.objects.object import Object
import random as r


class Jewel(Object):
    """Jewels

    This is the model to help create all the jewels in the game

    Attributes:
        center._x (int): x axis point
        center._y (int): y axis point
        scale (int): scale of the image from it's original file
        radius (int): radius around the object
        velocity (int): how fast the object will move
    """

    def __init__(self, j_list, radius, scale, height, width, low, max):
        super().__init__(r.choice(j_list))
        self._radius = radius
        self._center._x = r.randint(self._radius * 2, width - self._radius * 2)
        self._center._y = height - self._radius * 2
        self._scale = scale
        self._velocity._dy = r.randint(max, low)

    def hit(self):
        """Used to give points to the user

        Returns:
           Point value
        """
        return 2
