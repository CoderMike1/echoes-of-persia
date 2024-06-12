import pygame
from player import Player
from tileHandler import TileHandler
from level import Level1,Level2,WorkingLevel
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


        # 1.txt - Menu , 2 - Gra , 3 - Pauza
        self.gameStatus = 1
        self.difficult = None

        self.sounds = Sound()

        self.gameOver = False

        #inicjalizacja obiektow
        self.player = Player(self,11*48,13*48)

        #self.level = Level1(self,3)
        self.level = None
        #self.level = WorkingLevel(self,11)

        self.tileHandler = TileHandler(self)

        #self.tileHandler.loadMap("level1/map11.txt")
        #self.tileHandler.loadMap(f"level{self.level.getLevel()}/{self.level.currentMap}.txt")

        self.ui = UI(self)



    def draw(self):
        if self.gameStatus == 2:
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
                        running = False

            self.update()
            self.draw()

        pygame.quit()


