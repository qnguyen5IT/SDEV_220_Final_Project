import pygame, sys
from pygame.locals import *

from random import randint


class Alien:
    def __init__(self, window, Sprite_sheet, x, y, w, h, new_width, new_height, speed_x, speed_y):
        # Set up variables to use, also where rects will be created at.
        self.window = window
        self.Sprite_sheet = pygame.image.load(Sprite_sheet).convert_alpha()

        # Pass new_width and new_height to the get_sprite method
        self.image = self.get_sprite(x, y, w, h, new_width, new_height)
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,60)

        # Aliens positioning and movement for duplicates.
        self.x = self.rect.x
        self.y = self.rect.y
        self.width = new_width
        self.height = new_height
        self.speed_x = speed_x
        self.speed_y = speed_y

        self.direction = "right"

        self.aliens = []
        self.create_aliens(row_amount=5)

    def create_aliens(self, row_amount):
        # This spawns in the aliens. 
        self.aliens = []
        spawn_x = self.rect.x
        spawn_y = 0
        alien_spacing = 20
        for number in range(row_amount):
            # Created 10 aliens place in a row.
            for number2 in range(10):
                alien = pygame.Rect(spawn_x, spawn_y, self.rect.width, self.rect.height)
                #save alien rect to list. 
                self.aliens.append(alien)
                spawn_x += 60

            spawn_x = self.rect.x
            spawn_y += self.rect.height + alien_spacing


    def update(self, bullet):
        # This is where things like collision detection, animations changes, checks to
        # see if the alien was hit by a bullet.

        # Move aliens and handle direction changes. 
        for alien in self.aliens:
            if self.direction == "right":
                alien.x += self.speed_x 
            elif self.direction == "left":
                alien.x -= self.speed_x 

            # Fire at player.
            is_fire = randint(1, 400)
            if is_fire == 1:
                bullet.create(alien.x + 16, alien.y + 16, "down", "alien")
            
            

        # Check if the rightmost alien has hit the window's edge.
        highest_x = max(alien.x for alien in self.aliens)
        if highest_x > self.window.get_width() - 60:
            for alien in self.aliens:
                alien.y += 15
            self.direction = "left"

        # Check if the leftmost alien has hit the window's edge.
        lowest_x = min(alien.x for alien in self.aliens)
        if lowest_x < 20:
            for alien in self.aliens:
                alien.y += 15
            self.direction = "right"


        

        

    def get_sprite(self, x, y, w, h, new_width, new_height):
        alien = pygame.Surface((w, h)).convert()
        alien.set_colorkey((255, 255, 255)) # Sprite background is white
        alien.blit(self.Sprite_sheet, (0, 0), (x, y, w, h)) # Copying the alien from the sprite sheet

        # Scale the alien sprite to the new dimensions
        alien_scaled = pygame.transform.scale(alien, (new_width, new_height))
        return alien_scaled


    def draw(self):
        # This is where the sprite gets drawn to the screen.
        for alien_rect in self.aliens:
            self.window.blit(self.image, alien_rect.topleft)
