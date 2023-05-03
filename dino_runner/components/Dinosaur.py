import pygame
from dino_runner.utils.constants import (JUMPING, RUNNING, DUCKING, DEAD, RUNNING_SHIELD, DUCKING_SHIELD, JUMPING_SHIELD,
                                         DEFAULT_TYPE, SHIELD_TYPE, RUNNING_HAMMER, DUCKING_HAMMER, JUMPING_HAMMER, HAMMER_TYPE)

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5


    
    def __init__(self):
        self.run_image = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
        self.duck_image = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
        self.jump_image = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
        self.type = DEFAULT_TYPE
        self.image = self.run_image[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False  
        self.jump_vel = self.JUMP_VEL   
        self.dino_dead = False 
        self.count_jump = 0
        self.dino_super_jump = False
        self.dino_trampoline_jump = False
    
    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_super_jump:
            self.super_jump()
        if self.dino_trampoline_jump:
            self.trampoline_jump()

                
        if user_input[pygame.K_DOWN ] and not self.dino_jump and not self.dino_super_jump and not self.dino_trampoline_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False 
            self.dino_super_jump = False
        elif user_input[pygame.K_UP] and not self.dino_jump and not self.dino_super_jump and not self.dino_trampoline_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.dino_super_jump = False 
        elif user_input[pygame.K_SPACE] and not self.dino_jump and not self.dino_super_jump and not self.dino_trampoline_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = False
            self.dino_super_jump = True
        elif user_input[pygame.K_z] and not self.dino_jump and not self.dino_super_jump and not self.dino_trampoline_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.dino_super_jump = False
            self.dino_trampoline_jump = True  
        elif not self.dino_jump and not self.dino_super_jump and not self.dino_trampoline_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
            self.dino_super_jump = False 

                
        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)

    def dead(self):
        if self.dino_duck:
            self.image = DEAD
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.dino_dead = True
        self.image = DEAD
        self.dino_dead = True

    def run(self):
        if self.type == HAMMER_TYPE:
            self.image = self.run_image[self.type][0] if self.step_index < 5 else self.run_image[self.type][1]
        else:
            self.image = self.run_image[self.type][0] if self.step_index < 5 else self.run_image[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS 
        self.step_index += 1       
   
    def duck(self):
        self.image = self.duck_image[self.type][0] if self.step_index < 5 else self.duck_image[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jump_image[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def super_jump(self):
        self.image = self.jump_image[self.type]
        if self.dino_super_jump:
            self.dino_rect.y -= self.jump_vel * 6
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_super_jump = False
            self.jump_vel = self.JUMP_VEL

    def trampoline_jump (self):
        self.image = self.jump_image[self.type]
        if self.dino_trampoline_jump:
            self.dino_rect.y -= self.jump_vel * 6
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_trampoline_jump = False
            self.jump_vel = self.JUMP_VEL

    def set_power_up(self, power_up):
        if power_up.type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
        if power_up.type == HAMMER_TYPE:
            self.type = HAMMER_TYPE

        

    
       
            