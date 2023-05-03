import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.select_power_up = ("Shield", "Hammer")


    def update(self, game_speed, points, player):
        self.image = random.choice(self.select_power_up)
        if self.image == "Shield" and len(self.power_ups) == 0 and points % 200 == 0:
            self.power_ups.append(Shield())
        if self.image == "Hammer" and len(self.power_ups) == 0 and points % 200 == 0:
            self.power_ups.append(Hammer())
        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.remove(power_up)
            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)
      
    def draw(self, screen):
        for power_up in self.power_ups:
          power_up.draw(screen)
