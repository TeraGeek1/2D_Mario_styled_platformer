import pygame, sys
from os import path
sys.path.append(path.join(sys.path[0], '..'))
from settings import *
from pygame.locals import *
from support import import_folder


class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0)) -> None:

        # init funcs
        super().__init__()

        # init vars

        ## player state
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False


        ## animation
        self.import_assets()
        self.frame_idx = 0
        self.animation_speed = 0.15
        self.image = self.animations[self.status][self.frame_idx]
        self.rect = self.image.get_rect(topleft = pos)
        

        ## player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        self.allowed_jumps = 1
        self.current_jumps = 0
        self.coyote_jump = 0
        self.coyote_time = 150


    def animate(self):
        self.get_status()
        animate = self.animations[self.status]

        # loop over frame index
        self.frame_idx += self.animation_speed
        if self.frame_idx >= len(animate): self.frame_idx = 0
        self.image = animate[int(self.frame_idx)]
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image,True,False)
        

        # set the rect
        if self.on_ground:
            if self.on_left:
                self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
            elif self.on_right:
                self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
            else:
                self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

        elif self.on_ceiling:
            if self.on_left:
                self.rect = self.image.get_rect(topleft = self.rect.topleft)
            elif self.on_right:
                self.rect = self.image.get_rect(topright = self.rect.topright)
            else:
                self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[K_d] or keys[K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[K_a] or keys[K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else: self.direction.x = 0

        if keys[K_SPACE] or keys[K_UP]: # Checks if the player is jumping
            if self.on_ground or self.current_time - self.coyote_jump <= self.coyote_time: 
                self.jump()



    def get_status(self):
        # feature status
        if self.on_ground:
            self.coyote_jump = pygame.time.get_ticks()
            self.current_jumps = 0

        # animation status
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'


    def import_assets(self):
        character_path = 'graphics/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y


    def jump(self):
        if not self.current_jumps >= self.allowed_jumps:
            self.direction.y = self.jump_speed
            self.current_jumps += 1

    def update(self) -> None:
        self.current_time = pygame.time.get_ticks()
        self.get_input()
        self.animate()