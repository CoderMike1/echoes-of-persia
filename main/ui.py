import pygame,os


class UI:
    path = os.path.join(os.path.dirname(os.getcwd()), 'images', 'ui')
    BLACK = (0, 0, 0)
    RED = (255,0,0)
    RECT_COLOR = (197,167,162)
    PURPLE = (109,50,168)
    GRAY = (128,128,128)

    def __init__(self,game):
        self.game = game
        self.loadData()
        self.playerMaxLifes = 3
        self.playerLifes = self.playerMaxLifes

    def loadData(self):
        self.rect = pygame.Rect(0, 0, self.game.WIDTH, self.game.PIXEL_SIZE)
        self.font = pygame.font.SysFont("franklingothicdemi", 36)
        self.heartImage = pygame.transform.scale(pygame.image.load(os.path.join(self.path,'heart.png')).convert_alpha(),(30,35))
        self.heartRect = pygame.Rect(15,10,30,30)
        self.enemyHeartRect = pygame.Rect(self.game.WIDTH - 15,10,30,30)
        self.enemyHeartRect.right = self.game.WIDTH - 15
        self.startTime = pygame.time.get_ticks()


    def draw(self,surface):
        #rysujemy informacje o levelu
        pygame.draw.rect(surface,self.RECT_COLOR,self.rect)

        level_text = self.font.render(f"LEVEL 1",True,self.BLACK)

        surface.blit(level_text,((self.game.WIDTH/2)-(level_text.get_width()/2),5))


        #rysujemy poziom zycia
        for _ in range(self.playerLifes):
            pygame.draw.rect(surface,self.RED,self.heartRect)
            self.heartRect.x += 50
        self.heartRect.x = 15



        ##rysujemy poziom zycia przeciwnika
        for enemy in self.game.level.enemies:
            if enemy.currentMap == self.game.level.currentMap:
                for _ in range(enemy.enemyLives):
                    pygame.draw.rect(surface, self.PURPLE, self.enemyHeartRect)
                    self.enemyHeartRect.x -= 50
                self.enemyHeartRect.right = self.game.WIDTH - 15

        #rysujemy czas trwania gry
        if not self.game.gameOver:
            currentTime = pygame.time.get_ticks() - self.startTime
            self.seconds = (currentTime // 1000)%60
            self.minutes = (currentTime // 1000) //60

            time_text = self.font.render(f"{self.minutes:02}:{self.seconds:02}", True, self.BLACK)
            surface.blit(time_text, (((self.game.WIDTH / 2) - (time_text.get_width() / 2), 45)))

        else:
            time_text = self.font.render(f"{self.minutes:02}:{self.seconds:02}", True, self.BLACK)
            surface.blit(time_text, (((self.game.WIDTH / 2) - (time_text.get_width() / 2), 45)))

            overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
            overlay.fill((128,128,128,128))

            surface.blit(overlay,(0,0))






