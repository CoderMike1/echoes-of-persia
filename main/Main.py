import time
from player import Player
from ui import UI
import pygame

#zmienne stałe

SIZESCREEN = WIDTH, HEIGHT = 1050,700

LIGHTBLUE = pygame.color.THECOLORS['lightblue']

#ustawienia ekranu

screen = pygame.display.set_mode(SIZESCREEN)

pygame.display.set_caption("Project game")


#tworzenie obiektow gry
clock = pygame.time.Clock()
player = Player(WIDTH/2,HEIGHT-100)
ui = UI(LIGHTBLUE)

def update(keyPressed):
    #funkcja ogolna w ktorej umieszcza sie wszystkie zmiany dla wszystkich elementow gry
    #dokonujemy update gracza
    player.update(keyPressed)



    pass

def draw():
    #funkcja ogolna w ktorej umieszcza sie wszystkie narysowania wszystkich elementow gry

    # rysujemy UI, ekran elementy stale na ekranie, tlo
    ui.draw(surface=screen)

    #rysujemy gracza
    player.draw(surface=screen)



    pygame.display.update()
    pass




def main():



    # główna funkcja wykonujaca petle gry i sprawdzajaca czy gracz wylaczyl okno
    gameRun = True
    while gameRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameRun = False


        update(pygame.key.get_pressed())
        draw()
        clock.tick(60)

    pygame.quit()