import pygame, sys
from settings import *
from world.level import Level


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
            self.level.update()

            
            pygame.display.update()
            clock.tick(60)