import pygame
from constants import *
from helpers import screen
from classes.Post import Post

class ImagePost(Post):

    def __init__(self,username, location, description, likes_counter, comments, info = None):
        super().__init__(username, location, description, likes_counter, comments)
        self.info = info
    def add_like(self):
        super().add_like()

    def display(self):
        super().display()

        picture = pygame.image.load(self.info)
        picture = pygame.transform.scale(picture, (POST_WIDTH,POST_HEIGHT))
        picture_sr = picture.get_rect(topleft=(POST_X_POS, POST_Y_POS))
        screen.blit(picture,picture_sr)

    def display_comments(self):
        super().display_comments()