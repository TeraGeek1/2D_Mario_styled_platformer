import pygame

clock = pygame.time.Clock() # global game clock
pygame.init() # used to make screen


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
'XXXXXXXX  XXXXXX  XX  XXXX  '] # demo map

screen_width = 800
tile_size = int(screen_width / 18.75) # the size of all the games tiles
screen_height = len(level_map) * tile_size


screen = pygame.display.set_mode((screen_width, screen_height)) # the global screen