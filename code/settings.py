import pygame

clock = pygame.time.Clock()
pygame.init()


level_map = [
'                            ',
'                            ',
'                            ',
' XX    XXX            XX    ',
' XX P                       ',
' XXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

screen_width = 800
tile_size = int(screen_width / 18.75)
screen_height = len(level_map) * tile_size

print(screen_width, screen_height)
screen = pygame.display.set_mode((screen_width, screen_height))