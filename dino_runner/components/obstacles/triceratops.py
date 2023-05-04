from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import TRICERATOPS

class Triceratops(Obstacle):
    Y_POS_TRICERATOPS = 250
    steps_index = 0

    def __init__(self):
        self.image = TRICERATOPS[0]
        super().__init__(self.image)
        self.rect.y = self.Y_POS_TRICERATOPS

    def update(self, game_speed, player):
        self.image  = TRICERATOPS[0] if self.steps_index < 5 else TRICERATOPS[1]
        self.steps_index += 1
        if self.steps_index >= 10:
            self.steps_index  = 0
        super().update(game_speed, player)
