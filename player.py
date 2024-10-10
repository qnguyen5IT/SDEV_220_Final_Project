import pygame, sys
from pygame.locals import *

from resources import Resources


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

        self.cooldown_time = 0
        self.destroyed = False
    
        self.movement = True
        self.fire = False     
        self.right = False
        self.left = False

    def cooldown(self):
        # Time it takes for player to spawn back be invinsible.
        self.cooldown_time = 50

    def dispose(self):
        del self.image

    def update(self, health, bullet):
        # Player colliding with bullets is done in projectiles module.

        # Player Controls
        if self.cooldown_time > 0:
            self.cooldown_time -= 1
        if self.cooldown_time <= 0:
            self.movement = True

        # Movment
        if self.right == True and self.rect.right < self.window.get_width() and self.movement:
            self.rect.x += self.speed
        if self.left == True and self.rect.x > 0 and self.movement:
            self.rect.x -= self.speed

        # Fire (shoot)
        if self.fire == True:
            bullet.create(self.rect.centerx, self.rect.centery, "up", "player")
            self.fire = False

        # Check players health.
        # If health == 0 GameOver.
        if health.hitpoints == 0:
            self.destroyed = True
            self.movement = False
            Resources.game_over = True
        
            
    def get_sprite(self, x, y, w, h, new_width, new_height):
        player = pygame.Surface((w, h)).convert()
        player.set_colorkey((255, 255, 255)) # Sprite background is white
        player.blit(self.image, (0, 0), (x, y, w, h)) # Copying the player from the sprite sheet

        # Scale the player sprite to the new dimensions
        player_scaled = pygame.transform.scale(player, (new_width, new_height))
        return player_scaled


    def draw(self):
        if self.cooldown_time % 10 == 0 and self.destroyed == False:
            # This is where the sprite get drawn to the screen.
            self.window.blit(self.image, (self.rect.x, self.rect.y))
        
