import pygame, sys
sys.path.append("..")
from settings import *
from world.tiles import Tile

class Level:
    
    def __init__(self,level_data = level_map) -> None:
        self.setup(level_data)

        self.world_shift = 0


    def setup(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_idx, row in enumerate(layout):
            for col_idx, cell in enumerate(row):
                if cell == 'X':
                    tile = Tile((col_idx*tile_size,row_idx*tile_size),tile_size)
                    self.tiles.add(tile)

    
    def draw(self, surface = screen):
        self.tiles.update(self.world_shift)
        self.tiles.draw(surface)
