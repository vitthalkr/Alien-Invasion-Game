import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets"""
    
    def __init__(self, ai_game):
        """ Create a bullet object at ship current position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet at rect at (0,0) and then correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet posotion as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet to the screen"""
        #Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        #Update the rect position 
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

