from helper import *
from classes import Post

def textpost(post):
    screen.fill(BLACK)
    screen.blit(text_font.render(post.username, True, WHITE), (POST_USERNAME_X_POS, POST_USERNAME_Y_POS))
    screen.blit(text_font.render(post.location, True, WHITE), (POST_LOCATION_X_POS, POST_LOCATION_Y_POS))
    screen.blit(text_font.render(post.description, True, WHITE), (POST_DESCRIPTION_X_POS, POST_DESCRIPTION_Y_POS))
    screen.blit(text_font.render(f'Likes: {post.likes_counter}', True, WHITE), (POST_LIKE_COUNTER_X_POS, POST_LIKE_COUNTER_Y_POS))
    pygame.display.update()
    pass