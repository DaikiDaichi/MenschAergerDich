import pygame
from gameboard import TBackground, FPS, Fields, screen
from dice import TDice
from figures import Figures
from button import TButton
from dictionarys import *

# pygame initialization
pygame.init()

# used resources
Background_Img = "Aessets/Game_Field2.jpg"


button_font = pygame.font.SysFont('Arial', 25)
button_text = button_font.render("werfen", True, Color['WHITE'])


spielaktiv = True

clock = pygame.time.Clock()


# objects
fps = FPS()
dice = TDice()
Background = TBackground(Background_Img, [0, 0])
dice_button = TButton(screen, 'werfen', button_font, [625, 100])

feedback_color = 'BLACK'

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

                if feedback_color == 'BRIGHT_BLUE':
                    feedback_color = 'GREEN'
                elif feedback_color == 'GREEN':
                    feedback_color = 'RED'
                else:
                    feedback_color = 'BRIGHT_BLUE'

    # Spiellogik hier integrieren

    # Spielfeld löschen
    screen.fill(Color['YELLOW'])
    screen.blit(Background.image, Background.rect)

    # Spielfeld/figuren zeichnen
    for key in Fields:
        pygame.draw.circle(screen, Color['RED'], Fields[f'{key}'], 15)

    for key in Figures:
        Figures[f"{key}"].draw()

    if 625 < mouse_pos[0] < 725 and 100 < mouse_pos[1] < 130:
        dice_button.draw(Color['BLUE'])

    else:
        dice_button.draw(Color['BRIGHT_BLUE'])

    screen.blit(button_text, (640, 100))
    dice_number = button_font.render(str(dice.eyes), True, Color['BLACK'])
    screen.blit(dice_number, (665, 50))

    pygame.draw.circle(screen, Color[feedback_color], (685, 65), 5)

    fps.render(screen)

    # Fenster aktualisieren
    pygame.display.update()

    # Refresh-time
    fps.clock.tick(60)

pygame.quit()
