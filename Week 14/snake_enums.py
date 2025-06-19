class AudioFile:
    """Sound class to hold all audio files."""

    eat: str = "audio/gulp.wav"
    music: str = "audio/music.ogg"


class Color:
    """Color class to store RGB values for a color."""

    bg: tuple = (5, 255, 165)
    food: tuple = (255, 5, 155)
    snake: tuple = (255, 150, 5)
    text: tuple = (5, 130, 255)


class Direction:
    """Directions used for snake."""

    up: tuple = (0, -1)
    down: tuple = (0, 1)
    right: tuple = (1, 0)
    left: tuple = (-1, 0)


class State:
    """State class to represent the game states."""

    menu: int = 0
    in_game: int = 1
    game_over: int = 2
    end_game: int = 3

    def next_state(state: int) -> int:
        """Get the next state"""

        state = (state + 1) % 3
        return state