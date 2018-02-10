import pygame.font


class Button():
    def __init__(self, ai_settings, msg, screen):
        """Initailize buttton"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set button dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = 0, 255, 0
        self.text_color = 255, 255, 255
        self.font = pygame.font.SysFont(None, 48)

        # Build button rect obj and centre it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The message 
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into an image and center it on button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect() 
        self.msg_image_rect.center = self.rect.center 

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
