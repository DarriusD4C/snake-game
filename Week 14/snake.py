from food import Food
from game_manager import GameManager
from snake_enums import Color, Direction
from square import Square


class Snake:
    """Class to manage the snake."""

    def __init__(self, gm: GameManager) -> None:
        self.gm: GameManager = gm
        self.head: Segment = Segment(self.gm, gm.center(), Direction.up)
        self.segments: list = [self.head]

    def draw(self) -> None:
        """Render the sanke to the screen."""

        for segment in self.segments:
            segment.draw()

    def move(self) -> None:
        """Move all segments forward their direction."""

        for segment in self.segments:
            segment.x += segment.size * segment.direction[0]
            segment.y += segment.size * segment.direction[1]

        self.update_directions()

    def update_directions(self) -> None:
        """Update the direction of each nt starting with the back."""

        for index in range(len(self.segments)-1, 0, -1):
            before: Segment = self.segments[index - 1]
            self.segments[index].direction = before.direction

    def grow(self) -> None:
        """Add a new segment forward their direction."""

        end: Segment = self.segments[-1]
        x_loc: int = (end.x + self.gm.size * -end.direction[0])
        y_loc: int = (end.y + self.gm.size * -end.direction[1])
        segment: Segment = Segment(self.gm, (x_loc, y_loc), end.direction)

        self.segments.append(segment)

    def wall_hit(self) -> bool:
        """Check of the snake head is colliding with a wall."""

        x_hit: bool = self.head.x < 0 or self.head.x >= self.gm.width
        y_hit: bool = self.head.y < 0 or self.head.x >= self.gm.height

        return x_hit or y_hit
    
    def overlap(self, point: tuple) -> bool:
        """Check if point is overlapping with the snake."""

        for index, segment in enumerate(self.segments):
            if index > 2 and point == segment.get_pos():
                return True
        return False
    
    def body_hit(self) -> bool:
        """Check if snake is colliding with itself."""

        return self.overlap(self.head.get_pos())
    
    def food_hit(self, food: Food) -> bool:
        """Checks if head overlaps with food."""

        return self.head.get_pos() == food.get_pos()


class Segment(Square):
    """A class to represent a segment of the snake."""

    def __init__(
        self,
        gm: GameManager,
        pos: tuple,
        direction: Direction,
    ) -> None:
        
        super().__init__(gm, pos, Color.snake)
        self.direction: Direction = direction