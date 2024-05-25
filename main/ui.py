import pygame,os


class UI:
    path = os.path.join(os.path.dirname(os.getcwd()), 'images', 'ui')
    BLACK = (0, 0, 0)
    RED = (255,0,0)
    RECT_COLOR = (197,167,162)
    def __init__(self,game):
        self.game = game
        self.loadData()
        self.playerMaxLife = 3
        self.playerLife = self.playerMaxLife

    def loadData(self):
        self.rect = pygame.Rect(0, 0, self.game.WIDTH, self.game.PIXEL_SIZE)
        self.font = pygame.font.SysFont("franklingothicdemi", 36)
        self.heartImage = pygame.transform.scale(pygame.image.load(os.path.join(self.path,'heart.png')).convert_alpha(),(30,35))
        self.heartRect = pygame.Rect(15,10,30,30)
        self.startTime = pygame.time.get_ticks()


    def draw(self,surface):
        #rysujemy informacje o levelu
        pygame.draw.rect(surface,self.RECT_COLOR,self.rect)

        level_text = self.font.render(f"LEVEL 1",True,self.BLACK)

        surface.blit(level_text,((self.game.WIDTH/2)-(level_text.get_width()/2),5))


        #rysujemy poziom zycia
        for _ in range(self.playerLife):
            pygame.draw.rect(surface,self.RED,self.heartRect)
            self.heartRect.x += 50
        self.heartRect.x = 15

        #rysujemy czas trwania gry
        currentTime = pygame.time.get_ticks() - self.startTime
        seconds = (currentTime // 1000)%60
        minutes = (currentTime // 1000) //60


        time_text = self.font.render(f"{minutes:02}:{seconds:02}",True,self.BLACK)
        surface.blit(time_text,((self.game.WIDTH - time_text.get_width()-20,5)))


