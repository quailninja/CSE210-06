import arcade
from game.screens.instruction_screen import InstructionView

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Greed"

donkey = True


def main():
    """Main function
    This starts the arcade window that is run by the Video
    """
    # VideoService(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # arcade.run()
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
