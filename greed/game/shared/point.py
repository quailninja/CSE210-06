class Point:
    """Point

    This class is used to help keep track of where all objects are in the game.

    Attributes:
        _x (int): x axis point
        _y (int): y axis point
    """

    def __init__(self):
        self._x = 0
        self._y = 0


class Velocity:
    """Velocity

    This keeps track of how fast moving objects are going

    Attributes:
        dx (int): how fast an object moves on the x axis point
        dy (int): how fast an ojbect moves on the y axis point

    """

    def __init__(self):
        self._dx = 0
        self._dy = 0
