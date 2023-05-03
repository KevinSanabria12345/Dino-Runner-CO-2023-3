import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Birds

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.all_obstacles = (Cactus, Birds)

    def update(self, game_speed,player):
        self.image = random.choice(self.all_obstacles)
        if self.image == Cactus and len(self.obstacles) == 0 :
            self.obstacles.append(Cactus())
        if self.image == Birds and len(self.obstacles) == 0 :
            self.obstacles.append(Birds())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)    