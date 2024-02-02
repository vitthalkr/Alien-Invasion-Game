import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    """ A class to represent aliens  """

    def __init__(self, ai_game):
        """ Initializes the alien and the starting position """
        super().__init__()
        self.screen = ai_game.screen

        #load the image and set its rect attribute.
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the exact alien horizontal position
        self.x = float(self.rect.x)
