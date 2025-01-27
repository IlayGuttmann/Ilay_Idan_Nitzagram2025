import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []

    def add_likes(self,likes_counter):
        if event.type == pygame.MOUSEBUTTONDOWN :
            if ((LIKE_BUTTON_X_POS == mouse_pos[0] ==
                 LIKE_BUTTON_X_POS + button_width) and
                    (LIKE_BUTTON_Y_POS == mouse_pos[1] ==
                     LIKE_BUTTON_Y_POS + button_height)):
                likes_counter += 1
                self.likes_counter = likes_counter


    def add_comment(self, comment):
        # Add comment to the post and update the comments list
        # If there are more than 10 comments, remove the oldest one
        self.comments.append(comment)
        if len(self.comments) > 10:
            self.comments.pop(0)
            self.comments_display_index = 0




    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        # Display username, location, description and likes
        username_font = pygame.font.SysFont('chalkduster.ttf', USERNAME_TEXT_SIZE)
        username_text = username_font.render(self.username, True, WHITE)
        screen.blit(username_text, (USERNAME_TEXT_X_POS, USERNAME_TEXT_Y_POS))

        location_font = pygame.font.SysFont('chalkduster.ttf', LOCATION_TEXT_SIZE)
        location_text = location_font.render(self.location, True, WHITE)
        screen.blit(location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        description_font = pygame.font.SysFont('chalkduster.ttf', DESCRIPTION_TEXT_SIZE)
        description_text = description_font.render(self.description, True, WHITE)
        return None


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))
            return None

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break




