import arcade
import game.shared.point as p


class Object:

    """
    This is the standard for all objects in the game.
    """

    def __init__(self, img):
        self._center = p.Point()
        self._velocity = p.Velocity()
        self.alive = True
        self._texture = arcade.load_texture(img)
        self._radius = 5
        self._scale = 1

    def advance(self):
        """
        All objects will use this to move on screen
        """
        self._center._x += self._velocity._dx
        self._center._y += self._velocity._dy

    def draw(self):
        """
        All objects will use this to render on screen
        """
        arcade.draw_scaled_texture_rectangle(
            self._center._x, self._center._y, self._texture, self._scale
        )

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        """
        Checks to see if objects are off screen
        """
        if (
            self._center._x > SCREEN_WIDTH
            or self._center._y > SCREEN_HEIGHT
            or self._center._y < 0
            or self._center._x < 0
        ):
            return True
