import pygame

from playerdata import PlayerData

#Create bullets class
# Player = green
# Aliens = red
class Bullet():
    def __init__(self, window):
        self.window = window
        self.height = pygame.display.get_surface().get_size()[1]
        self.bullets = []
        self.speed = 3

        self.player_color = (0,255,0) 
        self.alien_color = (255,0,0) 

    def dispose(self):
        del self.bullets[:]
        
    def create(self, x, y, direction, entity):
        self.bullets.append({"position":[x, y], "direction":direction, "entity":entity})

    def update(self, player, health, explosion, explosion_group, alien):
        for bullet in self.bullets[:]:
            # Check if bullet hit player
            if player.rect.collidepoint(bullet["position"][0], bullet["position"][1]) and bullet["entity"] == 'alien' and player.cooldown_time <= 0:
                # Give player temporary invisibility.
                player.cooldown()
                # Blow up ship animation
                explosion.create(player.rect.centerx, player.rect.centery)
                explosion_group.add(explosion)
                # Lower player health by 1.
                health.updateHealth(health.hitpoints - 1)
                # Remove all bullets.
                self.bullets = []

            # Check if bullet hit alien
            for alien_ship in alien.aliens[:]:
                if alien_ship.collidepoint(bullet["position"][0], bullet["position"][1]) and bullet["entity"] == 'player':
                    # Blow up alien ship animation
                    explosion.create(alien_ship.centerx, alien_ship.centery)
                    explosion_group.add(explosion)
                    # Delete alien
                    alien.aliens.remove(alien_ship)
                    # Delete bullet
                    self.bullets.remove(bullet)
                    # Rank up score.
                    PlayerData.CURRENT_SCORE += 20 
            
            # Update position and delete if not on screen
            if bullet["direction"] == "down":
                bullet["position"][1] += self.speed

                # Delete
                if bullet["position"][1] > self.height:
                    self.bullets.remove(bullet)
            else:
                bullet["position"][1] -= self.speed

                # Delete
                if bullet["position"][1] < -10:
                    self.bullets.remove(bullet)
            
    
            # Draw to screen.
            if bullet["entity"] == "player":
                pygame.draw.circle(self.window, self.player_color, (bullet["position"][0], bullet["position"][1]), 4)
            else:
                pygame.draw.circle(self.window, self.alien_color, (bullet["position"][0], bullet["position"][1]), 4)


#Create explosion class
class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f"img/exp{num}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.counter = 0

        
    def create(self, x, y):
        self.index = 0
        self.rect.center = [x, y]
        self.counter = 0

    def dispose(self):
        for image in self.images:
            del image
        del self.images[:]
        del self.image
    
    def update(self):
        explosion_speed = 4
        #update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        #if the animation is complete, reset the animation index
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()
