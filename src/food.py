from random import randrange

from game_manager import GameManager
from snake_enums import Color
from square import Square


class Food(Square):
    """Food object to be consumed by snake."""

    def __init__(self, gm: GameManager, pos: tuple) -> None:
        super().__init__(gm, pos, Color.food)

    def move(self) -> None:
        """Move food to random location."""

        self.x = randrange(0, self.gm.width, self.size)
        self.y = randrange(0, self.gm.height, self.size)