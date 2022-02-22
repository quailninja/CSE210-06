import arcade


class KeyboardService(arcade.View):
    def __init__(self, item_move, move_speed, width):
        super().__init__()
        self._item_move = item_move
        self._move_speed = move_speed
        self.width = width

    def check_keys(self, key, pause):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if key == 65361:  # left directional button
            self._item_move.move_left(self._move_speed)

        if key == 65363:  # right directional button
            self._item_move.move_right(self.width, self._move_speed)

        if key == 65307:  # escape key
            self.window.show_view(pause)
