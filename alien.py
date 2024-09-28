import pygame, sys
from pygame.locals import *


class Alien:
    def __init__(self, window, Sprite_sheet, x, y, w, h, new_width, new_height):
        # Set up variables to use, also where rects will be created at.
        self.window = window
        self.Sprite_sheet = pygame.image.load(Sprite_sheet).convert()

        # Pass new_width and new_height to the get_sprite method
        self.image = self.get_sprite(x, y, w, h, new_width, new_height)
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,60)


    def update(self):
        # This is where things like collision detection, animations changes, checks to
        # see if the alien was hit by a bullet.
        pass


    def get_sprite(self, x, y, w, h, new_width, new_height):
        alien = pygame.Surface((w, h)).convert()
        alien.set_colorkey((255, 255, 255)) # Sprite background is white
        alien.blit(self.Sprite_sheet, (0, 0), (x, y, w, h)) # Copying the alien from the sprite sheet

        # Scale the alien sprite to the new dimensions
        alien_scaled = pygame.transform.scale(alien, (new_width, new_height))
        return alien_scaled


    def draw(self):
        # This is where the sprite gets drawn to the screen.
        self.window.blit(self.image, self.rect)
        pass
