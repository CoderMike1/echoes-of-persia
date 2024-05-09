import time

import pygame

#zmienne

SIZESCREEN = WIDTH, HEIGHT = 450, 450


screen = pygame.display.set_mode(SIZESCREEN)

pygame.display.set_caption("Project game")






def main():
    gameRun = True
    while gameRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameRun = False

    pygame.quit()