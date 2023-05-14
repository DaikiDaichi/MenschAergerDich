import pygame
BLACK = (0, 0, 0)


# class to calculate and display the fps
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


# class to create the background
class TBackground(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.smoothscale(self.image, (600, 600))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def __del__(self):
        pass


# open window
screen = pygame.display.set_mode((750, 600))

# window title
pygame.display.set_caption("MenschAergerDich!")


# dictionary of field coordinates
Fields = {'FIELD_1': (247, 35),
          'FIELD_2': (300, 35),
          'FIELD_3': (353, 35),
          'FIELD_4': (353, 88),
          'FIELD_5': (353, 142),
          'FIELD_6': (353, 195),
          'FIELD_7': (353, 247),
          'FIELD_8': (406, 247),
          'FIELD_9': (459, 247),
          'FIELD_10': (512, 247),
          'FIELD_11': (565, 247),
          'FIELD_12': (565, 300),
          'FIELD_13': (565, 353),
          'FIELD_14': (512, 353),
          'FIELD_15': (459, 353),
          'FIELD_16': (406, 353),
          'FIELD_17': (353, 353),
          'FIELD_18': (353, 406),
          'FIELD_19': (353, 459),
          'FIELD_20': (353, 512),
          'FIELD_21': (353, 565),
          'FIELD_22': (300, 565),
          'FIELD_23': (247, 565),
          'FIELD_24': (247, 512),
          'FIELD_25': (247, 459),
          'FIELD_26': (247, 406),
          'FIELD_27': (247, 353),
          'FIELD_28': (194, 353),
          'FIELD_29': (141, 353),
          'FIELD_30': (88, 353),
          'FIELD_31': (35, 353),
          'FIELD_32': (35, 300),
          'FIELD_33': (35, 247),
          'FIELD_34': (88, 247),
          'FIELD_35': (141, 247),
          'FIELD_36': (194, 247),
          'FIELD_37': (247, 88),
          'FIELD_38': (247, 142),
          'FIELD_39': (247, 195),
          'FIELD_40': (247, 247),

          'GREEN_S_1': (36, 35),
          'GREEN_S_2': (88, 35),
          'GREEN_S_3': (36, 89),
          'GREEN_S_4': (88, 89),

          'RED_S_1': (36, 511),
          'RED_S_2': (88, 511),
          'RED_S_3': (36, 565),
          'RED_S_4': (88, 565),

          'YELLOW_S_1': (512, 35),
          'YELLOW_S_2': (565, 35),
          'YELLOW_S_3': (512, 89),
          'YELLOW_S_4': (565, 89),

          'BLUE_S_1': (512, 511),
          'BLUE_S_2': (565, 511),
          'BLUE_S_3': (512, 565),
          'BLUE_S_4': (565, 565)
          }
