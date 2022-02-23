import arcade
import game.shared.point as p


class Object:
    """Object

    This is the baseline for all objects in the game

    Attributes:
        center (class): x axis point
        velocity (class): y axis point
        alive (bolean): true or false, helps remove objects during collision
        texture (string): image generated for objects
        scale (int): scale of the image from it's original file
        radius (int): radius around the object
    """

    def __init__(self, img, sound):
        self._center = p.Point()
        self._velocity = p.Velocity()
        self.alive = True
        self._texture = arcade.load_texture(img)
        if sound != 0:
            self._sound = arcade.load_sound(sound)
        self._radius = 5
        self._scale = 1
        self._hit = 0

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

    def sound(self):
        arcade.play_sound(self._sound)

    def hit(self):
        return self._hit

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
