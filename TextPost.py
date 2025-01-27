from helper import *
def textpost(post):
    textpost = pygame.image.load('Images/textpost.jpg')
    textpost = pygame.transform.scale(textpost, (POST_WIDTH, POST_HEIGHT))
    screen.blit(textpost, (POST_X_POS, POST_Y_POS))