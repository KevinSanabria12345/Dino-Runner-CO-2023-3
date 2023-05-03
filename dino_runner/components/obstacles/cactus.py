import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS



class Cactus(Obstacle):
    Y_POS_SMALL_CACTUS = 325
    Y_POS_LARGE_CACTUS = 300


    def __init__(self):
        all_cactus = (SMALL_CACTUS + LARGE_CACTUS)
        self.image = random.choice(all_cactus) 
        super().__init__(self.image)
        if self.image in SMALL_CACTUS:
          self.rect.y = self.Y_POS_SMALL_CACTUS
        
        if self.image in LARGE_CACTUS:
           self.rect.y = self.Y_POS_LARGE_CACTUS


          




    