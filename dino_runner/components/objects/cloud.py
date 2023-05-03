import random
from dino_runner.components.objects.object import Object
from dino_runner.utils.constants import CLOUD


class Clouds(Object):
    Y_POS_CLOUD_1 = 150
    Y_POS_CLOUD_2 = 200
    Y_POS_CLOUD_3 = 50
    Y_POS_CLOUD_4 = 170
    POS_Y = (Y_POS_CLOUD_1,Y_POS_CLOUD_2,Y_POS_CLOUD_3,Y_POS_CLOUD_4) 

    



    
    def __init__(self):
        self.image =  CLOUD
        super().__init__(self.image)
        self.rect.y = random.choice(self.POS_Y)
        self.image =  CLOUD
        self.rect.y = random.choice(self.POS_Y)
        self.image =  CLOUD
        self.rect.y = random.choice(self.POS_Y)
        self.image =  CLOUD
        self.rect.y = random.choice(self.POS_Y)
       




