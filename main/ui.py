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
    ORANGE = (245,121,20)

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
        self.pausedTicks = 0
        self.pauseStartTicks = None

    def draw(self,surface):
        keys = pygame.key.get_pressed()
        if self.game.gameStatus == 1:
            self.optionCounter +=1
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
                    #self.game.level = Level2(self.game, 21 )
                    self.game.tileHandler.loadMap(f"level{self.game.level.getLevel()}/{self.game.level.currentMap}.txt")





        elif self.game.gameStatus == 2 or self.game.gameStatus == 3:
            #rysujemy informacje o levelu
            pygame.draw.rect(surface,self.RECT_COLOR,self.rect)

            level_text = self.font.render(f"LEVEL {self.game.level.getLevel()}",True,self.BLACK)

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

            if self.game.gameStatus == 3:
                if self.pauseStartTicks is None:
                    self.pauseStartTicks = pygame.time.get_ticks()

                self.time_text = self.font.render(f"{self.minutes:02}:{self.seconds:02}", True, self.WHITE)
                surface.blit(self.time_text, (((self.game.WIDTH / 2) - (self.time_text.get_width() / 2), 45)))

                overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
                overlay.fill((128, 128, 128, 128))
                surface.blit(overlay, (0, 0))

                text = self.font.render("PAUSED!", True, self.ORANGE)
                surface.blit(text,
                             (((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 3)))

                self.optionCounter += 1

                if self.optionChoose == 1:
                    text = self.font.render("RESUME", True, self.WHITE)
                else:
                    text = self.font.render("RESUME", True, self.BLACK)
                surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 2))

                if self.optionChoose == 2:
                    text = self.font.render("EXIT", True, self.WHITE)
                else:
                    text = self.font.render("EXIT", True, self.BLACK)
                surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 1.7))

                if keys[pygame.K_DOWN] and self.optionCounter > 20:
                    self.optionCounter = 1
                    self.optionChoose += 1
                    if self.optionChoose > 2:
                        self.optionChoose = 1
                elif keys[pygame.K_UP] and self.optionCounter > 20:
                    self.optionCounter = 1
                    self.optionChoose -= 1
                    if self.optionChoose < 1:
                        self.optionChoose = 2

                if keys[pygame.K_RETURN] and self.optionCounter > 20:
                    self.optionCounter = 100
                    if self.optionChoose == 1:
                        self.game.gameStatus =2
                    elif self.optionChoose == 2:
                        pygame.quit()



            else:
                if self.pauseStartTicks is not None:
                    self.pausedTicks += pygame.time.get_ticks() - self.pauseStartTicks
                    self.pauseStartTicks = None

                currentTime = pygame.time.get_ticks() - self.startTime - self.pausedTicks
                self.seconds = (currentTime // 1000) % 60
                self.minutes = (currentTime // 1000) // 60

                self.time_text = self.font.render(f"{self.minutes:02}:{self.seconds:02}", True, self.WHITE)
                surface.blit(self.time_text, (((self.game.WIDTH / 2) - (self.time_text.get_width() / 2), 45)))




        elif self.game.gameStatus == 4:
            #win
            overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
            overlay.fill((97, 226, 0, 128))

            surface.blit(overlay, (0, 0))
            text = self.font.render("YOU WON!",True,self.WHITE)
            surface.blit(text,
                         (((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 3)))
            text = self.font.render("YOUR TIME:", True, self.WHITE)
            surface.blit(text,
                         (((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 2.5)))
            surface.blit(self.time_text, (((self.game.WIDTH / 2) - (self.time_text.get_width() / 2), self.game.HEIGHT/2)))

        elif self.game.gameStatus == 5:
            #lose
            overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
            overlay.fill((253, 6, 0, 128))

            surface.blit(overlay, (0, 0))
            text = self.font.render("YOU LOSE!", True, self.ORANGE)
            surface.blit(text,
                         (((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 3)))


            self.optionCounter +=1

            if self.optionChoose == 1:
                text = self.font.render("TRY AGAIN", True, self.WHITE)
            else:
                text = self.font.render("TRY AGAIN", True, self.BLACK)
            surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 2))

            if self.optionChoose == 2:
                text = self.font.render("EXIT", True, self.WHITE)
            else:
                text = self.font.render("EXIT", True, self.BLACK)
            surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 1.7))

            if keys[pygame.K_DOWN] and self.optionCounter > 20:
                self.optionCounter = 1
                self.optionChoose += 1
                if self.optionChoose > 2:
                    self.optionChoose = 1
            elif keys[pygame.K_UP] and self.optionCounter > 20:
                self.optionCounter = 1
                self.optionChoose -= 1
                if self.optionChoose < 1:
                    self.optionChoose = 2

            if keys[pygame.K_RETURN] and self.optionCounter > 20:
                self.optionCounter = 100
                if self.optionChoose == 1:
                    self.game.newLevel(1)
                elif self.optionChoose == 2:
                    pygame.quit()












