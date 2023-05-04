from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import TRAMPOLINE, TRAMPOLINE_TYPE

class SaltoTrampolin(PowerUp):
    def __init__(self):
        self.image = TRAMPOLINE 
        self.type = TRAMPOLINE_TYPE
        super().__init__(self.image, self.type)