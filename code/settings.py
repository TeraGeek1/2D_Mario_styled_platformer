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

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size

screen = pygame.display.set_mode((screen_width, screen_height))