import pygame
from os import walk
pygame.init()


def import_folder(path: str):
    surface_list = []
    for _,__,img_files in walk(path):
        for img in img_files:
            surface_list.append(pygame.image.load(f"{path}/{img}").convert_alpha())
    return surface_list
        
