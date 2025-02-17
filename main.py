import pygame
from Post import Post
from constants import *
from ImagePost import ImagePost
from TextPost import TextPost

def main():
    pygame.init()
    print("Pygame initialized")

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Nitzagram')
    print("Screen created")

    clock = pygame.time.Clock()

    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    print("Background image loaded successfully")

    post1 = ImagePost("Cristiano Ronaldo", "United", "", "Images/ronaldo.jpg")
    post2 = ImagePost("Erel", "Festigal", "Another great picture!", "Images/noa_kirel.jpg")
    post3 = TextPost("Nikel", "Unknown", "This is a text post!", WHITE, LIGHT_GRAY, BLACK)
    posts = [post1, post2, post3]
    print("Posts created successfully")

    current_post_index = 0
    print("Entering game loop")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event detected")
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Mouse click detected, changing post")
                    current_post_index = (current_post_index + 1) % len(posts)

        screen.fill(BLACK)
        if background:
            screen.blit(background, (0, 0))

        posts[current_post_index].display(screen)

        pygame.display.update()
        clock.tick(60)

    print("Exiting game loop")
    pygame.quit()
    print("Pygame quit")

if __name__ == "__main__":
    main()