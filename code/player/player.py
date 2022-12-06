import pygame
from settings import *
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0)) -> None:

        # init funcs
        super().__init__()


        # init vars
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        

        ## player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        self.coyote_jump = 0
        self.coyote_time = 150



    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[K_d] or keys[K_RIGHT]:
            self.direction.x = 1
        elif keys[K_a] or keys[K_LEFT]:
            self.direction.x = -1
        else: self.direction.x = 0

        if keys[K_SPACE] or keys[K_UP]: # Checks if the player is jumping
            if self.direction.y == 0 or self.current_time - self.coyote_jump <= self.coyote_time: 
                self.jump()

    
    def apply_gravity(self):
        self.direction.y += self.gravity


    def jump(self):
        self.direction.y = self.jump_speed

    def update(self) -> None:
        self.current_time = pygame.time.get_ticks()
        self.get_input()
        self.apply_gravity()