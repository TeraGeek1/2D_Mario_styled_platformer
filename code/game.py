import pygame, sys, os
sys.path.append(os.path.join(sys.path[0], 'world'))
sys.path.append(os.path.join(sys.path[0], 'player')) #stops an import error when directly running this file
from settings import *
from level import Level


class Game:

    def __init__(self) -> None:

        # init func
        pygame.init()

        # init vars
        self.level = Level(level_map)


    def run(self):
        while True: # game loop
            screen.fill('Black') # fills the background with black
            for event in pygame.event.get(): # event loop
                if event.type == pygame.QUIT: # exit game event
                    pygame.quit()
                    sys.exit()
                                
            self.level.draw(screen) # draws the current level to the screen


            pygame.display.update() # refresh the screen
            clock.tick(FPS) # Sets the games fps to 60