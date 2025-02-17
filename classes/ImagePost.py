import pygame
from classes.Post import Post
from constants import *
from helpers import screen

class ImagePost(Post):
    def __init__(self, username, location, description, image_path):
        super().__init__(username, location, description)


        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))
        except pygame.error:
            print(f"Error: Unable to load image {image_path}")
            self.image = None

    def display(self, screen):
        if self.image:
            screen.blit(self.image, (POST_X_POS, POST_Y_POS))

        pygame.draw.rect(screen, BLACK, (POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT), 2)


        super().display()
