import arcade
from game.directing.game_director import GameDirector


TITLE_LINE_HEIGHT = 70
DEFAULT_LINE_HEIGHT = 50
TITLE_FONT_SIZE = 60
DEFAULT_FONT_SIZE = 20


class InstructionView(arcade.View):
    """Instruction Screen

    This is the first screen shown to players when the game starts.

    Attributes:
        none
    """

    def __init__(self):
        super().__init__()

    def on_show(self):
        """Updates the background and resets user view

        Args:
            changes back ground color and also the viewport the view port change doesn't seem necessary
        """

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """Draws users view

        Args:
            Instructions given to user on screen using arcades draw_text function
        """
        self.clear()
        arrows = arcade.load_texture("greed/game/images/arrows.png")
        red_gem = arcade.load_texture("greed/game/images/red.png")
        blue_gem = arcade.load_texture("greed/game/images/blue.png")
        yellow_gem = arcade.load_texture("greed/game/images/yellow.png")
        rock = arcade.load_texture("greed/game/images/rock.png")
        self.clear()
        start_y = self.window.height - 100
        start_x = self.window.width / 2
        arcade.draw_text(
            "Welcome to Greed!",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=TITLE_FONT_SIZE,
            anchor_x="center",
        )

        start_y -= TITLE_LINE_HEIGHT
        arcade.draw_text(
            "Use the arrow keys to move the bag.",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
        )
        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_scaled_texture_rectangle(start_x, start_y, arrows, 0.25)

        start_y -= DEFAULT_LINE_HEIGHT + 10
        arcade.draw_text(
            "ESC key to pause.",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
        )

        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_scaled_texture_rectangle(start_x - 60, start_y + 10, blue_gem, 1)
        arcade.draw_scaled_texture_rectangle(start_x - 10, start_y + 10, yellow_gem, 1)
        arcade.draw_text(
            "= 2",
            start_x + 30,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
        )
        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_scaled_texture_rectangle(start_x - 25, start_y + 10, red_gem, 1)
        arcade.draw_text(
            "= 7",
            start_x + 30,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
        )
        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_scaled_texture_rectangle(start_x - 25, start_y + 10, rock, 1)
        arcade.draw_text(
            "= -10",
            start_x + 40,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
        )

        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text(
            "Click to start the game",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE / 2,
            anchor_x="center",
        )

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Waits to detect mouse click from user

        Args:
            uses arcades on_mouse_press to detect mouse click
            then it changes the screen
        """
        game = GameDirector(self)
        self.window.show_view(game)
