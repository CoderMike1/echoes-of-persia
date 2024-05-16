import pygame
from player import Player
from tileHandler import TileHandler
class Game:
    LIGHTBLUE = pygame.color.THECOLORS['lightblue']
    def __init__(self):
        pygame.display.init()
        pygame.display.set_caption("Project game")
        self.WIDTH = 1056
        self.HEIGHT = 672
        self.PIXEL_SIZE = 48
        self.FPS = 60
        self.window = pygame.display.set_mode((self.WIDTH,self.HEIGHT))

        #inicjalizacja obiektow
        self.player = Player(self,100,100)

        self.tileHandler = TileHandler(self)
        self.tileHandler.loadMap("map1.txt")

    def draw(self):
        self.window.fill(self.LIGHTBLUE)

        #rysujemy gracza
        self.player.draw(self.window)

        #rysujemy mape
        self.tileHandler.draw(self.window)


        pygame.display.flip()



    def update(self):

        #update gracza
        self.player.update()

        #update mapy
        self.tileHandler.update()


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


