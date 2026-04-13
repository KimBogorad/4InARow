import pygame
from pygame.locals import Color

white = Color('white')
img_length = 44
img_dx = 10
img_dy = 14

empty_img = 'circle-xxl.png'


class Token():

    def __init__(self, screen, row, col, val=0):
        self.val = val
        self.image = pygame.image.load(empty_img)  # transparent
        self.image = pygame.transform.scale(self.image, (img_length, int(img_length)))
        self.image.set_colorkey(white)
        self.row = row
        self.col = col
        self.rect = self.image.get_rect()
        self.rect.y = 120 + row * (img_length + img_dy)
        self.rect.x = 117 + col * (img_length + img_dx)
        screen.blit(self.image, self.rect)

    def color_token(self, val, img=empty_img):
        self.val = val
        self.image = pygame.image.load(img)  # transparent
        self.image = pygame.transform.scale(self.image, (img_length, img_length))
        self.image.set_colorkey(white)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
