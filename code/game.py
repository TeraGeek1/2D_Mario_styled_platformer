import pygame, sys, os
sys.path.append(os.path.join(sys.path[0], 'world'))
sys.path.append(os.path.join(sys.path[0], 'player'))
from settings import *
from level import Level
from player import Player


class Game:

    def __init__(self) -> None:
        pygame.init()
        self.level = Level(level_map)


    def run(self):
        while True:
            screen.fill('Black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                                
            self.level.draw(screen)


            pygame.display.update()
            clock.tick(60)