import pygame
from constants import *
from helpers import screen

class Comment:
    def _init_(self, text):
        self.text = text

    def display(self, i):
        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        text = font.render(self.text, True, (0,0,0))
        screen.blit(text, (FIRST_COMMENT_X_POS , FIRST_COMMENT_Y_POS + COMMENT_TEXT_SIZE * i))