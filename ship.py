import pygame
class Ship:
    """a class to manage th ship"""

    def __init__(self, ai_game):
        """Initializes the ship and sets it startig position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and its rect
        self.image = pygame.image.load('Images/shuttlere.bmp')
        self.rect = self.image.get_rect()

        #start new ship at the bottom the screem
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship positon based on the moving flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x
        
    
    def blitme(self):
        """Draws thw ship at its current location"""
        self.screen.blit(self.image, self.rect)