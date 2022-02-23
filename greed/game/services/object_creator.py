import random as r
from game.objects.rock import Rock
from game.objects.jewel import Jewel

BAG_RADIUS = 12.5
BAG_SCALE = 0.05

JEWEL_RADIUS = 15
JEWEL_SCALE = 0.5

ROCK_RADIUS = 16
ROCK_SCALE = 0.6

LOW_SPEED = -2
MAX_SPEED = -7

SCORE_JEWEL = 2
SCORE_ROCK = -10

JEWEL_LIST = [
    "greed/game/images/blue.png",
    "greed/game/images/yellow.png",
    "greed/game/images/red.png",
]
BAG_IMG = "greed/game/images/bag.png"
ROCK_IMG = "greed/game/images/rock.png"


class ObjectCreator:
    """
    Creates most of the ojbects in the game, rocks and jewels.

    Attributes:
        _width (class): screen width
        _height(int): screen height
        _the_objects (list): list of objects
    """

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._the_objects = []

    def create_object(self):
        """
        Creates a new actor of a random type and adds it to the list.
        :return:
        """
        number = r.randint(1, 50)
        if number < 25:
            item = Rock(
                ROCK_IMG,
                ROCK_SCALE,
                ROCK_RADIUS,
                self._width,
                self._height,
                MAX_SPEED,
                LOW_SPEED,
                SCORE_ROCK,
            )
        elif 50 > number > 25:
            item = Jewel(
                JEWEL_LIST[r.randint(0, 1)],
                JEWEL_RADIUS,
                JEWEL_SCALE,
                self._height,
                self._width,
                LOW_SPEED,
                MAX_SPEED,
                SCORE_JEWEL,
            )
        else:
            item = Jewel(
                JEWEL_LIST[2],
                JEWEL_RADIUS,
                JEWEL_SCALE,
                self._height,
                self._width,
                LOW_SPEED,
                MAX_SPEED,
                SCORE_JEWEL,
            )

        self._the_objects.append(item)

    def cleanup_zombies(self):
        """
        Removes objects that collide with the bag
        :return:
        """
        for item in self._the_objects:
            if not item.alive:
                self._the_objects.remove(item)

    def check_off_screen(self):
        """
        Checks to see if objects have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for item in self._the_objects:
            if item.is_off_screen(self._width, self._height):
                self._the_objects.remove(item)
