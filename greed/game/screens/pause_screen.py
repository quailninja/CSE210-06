import arcade


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
        self.game_view = game_view
        self._i_view = i_view

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
            If user hits the ESC key they return to the game
            If user hits the ENTER key they exit the game
        """
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)
        elif key == arcade.key.Q:
            arcade.close_window()
        elif key == arcade.key.ENTER:
            self.window.show_view(self._i_view)

    # def on_key_press(self, key, key_modifiers):
    #     self._key = key
