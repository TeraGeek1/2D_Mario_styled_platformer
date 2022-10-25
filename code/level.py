import pygame
from tiles import Tile

class Level:
    
    def __init__(self,level_data,surface) -> None:
        self.display_surface = surface