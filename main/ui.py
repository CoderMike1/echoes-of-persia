import pygame,os

from level import Level1,Level2,WorkingLevel
class UI:
    path = os.path.join(os.path.dirname(os.getcwd()), 'images', 'maps')
    BLACK = (0, 0, 0)
    WHITE =(255,255,255)
    RED = (255,0,0)
    RECT_COLOR = (197,167,162)
    PURPLE = (109,50,168)
    GRAY = (128,128,128)
    ORANGE = (245,121,20)
    MINT = (127, 232, 121)

    def __init__(self,game):
        self.game = game
        self.loadData()
        self.playerMaxLifes = 3
        self.playerLifes = self.playerMaxLifes

        self.optionChoose = 1
        self.optionCounter = 101

        self.chooseDifficult = False
        self.chooseOptionsTab = False
        self.chooseKeyboardControls = False
        self.chooseCredits = False

    def loadData(self):
        self.rect = pygame.Rect(0, 0, self.game.WIDTH, self.game.PIXEL_SIZE)
        self.font = pygame.font.SysFont("franklingothicdemi", 36)
        self.winfont = pygame.font.SysFont("franklingothicdemi", 75)
        self.titleFont = pygame.font.SysFont("georgia", 80)
        self.pFont = pygame.font.SysFont("franklingothicdemi",20)
        self.backgroundMenu = pygame.image.load(os.path.join(self.path, "backgroundMenu.png")).convert_alpha()
        self.backgroundMenu_x = 0
        self.backgroundMenu_velocity = 0
        self.controlKeyboardTable = pygame.image.load(os.path.join(self.path,"controlKeyboardTable.png")).convert_alpha()
        self.creditsTable = pygame.image.load(os.path.join(self.path, "creditsTable.png")).convert_alpha()
        self.heartRect = pygame.Rect(15,10,30,30)
        self.enemyHeartRect = pygame.Rect(self.game.WIDTH - 15,10,30,30)
        self.enemyHeartRect.right = self.game.WIDTH - 15
        self.startTime = pygame.time.get_ticks()
        self.pausedTicks = 0
        self.pauseStartTicks = None

    def draw(self,surface):
        keys = pygame.key.get_pressed()
        if self.game.gameStatus == 1:



            surface.blit(self.backgroundMenu, (self.backgroundMenu_x, 0))
            self.backgroundMenu_x += self.backgroundMenu_velocity
            if self.backgroundMenu_x <= -440:
                self.backgroundMenu_velocity = 1
            elif self.backgroundMenu_x >= 0:
                self.backgroundMenu_velocity = -1

            text = self.titleFont.render("ECHOES OF PERSIA", True, self.MINT)
            surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 17))

            text = self.pFont.render("Press k for Keyboard controls", True, self.RED)
            surface.blit(text, ((self.game.WIDTH / 1.2) - (text.get_width() / 2), self.game.HEIGHT / 1.1))

            text = self.pFont.render("Press c for credits", True, self.MINT)
            surface.blit(text, ((self.game.WIDTH / 9) - (text.get_width() / 2), self.game.HEIGHT / 1.1))

            self.optionCounter +=1
            if not self.chooseDifficult and not self.chooseOptionsTab and not self.chooseKeyboardControls and not self.chooseCredits:
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
                if self.optionChoose == 1:
                    text = self.font.render("START GAME",True,self.WHITE)
                else:
                    text = self.font.render("START GAME", True, self.ORANGE)
                surface.blit(text,((self.game.WIDTH/2) -(text.get_width()/2), self.game.HEIGHT/4))

                if self.optionChoose == 2:
                    text = self.font.render("OPTIONS",True,self.WHITE)
                else:
                    text = self.font.render("OPTIONS", True, self.ORANGE)
                surface.blit(text,((self.game.WIDTH/2) -(text.get_width()/2), self.game.HEIGHT/3))

                if self.optionChoose == 3:
                    text = self.font.render("QUIT",True,self.WHITE)
                else:
                    text = self.font.render("QUIT", True, self.ORANGE)
                surface.blit(text,((self.game.WIDTH/2) -(text.get_width()/2), self.game.HEIGHT/2))


                if keys[pygame.K_RETURN]:
                    self.optionCounter = 1
                    if self.optionChoose == 1:
                        self.chooseDifficult = True
                    elif self.optionChoose == 2:
                        self.chooseOptionsTab = True
                    elif self.optionChoose == 3:
                        pygame.quit()

                if keys[pygame.K_k] and self.optionCounter > 60:
                    self.optionCounter = 1
                    self.chooseKeyboardControls = True
                if keys[pygame.K_c] and self.optionCounter > 60:
                    self.optionCounter = 1
                    self.chooseCredits = True

            elif self.chooseDifficult:
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

                text = self.font.render("Choose the difficulty:",True,self.MINT)
                surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 4))

                if self.optionChoose == 1:
                    text = self.font.render("EASY", True, self.WHITE)
                else:
                    text = self.font.render("EASY", True, self.ORANGE)
                surface.blit(text, ((self.game.WIDTH / 3) - (text.get_width() / 2), self.game.HEIGHT / 3))

                if self.optionChoose == 2:
                    text = self.font.render("MEDIUM", True, self.WHITE)
                else:
                    text = self.font.render("MEDIUM", True, self.ORANGE)
                surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 3))

                if self.optionChoose == 3:
                    text = self.font.render("HARD", True, self.WHITE)
                else:
                    text = self.font.render("HARD", True, self.ORANGE)
                surface.blit(text, ((self.game.WIDTH / 1.5) - (text.get_width() / 2), self.game.HEIGHT / 3))

                if keys[pygame.K_RETURN] and self.optionCounter > 20:
                    self.game.gameStatus = 2
                    self.optionCounter = 1
                    if self.optionChoose == 1:
                        self.game.difficult = "EASY"
                    elif self.optionChoose == 2:
                        self.game.difficult = "MEDIUM"
                    elif self.optionChoose == 3:
                        self.game.difficult = "HARD"

                    self.game.level = Level1(self.game,1)
                    self.game.sounds.stopSound("menuMusic")
                    self.game.sounds.playSound("1level")
                    self.game.sounds.playSound("music")
                    self.game.tileHandler.loadMap(f"level{self.game.level.getLevel()}/{self.game.level.currentMap}.txt")
                if keys[pygame.K_ESCAPE]:
                    self.chooseDifficult = False
            elif self.chooseOptionsTab:
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

                text = self.font.render("Sound volume:",True,self.MINT)
                surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 4))

                if self.optionChoose == 1:
                    text = self.font.render("LOW", True, self.WHITE)
                else:
                    text = self.font.render("LOW", True, self.ORANGE)
                surface.blit(text, ((self.game.WIDTH / 3) - (text.get_width() / 2), self.game.HEIGHT / 3))

                if self.optionChoose == 2:
                    text = self.font.render("MEDIUM", True, self.WHITE)
                else:
                    text = self.font.render("MEDIUM", True, self.ORANGE)
                surface.blit(text, ((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 3))

                if self.optionChoose == 3:
                    text = self.font.render("HIGH", True, self.WHITE)
                else:
                    text = self.font.render("HIGH", True, self.ORANGE)
                surface.blit(text, ((self.game.WIDTH / 1.5) - (text.get_width() / 2), self.game.HEIGHT / 3))

                if keys[pygame.K_RETURN] and self.optionCounter > 20:
                    self.optionCounter = 1
                    if self.optionChoose == 1:
                        self.game.sounds.soundVolume = 0.3
                    elif self.optionChoose == 2:
                        self.game.sounds.soundVolume = 0.6
                    elif self.optionChoose == 3:
                        self.game.sounds.soundVolume = 0.9
                    self.chooseOptionsTab = False
                    self.optionChoose = 0
                if keys[pygame.K_ESCAPE]:
                    self.chooseOptionsTab = False


            elif self.chooseKeyboardControls:
                surface.blit(self.controlKeyboardTable,(0,0))
                if keys[pygame.K_k] and self.optionCounter > 20:
                    self.optionCounter = 1
                    self.chooseKeyboardControls = False

            elif self.chooseCredits:
                surface.blit(self.creditsTable,(0,0))
                if keys[pygame.K_c] and self.optionCounter > 20:
                    self.optionCounter = 1
                    self.chooseCredits = False





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
            text = self.winfont.render("YOU WON!",True,self.ORANGE)
            surface.blit(text,
                         (((self.game.WIDTH / 2) - (text.get_width() / 2), self.game.HEIGHT / 7)))
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
                self.optionCounter = 1
                if self.optionChoose == 1:
                    self.game.newLevel(1)
                elif self.optionChoose == 2:
                    pygame.quit()












