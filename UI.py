import pygame
BLACK = (0, 0 ,0)


class FPS(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, BLACK)

    def __del__(self):
        pass

    def render(self, display):
        self.text = self.font.render(str(round(self.clock.get_fps(), 1)), True, BLACK)
        display.blit(self.text, (700, 0))


class TBackground(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.smoothscale(self.image, (600, 600))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def __del__(self):
        pass