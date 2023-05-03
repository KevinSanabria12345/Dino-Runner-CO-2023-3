import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Birds(Obstacle):
    Y_POS_BIRD_HIGH = 220
    Y_POS_BIRD_MEDIUM = 260
    Y_POS_BIRD_LOW = 300
    POS_Y = (Y_POS_BIRD_HIGH,Y_POS_BIRD_MEDIUM,Y_POS_BIRD_LOW) 
    steps_index = 0

    
    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = random.choice(self.POS_Y)
   

    def update(self, game_speed, player):
        self.image  = BIRD[0] if self.steps_index < 5 else BIRD[1]
        self.steps_index += 1
        if self.steps_index >= 10:
            self.steps_index  = 0
        super().update(game_speed, player)


