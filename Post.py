import pygame.image
from pygame.examples.cursors import image

from constants import *
from helpers import screen,from_text_to_array,center_text


class Post:
    def __init__(self,username,location,description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []

    def add_like(self, likes_counter):
        likes_counter += 1

    def add_comment(self, text):
        self.comments.append(text)

    def display(self):
        pass

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = 0
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

# ############################################################################### #
# ############################################################################### #
class ImagePost(Post):

    def __init__(self, image , username, location, description):
        super().__init__(username, location, description)
        self.image = image
    def display(self):
        img = pygame.image.load(self.image)
        img = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))
        screen.blit(img, (POST_X_POS,POST_Y_POS))

        font = pygame.font.SysFont(FONT_NAME,UI_FONT_SIZE)
        user_text = font.render(self.username,True,(0,0,0))
        screen.blit(user_text,(USER_NAME_X_POS,USER_NAME_Y_POS))

        location_text = font.render(self.location, True, (0, 0, 0))
        screen.blit(location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        description_text = font.render(self.description, True, (0, 0, 0))
        screen.blit(description_text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

        like_text = font.render(str(self.likes_counter),True,(0,0,0))
        screen.blit(like_text, (LIKE_TEXT_X_POS,LIKE_BUTTON_Y_POS))

        self.display_comments()
########################################################################################################
########################################################################################################

class TextPost(Post):
    def __init__(self, text, text_color , text_background_col,  username, location, description):
        super().__init__( username, location, description)
        self.text = text
        self.text_color = text_color
        self.text_background_col = text_background_col

    def display(self):
        square = pygame.Rect(POST_X_POS,POST_Y_POS,POST_WIDTH,POST_HEIGHT)
        pygame.draw.rect(screen,self.text_background_col, square)

        font2 = pygame.font.SysFont(FONT_NAME,TEXT_POST_FONT_SIZE)
        user_text = font2.render(self.text,True,self.text_color)
        arr_text = from_text_to_array(self.text)
        count = 0
        for item in arr_text:
            count += 1
            text_text = font2.render(item,True,self.text_color)
            pos = center_text(len(arr_text),text_text,count)
            screen.blit(text_text,pos)

        font = pygame.font.SysFont(FONT_NAME,UI_FONT_SIZE)
        username_text = font.render(self.username,True,(0,0,0))
        screen.blit(username_text,(USER_NAME_X_POS,USER_NAME_Y_POS))

        location_text = font.render(self.location, True, (0, 0, 0))
        screen.blit(location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        description_text = font.render(self.description, True, (0, 0, 0))
        screen.blit(description_text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

        like_text = font.render(str(self.likes_counter),True,(0,0,0))
        screen.blit(like_text, (LIKE_TEXT_X_POS,LIKE_BUTTON_Y_POS))

        self.display_comments()















