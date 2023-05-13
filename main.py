import pygame
from UI import TBackground, FPS
from dice import TDice
from Figures import TFigures
from button import TButton

# pygame initialization
pygame.init()

# used resources
Background_Img = "Aessets/Game_Field2.jpg"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (128, 0, 0)
BRIGHT_BLUE = (0, 0, 255)
BLUE = (0, 0, 128)
DARK_YELLOW = (127.5, 127.5, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
button_font = pygame.font.SysFont('Arial', 25)
button_text = button_font.render("werfen", True, WHITE)

# open window
screen = pygame.display.set_mode((750, 600))

# window title
pygame.display.set_caption("MenschAergerDich!")

spielaktiv = True

clock = pygame.time.Clock()

test_dic = {'color_1': GREEN,
            'color_2': RED
            }

Figures = {'GREEN_F1': TFigures(GREEN, [36, 35], screen, 15),
           'GREEN_F2': TFigures(GREEN, [36, 89], screen, 15),
           'GREEN_F3': TFigures(GREEN, [88, 35], screen, 15),
           'GREEN_F4': TFigures(GREEN, [88, 89], screen, 15),

           'RED_F1': TFigures(RED, [36, 511], screen, 15),
           'RED_F2': TFigures(RED, [36, 565], screen, 15),
           'RED_F3': TFigures(RED, [88, 511], screen, 15),
           'RED_F4': TFigures(RED, [88, 565], screen, 15),

           'BLUE_F1': TFigures(BLUE, [512, 511], screen, 15),
           'BLUE_F2': TFigures(BLUE, [512, 565], screen, 15),
           'BLUE_F3': TFigures(BLUE, [564, 511], screen, 15),
           'BLUE_F4': TFigures(BLUE, [564, 565], screen, 15),

           'YELLOW_F1': TFigures(DARK_YELLOW, [512, 35], screen, 15),
           'YELLOW_F2': TFigures(DARK_YELLOW, [512, 89], screen, 15),
           'YELLOW_F3': TFigures(DARK_YELLOW, [564, 35], screen, 15),
           'YELLOW_F4': TFigures(DARK_YELLOW, [564, 89], screen, 15),
           }

# objects
fps = FPS()
dice = TDice()
Background = TBackground(Background_Img, [0, 0])
dice_button = TButton(screen, 'werfen', button_font, [625, 100])

n = 'color_1'

# main loop
while spielaktiv:
    mouse_pos = pygame.mouse.get_pos()

    # user input check
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hat Maus angeklickt")

            if 625 < mouse_pos[0] < 725 and 100 < mouse_pos[1] < 130:
                print('Button was clicked')
                dice_number = dice.roll()
                print(dice_number)

                if n == 'color_1':
                    n = 'color_2'
                else:
                    n = 'color_1'

    # Spiellogik hier integrieren

    # Spielfeld löschen
    screen.fill(YELLOW)
    screen.blit(Background.image, Background.rect)

    # Spielfeld/figuren zeichnen
    for key in Figures:
        Figures[f"{key}"].draw()

    if 625 < mouse_pos[0] < 725 and 100 < mouse_pos[1] < 130:
        dice_button.draw(BLUE)

    else:
        dice_button.draw(BRIGHT_BLUE)

    screen.blit(button_text, (640, 100))
    dice_number = button_font.render(str(dice.eyes), True, BLACK)
    screen.blit(dice_number, (665, 50))

    pygame.draw.circle(screen, test_dic[n], (685, 65), 5)


    fps.render(screen)

    # Fenster aktualisieren
    pygame.display.update()

    # Refresh-time
    fps.clock.tick(60)

pygame.quit()
