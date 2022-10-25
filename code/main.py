import pygame
from settings import *
import sys

pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
    screen.fill('Black')
    
    
    pygame.display.update()
    clock.tick(60)