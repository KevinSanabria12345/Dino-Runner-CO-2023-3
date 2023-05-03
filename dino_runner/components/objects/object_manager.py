from dino_runner.components.objects.cloud import Clouds

class ObjectManager:
    def __init__(self):
        self.objects = []

    def update(self, game_speed):
        if len(self.objects) == 0:
            self.objects.append(Clouds())
        for object in self.objects:
            if object.rect.x < -object.rect.width:
                self.objects.remove(object)
            object.update(game_speed)


    def draw(self, screen):
        for object in self.objects:
            object.draw(screen)
