class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0


    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        purse = cast.get_first_actor("purse")
        velocity = self._keyboard_service.get_direction()
        purse.set_velocity(velocity)
    
    def _do_updates(self, cast):
        banner = cast.get_first_actor("banners")
        purse = cast.get_first_actors("purse")
        artifacts = cast.get_first_actors("artifacts")
        #gems = cast.get_first_actors("gems")
        #rocks = cast.get_first_actors("rocks")

        max_y = self._video_service.get_height()
        max_x = self._video_service.get_width()
        purse.move_next(max_x, max_y)

        for artifact in artifacts:
            if purse.get_position().equals(artifact.get_position()):
                self._score+= artifact.get_score()
                banner.set_text(self._score)

    def _do_outputs(self, cast):
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
                