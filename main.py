import pygame
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from Post import *


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    posts_data_list = [
        [img1_post_path, "noam_belkin", "dimona", "give this post a like if you think messi is better", "image"],
        [img2_post_path, "omerKorin1808", "beer sheva", "love the camel and cool aid", "image"],
        [img3_post_path, "mashash", "Manchester",
         "i love big black dick and femboys", "image"],[" when life give you time you need to goon - yarin 2025",(0,0,0),(109 ,162 ,206),"yarin_pin","mashash house","IM GOONING RIGHT NOW GANG!!!!"]
    , img4_post_path,]

    posts_list= []
    for posts_data in posts_data_list:
        if posts_data[-1] == "image":
            post = ImagePost(posts_data[0], posts_data[1],posts_data[2],posts_data[3])
        else:
            post = TextPost(posts_data[0],posts_data[1],posts_data[2],posts_data[3],posts_data[4],posts_data[5])
        posts_list.append(post)
    running = True
    cur_post = posts_list[0]
    cur_post_num = 3
    start_comment = 0
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        cur_post = posts_list[cur_post_num]
        cur_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
