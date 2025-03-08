import pygame
from classes.Comment import Comment
from buttons import *
from classes.TextPost import TextPost
from classes.ImagePost import ImagePost
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from helpers import *

def create_Imagepost(username, location, description, likes_counter, comments, info=None):
    post = ImagePost(username, location, description, likes_counter, comments, info)
    return post

def create_Textpost(username, location, description, likes_counter, comments, info=None):
    post = TextPost(username, location, description, likes_counter, comments, info)
    return post

def create_Comm(comment):
    return Comment(comment)

comments_txt = [
    "Great post!",
    "Awesome picture!",
    "Love this!",
    "So cool!",
    "This is amazing!",
    "Wow, incredible!",
    "Nice shot!",
    "Incredible view!"
]
comms = []
for i in range(len(comments_txt)):
    comms.append(create_Comm(comments_txt[i]))

Posts = []
post1 = ImagePost("Vladimir Putin", "Russian", "we bring the boom!", 0, [], "Images/putin.jpg")
post2 = ImagePost("Josep Stalin", "Soviet Union", "Something putin will never forget", 0, [], "Images/stalin.jpg")
post3 = TextPost("Elon Musk", "Freedoom kindom", "Trump is the best", 0, [], " You need to invade gaza")
Posts = [post1, post2, post3]

def main():
    pygame.init()
    font = pygame.font.Font(None, 36)
    pygame.display.set_caption('Nitzagram')
    clock = pygame.time.Clock()

    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    running = True
    post_number = 0
    f = False
    latest_comments_check = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_in_button(click_post_button, pygame.mouse.get_pos()):
                    post_number = (post_number + 1) % len(Posts)

                if mouse_in_button(like_button, pygame.mouse.get_pos()):
                    Posts[post_number].add_like()

                if mouse_in_button(comment_button, pygame.mouse.get_pos()):
                    if f == False:
                        f = True
                    else:
                        f = False

                if mouse_in_button(view_more_comments_button, pygame.mouse.get_pos()):
                    Posts[post_number].latest_comments_show = True

            if event.type == pygame.MOUSEWHEEL:
                Posts[post_number].latest_comments_show = False
                post_number = (post_number + 1) % len(Posts)

        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        Posts[post_number].display()
        Posts[post_number].display_comments()

        if f == True:
            draw_comment_text_box()
            new_comm = read_comment_from_user()
            Posts[post_number].comments.append(create_Comm(new_comm))
            f = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

main()