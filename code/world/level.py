import pygame
from settings import *
from tiles import Tile

class Level:
    
    def __init__(self,level_data = level_map, surface = screen) -> None:
        self.display_surf = surface
        self.level_data = level_data