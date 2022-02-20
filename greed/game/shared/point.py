class Point:
    """
    This class keeps track for where the paddle and ball are on screen.
    """

    def __init__(self):
        self._x = 0
        self._y = 0


class Velocity:
    """
    This class sets how fast the ball is moving on screen.
    """

    def __init__(self):
        self._dx = 0
        self._dy = 0
