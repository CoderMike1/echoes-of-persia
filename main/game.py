import time

import pygame
from player import Player
from tileHandler import TileHandler
from level import Level1,Level2
from ui import UI
from sound import Sound
class Game:
    LIGHTBLUE = pygame.color.THECOLORS['lightblue']
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Project game")
        self.WIDTH = 1056
        self.HEIGHT = 672
        self.PIXEL_SIZE = 48
        self.FPS = 60
        self.window = pygame.display.set_mode((self.WIDTH,self.HEIGHT))

        pygame.mouse.set_visible(False)


        # 1.txt - Menu , 2 - Gra , 3 - Pauza 4 - Wygrana 5-Porazka
        self.gameStatus = 1
        self.difficult = None

        self.sounds = Sound()
        self.sounds.playSound("menuMusic")

        self.gameOver = False

        #inicjalizacja obiektow
        self.player = Player(self,11*48,13*48)

        self.level = None


        self.tileHandler = TileHandler(self)


        self.ui = UI(self)

    def newLevel(self,level):
        if level == 1:
            self.sounds.playSound("1level")
            self.gameStatus = 2
            self.gameOver = False
            self.ui.playerLifes = self.ui.playerMaxLifes
            self.ui.startTime = pygame.time.get_ticks()
            del self.level, self.player
            self.level = Level1(self, 1)
            self.player = Player(self, 11 * 48, 13 * 48)
            self.tileHandler.loadMap(f"level{self.level.getLevel()}/{self.level.currentMap}.txt")
        elif level == 2:
            del self.level, self.player
            self.sounds.stopSound("music")
            self.sounds.playSound("nextLevel")
            time.sleep(10)
            self.sounds.playSound("1level")
            self.sounds.playSound("music2")
            self.level = Level2(self,1)
            self.player = Player(self,3*48,8*48)
            self.tileHandler.loadMap(f"level{self.level.getLevel()}/{self.level.currentMap}.txt")
        elif level == 3:
            self.sounds.stopSound("music")
            self.sounds.playSound("gamewin")
            self.gameStatus = 4

    def draw(self):
        if self.gameStatus == 2 or self.gameStatus == 4 or self.gameStatus ==5 or self.gameStatus == 3:
            # rysujemy mape
            self.tileHandler.draw(self.window)

            # rysujemy drzwi
            if self.level.door.currentMap == self.level.currentMap:
                self.level.door.draw(self.window)

            #rysujemy gracza
            self.player.draw(self.window)


            # rysujemy rzeczy na levelu
            self.level.draw(self.window)

            #rysujemy statystyki
            self.ui.draw(self.window)
        elif self.gameStatus == 1:
            # rysujemy statystyki
            self.ui.draw(self.window)


        pygame.display.flip()



    def update(self):
        if self.gameOver:
            self.gameStatus = 5


        if self.gameStatus == 2:
            #update gracza
            self.player.update()

            #update mapy
            self.tileHandler.update()

            self.level.update(self.level.getLevel())


    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.gameStatus == 2:
                            self.gameStatus = 3
                        elif self.gameStatus == 3:
                            self.gameStatus = 2

            self.update()
            self.draw()

        pygame.quit()


