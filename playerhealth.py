import pygame, sys
from resources import *

# Health class 
# updateHealth to update the health
# self.hitpoints to know the hitpoint of the player
class PlayerHealth:
    def __init__(self, health):
        self.updateHealth(health)
    
    def updateHealth(self, health):
        self.hitpoints = health
        self.text = Resources.TEXT_FONT.render(self.hitpoints.__str__(), True, (255, 255, 255))

    def draw(self, window):
        rect = self.text.get_rect()
        rect.center = (40, 560)

        window.blit(self.text, rect)