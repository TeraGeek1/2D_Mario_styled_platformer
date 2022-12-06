import pygame, sys, os
sys.path.append(os.path.join(sys.path[0], '..', '..','code'))
sys.path.append(os.path.join(sys.path[0], '..', 'player'))
from settings import *
from tiles import Tile
from player import Player

class Level:
    
    def __init__(self,level_data = level_map) -> None:
        self.setup(level_data)
        self.world_shift = 0


    def setup(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_idx, row in enumerate(layout):
            for col_idx, cell in enumerate(row):
                correct_pos = (col_idx*tile_size,row_idx*tile_size)

                if cell == 'X':
                    tile = Tile(correct_pos,tile_size)
                    self.tiles.add(tile)
                
                if cell == 'P':
                    self.player.add(Player(correct_pos))


    
    def draw(self, surface = screen):
        self.tiles.update(self.world_shift)
        self.tiles.draw(surface)
        self.player.update()
        self.player.draw(surface)
