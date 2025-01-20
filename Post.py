import pygame.image
from constants import *


class Post:
    def __init__(self,username,location,description,likes_counter,comments):
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

# ############################################################################### #
# ############################################################################### #
class ImagePost(Post):

    def __init__(self, image):
        super().__init__(self.username,self.location,self.description)
        self.image = pygame.image.load(POST_WIDTH,POST_HEIGHT)

    def display(self):


