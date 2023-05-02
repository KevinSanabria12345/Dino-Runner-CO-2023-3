import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import CLOUD
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager 


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        #Clouds
        self.x_pos_cloud = 2000
        self.y_pos_cloud = 150
        self.game_speed_cloud = 1.5
        self.x_pos_cloud_2 = 1080
        self.y_pos_cloud_2 = 100
        self.game_speed_cloud_2 = 1.3
        self.x_pos_cloud_3 = 1300
        self.y_pos_cloud_3 = 20
        self.game_speed_cloud_3 = 1
        self.x_pos_cloud_4 = 2500
        self.y_pos_cloud_4 = 46
        self.game_speed_cloud_4 = 1
        self.x_pos_cloud_5 = 1500
        self.y_pos_cloud_5 = 130
        self.game_speed_cloud_5 = 1
        self.x_pos_fondo = 0
        self.y_pos_fondo = 230
        self.obstacle_Manager = ObstacleManager()


       

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_Manager.update(self.game_speed, self.player)
        if self.player.dino_dead:
            self.playing = False
            
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()       
        self.draw_cloud()
        self.obstacle_Manager.draw(self.screen)

        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD,(self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -200:
            self.screen.blit(CLOUD,(image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1200
        self.x_pos_cloud -= self.game_speed_cloud
        image_width_2 = CLOUD.get_width()
        self.screen.blit(CLOUD,(self.x_pos_cloud_2, self.y_pos_cloud_2))
        if self.x_pos_cloud_2 <= -200:
            self.screen.blit(CLOUD,(image_width_2 + self.x_pos_cloud_2, self.y_pos_cloud_2))
            self.x_pos_cloud_2 = 1200
        self.x_pos_cloud_2 -= self.game_speed_cloud
        image_width_3 = CLOUD.get_width()
        self.screen.blit(CLOUD,(self.x_pos_cloud_3, self.y_pos_cloud_3))
        if self.x_pos_cloud_3 <= -200:
            self.screen.blit(CLOUD,(image_width_3 + self.x_pos_cloud_3, self.y_pos_cloud_3))
            self.x_pos_cloud_3 = 1200
        self.x_pos_cloud_3 -= self.game_speed_cloud_3
        image_width_4 = CLOUD.get_width()
        self.screen.blit(CLOUD,(self.x_pos_cloud_4, self.y_pos_cloud_4))
        if self.x_pos_cloud_4 <= -200:
            self.screen.blit(CLOUD,(image_width_4 + self.x_pos_cloud_4, self.y_pos_cloud_4))
            self.x_pos_cloud_4 = 1200
        self.x_pos_cloud_4 -= self.game_speed_cloud_4
        image_width_5 = CLOUD.get_width()
        self.screen.blit(CLOUD,(self.x_pos_cloud_5, self.y_pos_cloud_5))
        if self.x_pos_cloud_5 <= -200:
            self.screen.blit(CLOUD,(image_width_5 + self.x_pos_cloud_5, self.y_pos_cloud_5))
            self.x_pos_cloud_5 = 1200
        self.x_pos_cloud_5 -= self.game_speed_cloud_5
    
   