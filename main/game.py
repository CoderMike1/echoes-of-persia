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

        self.sounds = Sound()

        self.gameOver = False

        #inicjalizacja obiektow
        self.player = Player(self,1*48,14*48)

        #self.level = Level1(self,10)
        self.level = WorkingLevel(self,11)

        self.tileHandler = TileHandler(self)

        #self.tileHandler.loadMap("level1/map11.txt")
        self.tileHandler.loadMap(f"level{self.level.getLevel()}/map{self.level.currentMap}.txt")

        self.ui = UI(self)



    def draw(self):
        # rysujemy mape
        self.tileHandler.draw(self.window)

        #rysujemy gracza
        self.player.draw(self.window)



        # rysujemy rzeczy na levelu
        self.level.draw(self.window)


        #rysujemy statystyki
        self.ui.draw(self.window)





        pygame.display.flip()



    def update(self):

        #update gracza
        self.player.update()

        #update mapy
        self.tileHandler.update()

        self.level.update(self.level.getLevel())


        pass

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

            self.update()
            self.draw()

        pygame.quit()


