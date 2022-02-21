import arcade
from game.directing.game_director import GameDirector

TITLE_LINE_HEIGHT = 75
DEFAULT_LINE_HEIGHT = 45
TITLE_FONT_SIZE = 50
DEFAULT_FONT_SIZE = 20


class InstructionView(arcade.View):
    """Instruction Screen

    This is the first screen shown to players when the game starts.

    Attributes:
        none
    """

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
            "Use the arrow keys to move the bag. ESCAPE key to pause.",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
        )

        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text(
            "Gems are worth 2 points, rocks are -10 points",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
        )

        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text(
            "You win if you can get 600 points.",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
        )

        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text(
            "You lose if you get -20 points",
            start_x,
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
