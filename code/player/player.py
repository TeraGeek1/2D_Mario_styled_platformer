import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos = (0,0)) -> None:

        # init funcs
        super().__init__()


        # init vars
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
