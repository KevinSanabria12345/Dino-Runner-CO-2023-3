import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Birds
from dino_runner.components.obstacles.triceratops import Triceratops

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.all_obstacles = (Cactus, Birds, Triceratops)

    def update(self, game_speed,player):
        self.image = random.choice(self.all_obstacles)
        if self.image == Cactus and len(self.obstacles) == 0 :
            self.obstacles.append(Cactus())
        elif self.image == Birds and len(self.obstacles) == 0 :
            self.obstacles.append(Birds())
        elif self.image == Triceratops and len(self.obstacles) == 0 :
            self.obstacles.append(Triceratops())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width or player.hammer == True:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)    