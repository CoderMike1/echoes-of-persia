import pygame
from player import Player
class Game:
    LIGHTBLUE = pygame.color.THECOLORS['lightblue']
    def __init__(self):
        pygame.display.init()
        pygame.display.set_caption("Project game")
        self.WIDTH = 1056
        self.HEIGHT = 672
        self.FPS = 60
        self.window = pygame.display.set_mode((self.WIDTH,self.HEIGHT))

        #inicjalizacja obiektow
        self.player = Player(self,100,self.HEIGHT-100)

    def draw(self):
        self.window.fill(self.LIGHTBLUE)

        #rysujemy gracza
        self.player.draw(self.window)


        pygame.display.update()


        pass

    def update(self):

        #update gracza
        self.player.update()


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


