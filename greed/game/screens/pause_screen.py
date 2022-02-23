import arcade
from game.services.keyboard_service import KeyboardService


class PauseView(arcade.View):
    """Pause screen

    This screen appears if the player hits the ESC key

    Attributes:
        game_view (?): Captures the game screen information until the player resumes the game.
        width (int): Screen width
        height (int): screen height
    """

    def __init__(self, game_view, i_view):
        super().__init__()
        self._game_view = game_view
        self._i_view = i_view
        self._keyboard_services = KeyboardService(0, 0)

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        """draws images on the pause screen

        Args:
            clears the screen for new screen
            inputs a message on the screen for the user
        """
        self.clear()

        arcade.draw_text(
            "PAUSED",
            self.window.width / 2,
            self.window.height / 2 + 50,
            arcade.color.BLACK,
            font_size=50,
            anchor_x="center",
        )

        arcade.draw_text(
            "Press Esc. to return",
            self.window.width / 2,
            self.window.height / 2,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Press Q to quit",
            self.window.width / 2,
            self.window.height / 2 - 30,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Enter to restart",
            self.window.width / 2,
            self.window.height / 2 - 60,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )

    def on_key_press(self, key, _modifiers):
        """Checks user key press

        Args:
            runs keyboard_services check keys class
        """
        self._keyboard_services.check_keys(key, self._game_view, self._i_view)
