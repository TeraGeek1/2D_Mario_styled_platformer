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
                current_pos = (col_idx * tile_size, row_idx * tile_size)

                if cell == 'X': # Adds test tiles
                    tile = Tile(current_pos,tile_size)
                    self.tiles.add(tile)
                
                if cell == 'P': # Adds a player to the world
                    self.player.add(Player(current_pos))

                
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/2.5 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width/2.5) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8


    def horizontal_movement_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

                
    
    def vertical_movement_collisions(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: # Bottom player collision
                    player.rect.bottom = sprite.rect.top # corrects collision
                    player.direction.y = 0 # Activate coyote timer and allow jumping
                    player.on_ground = True
                elif player.direction.y < 0: # Top player collision
                    player.rect.top = sprite.rect.bottom # corrects collision
                    player.direction.y = 1 # don't change to 0
                    player.on_ceiling = True
        
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 1:
            player.on_ceiling

                    

    
    def draw(self, surface = screen): # draws and updates the groups to the screen
        self.scroll_x()

        # tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(surface)

        # player
        self.player.update()
        self.horizontal_movement_collisions()
        self.vertical_movement_collisions()
        self.player.draw(surface)
