import os
import sys
import pygame

def load_image(name, colorkey = None):
    fullname = os.path.join('images', name)
    image = pygame.image.load(fullname)
    return image