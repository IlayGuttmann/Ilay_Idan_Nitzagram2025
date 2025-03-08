import pygame
from constants import *
from helpers import *
from classes.Post import Post

class TextPost(Post):

    text_color = (23, 23, 32)

    def __init__(self,username, location, description, likes_counter, comments, info = None):
        super().__init__(username, location, description, likes_counter, comments)
        self.info = info
    def add_like(self):
        super().add_like()

    def display(self):
        super().display()
        font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE - 10)

        text = font.render(self.info, True, self.text_color)
        screen.blit(text, center_text(5,text, 0))


    def display_comments(self):
        super().display_comments()