import pygame


class TButton(object):
    def __init__(self, surface, text, font, pos):
        self.surface = surface
        self.text = text
        self.font = font
        #self.font_size = font_size
        self.pos_x, self.pos_y = pos

    def __del__(self):
        pass

    def draw(self, color):
        pygame.draw.rect(self.surface, color, [self.pos_x, self.pos_y, 100, 30])
