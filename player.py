import pygame, sys
from pygame.locals import *


class Player:
    def __init__(self, window, image, color):
        # Set up variables to use, also where rects will be created at.
        self.window = window

        self.width = 300
        self.height = 420
        self.speed = 6

        self.image = image
        self.image = self.get_sprite(0, 0, 623, 869, 40, 56)

        self.rect = self.image.get_rect()

        self.rect.centerx = self.window.get_width() // 2
        self.rect.bottom = self.window.get_height() - 70

        self.right = False
        self.left = False


    def update(self):
        # This is where things like collision detection, animations changes, checks to
        # see if the player was hit by a bullet or an alien crashed into them.
        # Player Controls
        if self.right == True and self.rect.right < self.window.get_width():
            self.rect.x += self.speed
        if self.left == True and self.rect.x > 0:
            self.rect.x -= self.speed
            


    def get_sprite(self, x, y, w, h, new_width, new_height):
        player = pygame.Surface((w, h)).convert()
        player.set_colorkey((255, 255, 255)) # Sprite background is white
        player.blit(self.image, (0, 0), (x, y, w, h)) # Copying the player from the sprite sheet

        # Scale the player sprite to the new dimensions
        player_scaled = pygame.transform.scale(player, (new_width, new_height))
        return player_scaled


    def draw(self):
        # This is where the sprite get drawn to the screen.
        self.window.blit(self.image, (self.rect.x, self.rect.y))
