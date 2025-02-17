import pygame
from classes.Post import Post
from constants import *
from helpers import screen


class TextPost(Post):
    def __init__(self, username, location, text, color_text, color_background, color_border):
        super().__init__(username, location, text)
        self.color_text = color_text
        self.color_background = color_background
        self.color_border = color_border

    def display(self, screen):
        font = pygame.font.Font(None, 50)
        text_surface = font.render(self.description, True, BLACK)
        text_rect = text_surface.get_rect(topleft=(DESCRIPTION_TEXT_X_POS - 10, DESCRIPTION_TEXT_Y_POS - 200))

        background_rect = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.color_background, background_rect)
        pygame.draw.rect(screen, self.color_border, background_rect, 2)

        screen.blit(text_surface, text_rect)

        super().display()