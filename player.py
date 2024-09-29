import pygame, sys
from pygame.locals import *


class Player:
    def __init__(self, window, image):
        # Set up variables to use, also where rects will be created at.
        self.window = window
        self.image = image


    def update(self):
        # This is where things like collision detection, animations changes, checks to
        # see if the player was hit by a bullet or an alien crashed into them.
        pass

    def draw(self, frame, width, height, scale, color):
        # This is where the sprite get drawn to the screen.
        image = pygame.Surface((width, height)).convert_alpha()

        image.blit(self.image, (0,0), ((frame * width), 0, width, height))

        image = pygame.transform.scale(image, (width * scale, height * scale))

        image.set_colorkey(color)
        
        return image
