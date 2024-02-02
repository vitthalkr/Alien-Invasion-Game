class Settings:
    """ A class to store all the settings"""

    def __init__(self):
        """ initializes the game settings """
        # screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (200, 200, 200)

        #ship seetings
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (56, 99, 20)
        self.bullets_allowed = 10
        