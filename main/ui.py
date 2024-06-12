import pygame,os

from level import Level1,Level2,WorkingLevel
class UI:
    path = os.path.join(os.path.dirname(os.getcwd()), 'images', 'ui')
    BLACK = (0, 0, 0)
    WHITE =(255,255,255)
    RED = (255,0,0)
    RECT_COLOR = (197,167,162)
    PURPLE = (109,50,168)
    GRAY = (128,128,128)

    def __init__(self,game):
        self.game = game
        self.loadData()
        self.playerMaxLifes = 3
        self.playerLifes = self.playerMaxLifes

        self.optionChoose = 1
        self.optionCounter = 101

        self.chooseDifficult = False

    def loadData(self):
        self.rect = pygame.Rect(0, 0, self.game.WIDTH, self.game.PIXEL_SIZE)
        self.font = pygame.font.SysFont("franklingothicdemi", 36)
        self.heartRect = pygame.Rect(15,10,30,30)
        self.enemyHeartRect = pygame.Rect(self.game.WIDTH - 15,10,30,30)
        self.enemyHeartRect.right = self.game.WIDTH - 15
        self.startTime = pygame.time.get_ticks()


    def draw(self,surface):
        if self.game.gameStatus == 1:



            self.optionCounter +=1
            keys = pygame.key.get_pressed()
            if not self.chooseDifficult:

                if keys[pygame.K_DOWN] and self.optionCounter > 20:
                    self.optionCounter = 1
                    self.optionChoose +=1
                    if self.optionChoose >3:
                        self.optionChoose = 1
                elif keys[pygame.K_UP] and self.optionCounter > 20:
                    self.optionCounter = 1
                    self.optionChoose -=1
                    if self.optionChoose <1:
                        self.optionChoose = 3


                surface.fill(self.PURPLE)
                if self.optionChoose == 1:
                    text = self.font.render("START GAME",True,self.WHITE)
                else:
                    text = self.font.render("START GAME", True, self.BLACK)
                surface.blit(text,((self.game.WIDTH/2) -(text.get_width()/2), self.game.HEIGHT/4))

                if self.optionChoose == 2:
                    text = self.font.render("OPTIONS",True,self.WHITE)
                else:
                    text = self.font.render("OPTIONS", True, self.BLACK)
                surface.blit(text,((self.game.WIDTH/2) -(text.get_width()/2), self.game.HEIGHT/3))

                if self.optionChoose == 3:
                    text = self.font.render("QUIT",True,self.WHITE)
                else:
                    text = self.font.render("QUIT", True, self.BLACK)
                surface.blit(text,((self.game.WIDTH/2) -(text.get_width()/2), self.game.HEIGHT/2))


                if keys[pygame.K_RETURN]:
                    self.optionCounter = 1
                    if self.optionChoose == 1:
                        self.chooseDifficult = True
                    elif self.optionChoose == 2:
                        pass
                    elif self.optionChoose == 3:
                        pygame.quit()

            else:
                if keys[pygame.K_RIGHT] and self.optionCounter > 20:
                    self.optionCounter = 1
                    self.optionChoose += 1
                    if self.optionChoose > 3:
                        self.optionChoose = 1
                elif keys[pygame.K_LEFT] and self.optionCounter > 20:
                    self.optionCounter = 1
                    self.optionChoose -= 1
                    if self.optionChoose < 1:
                        self.optionChoose = 3

                surface.fill(self.PURPLE)
                text = self.font.render("Choose the difficulty:",True,self.BLACK)
                surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 4))

                if self.optionChoose == 1:
                    text = self.font.render("EASY", True, self.WHITE)
                else:
                    text = self.font.render("EASY", True, self.BLACK)
                surface.blit(text, ((self.game.WIDTH / 3) - (text.get_width() / 2), self.game.HEIGHT / 3))

                if self.optionChoose == 2:
                    text = self.font.render("MEDIUM", True, self.WHITE)
                else:
                    text = self.font.render("MEDIUM", True, self.BLACK)
                surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 3))

                if self.optionChoose == 3:
                    text = self.font.render("HARD", True, self.WHITE)
                else:
                    text = self.font.render("HARD", True, self.BLACK)
                surface.blit(text, ((self.game.WIDTH / 1.5) - (text.get_width() / 2), self.game.HEIGHT / 3))

                if keys[pygame.K_RETURN] and self.optionCounter > 20:
                    self.game.gameStatus = 2
                    if self.optionChoose == 1:
                        self.game.difficult = "EASY"
                    elif self.optionChoose == 2:
                        self.game.difficult = "MEDIUM"
                    elif self.optionChoose == 3:
                        self.game.difficult = "HARD"

                    self.game.level = Level1(self.game,1)
                    self.game.tileHandler.loadMap(f"level{self.game.level.getLevel()}/{self.game.level.currentMap}.txt")





        elif self.game.gameStatus == 2:
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

                time_text = self.font.render(f"{self.minutes:02}:{self.seconds:02}", True, self.WHITE)
                surface.blit(time_text, (((self.game.WIDTH / 2) - (time_text.get_width() / 2), 45)))

            else:
                time_text = self.font.render(f"{self.minutes:02}:{self.seconds:02}", True, self.WHITE)
                surface.blit(time_text, (((self.game.WIDTH / 2) - (time_text.get_width() / 2), 45)))

                overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
                overlay.fill((128,128,128,128))

                surface.blit(overlay,(0,0))






