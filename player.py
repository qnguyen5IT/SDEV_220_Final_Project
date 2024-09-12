import pygame, sys
from pygame.locals import *


class Player:
    def __init__(self, window):
        # Set up variables to use, also where rects will be created at.
        self.window = window


    def update(self):
        # This is where things like collision detection, animations changes, checks to
        # see if the player was hit by a bullet or an alien crashed into them.
        pass


    def draw(self):
        # This is where the sprite get drawn to the screen.
        pass
