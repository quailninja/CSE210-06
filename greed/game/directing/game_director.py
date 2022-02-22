from asyncio.windows_events import NULL
from tarfile import NUL
import arcade
import random as r

from game.objects.bag import Bag
from game.objects.rock import Rock
from game.objects.jewel import Jewel
from game.screens.pause_screen import PauseView
from game.services.keyboard_service import KeyboardService

BAG_RADIUS = 12.5
BAG_SCALE = 0.05

JEWEL_RADIUS = 15
JEWEL_SCALE = 0.5

ROCK_RADIUS = 16
ROCK_SCALE = 0.6

MOVE_AMOUNT = 5
LOW_SPEED = -2
MAX_SPEED = -7

SCORE_JEWEL = 2
SCORE_ROCK = 10

JEWEL_LIST = [
    "greed/game/images/red.png",
    "greed/game/images/blue.png",
    "greed/game/images/yellow.png",
]
BAG_IMG = "greed/game/images/bag.png"
ROCK_IMG = "greed/game/images/rock.png"
BACKGROUND_IMG = "greed/game/images/mountain_back.png"


class GameDirector(arcade.View):
    """Game director

    This is the main game screen, it keeps track of:
    -Player keyboard input
    -Score
    -Removing and creating objects

    Attributes:
        bag (class): player object
        flying_actors (list): all the rocks and jewels are put into this list
        score (int): the players score
    """

    def __init__(self, i_view):
        """
        Sets up the initial conditions of the game

        """
        super().__init__()
        self.bag = Bag(BAG_IMG, self.window.width, BAG_RADIUS, BAG_SCALE)
        self.flying_actors = []
        self.score = 0
        self._i_view = i_view
        self._key = NUL
        self._keyboard_services = KeyboardService(self.bag, MOVE_AMOUNT)
        self._background = arcade.load_texture(BACKGROUND_IMG)

    def on_show(self):
        """
        Used to set the initial screen

        """

        arcade.set_background_color(arcade.color.WHITE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        self.clear()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self._background
        )
        # draw each object
        self.bag.draw()

        for item in self.flying_actors:
            item.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = self.window.height - 20
        arcade.draw_text(
            score_text,
            start_x=start_x,
            start_y=start_y,
            font_size=12,
            color=arcade.color.NAVY_BLUE,
        )

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        pause = PauseView(self, self._i_view)
        self._keyboard_services.check_keys(self._key, pause, 0)
        self.check_off_screen()
        self.check_collisions()
        if self._key == 65307:
            self._key = NUL
        if r.randint(1, 25) == 1:
            self.create_object()

        for item in self.flying_actors:
            item.advance()

    def check_collisions(self):
        """
        Checks to see if actors have the bag.
        Updates scores and removes dead items.
        :return:
        """
        for item in self.flying_actors:

            too_close = item._radius + self.bag._radius

            if (
                abs(item._center._x - self.bag._center._x) < too_close
                and abs(item._center._y - self.bag._center._y) < too_close
            ):
                item.alive = False
                self.score += item.hit()

        self.cleanup_zombies()

    def create_object(self):
        """
        Creates a new actor of a random type and adds it to the list.
        :return:
        """
        if r.randint(1, 3) == 1:
            item = Rock(
                ROCK_IMG,
                ROCK_SCALE,
                ROCK_RADIUS,
                self.window.width,
                self.window.height,
                MAX_SPEED,
                LOW_SPEED,
            )
        else:
            item = Jewel(
                JEWEL_LIST,
                JEWEL_RADIUS,
                JEWEL_SCALE,
                self.window.height,
                self.window.width,
                LOW_SPEED,
                MAX_SPEED,
            )

        self.flying_actors.append(item)

    def check_off_screen(self):
        """
        Checks to see if objects have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for item in self.flying_actors:
            if item.is_off_screen(self.window.width, self.window.height):
                self.flying_actors.remove(item)

    def cleanup_zombies(self):
        """
        Removes objects that collide with the bag
        :return:
        """
        for item in self.flying_actors:
            if not item.alive:
                self.flying_actors.remove(item)

    def on_key_press(self, key, key_modifiers):
        self._key = key

    def on_key_release(self, key, key_modifiers):
        self._key = NUL
