import pygame, sys, os
sys.path.append(os.path.join(sys.path[0], '..', '..','code')) # adds code to the local reach
sys.path.append(os.path.join(sys.path[0], '..', 'player')) # adds player to the local reach
from settings import *
from tiles import Tile
from player import Player

class Level:
    
    def __init__(self,level_data = level_map) -> None:
        
        self.setup(level_data) # setup the objects to be placed on the screen
        self.world_shift = 0 # The camera location


    def setup(self, layout):

        # object groups
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()


        for row_idx, row in enumerate(layout): # unpack the level
            for col_idx, cell in enumerate(row):
                correct_pos = (col_idx*tile_size,row_idx*tile_size)

                if cell == 'X': # Adds test tiles
                    tile = Tile(correct_pos,tile_size)
                    self.tiles.add(tile)
                
                if cell == 'P': # Adds a player to the world
                    self.player.add(Player(correct_pos))


    
    def draw(self, surface = screen): # draws and updates the groups to the screen

        # tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(surface)

        # player
        self.player.update()
        self.player.draw(surface)
