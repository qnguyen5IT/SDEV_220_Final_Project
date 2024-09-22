import pygame, sys

# Health class 
# updateHealth to update the health
# self.hitpoints to know the hitpoint of the player
class PlayerHealth:
    def __init__(self, font, health):
        self.updateHealth(font, health)
    
    def updateHealth(self, font, health):
        self.hitpoints = health
        self.text = font.render(self.hitpoints.__str__(), True, (255, 255, 255))

    def draw(self, window):
        rect = self.text.get_rect()
        rect.center = (10, 850)

        window.blit(self.text, rect)

