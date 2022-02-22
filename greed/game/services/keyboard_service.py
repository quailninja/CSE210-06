import arcade


class KeyboardService(arcade.View):
    """
    Handles the keyboard inputs for the game

    Attributes:
        _item_move (class): A class that can be moved by the player
        move_speed (int): how fast the player can move the object
        width (int): screen width
    """

    def __init__(self, item_move, move_speed):
        super().__init__()
        self._item_move = item_move
        self._move_speed = move_speed

    def check_keys(self, key, view1, view2):
        """
        Checks if a certain key is being pressed
        """
        if key == arcade.key.LEFT:
            self._item_move.move_left(self._move_speed)

        if key == arcade.key.RIGHT:
            self._item_move.move_right(self.window.width, self._move_speed)

        if key == arcade.key.ESCAPE:
            self.window.show_view(view1)

        elif key == arcade.key.Q:
            arcade.close_window()

        elif key == arcade.key.ENTER and view2 != 0:
            self.window.show_view(view2)
