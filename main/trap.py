import pygame,abc,os

class Trap(abc.ABC):
    path = os.path.join(os.path.dirname(os.getcwd()), 'images', 'trap')
    TRAP_SCALE = 3
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def loadImage(self):
        pass

    def pLoad(self, fileName):
        i = pygame.image.load(os.path.join(self.path, fileName + ".png")).convert_alpha()
        i = pygame.transform.scale(i, (i.get_width() * self.TRAP_SCALE, i.get_height() * self.TRAP_SCALE))
        return i
    @abc.abstractmethod
    def draw(self,surface):
        pass

    @abc.abstractmethod
    def update(self):
        pass



class Blades(pygame.sprite.Sprite,Trap):
    def __init__(self,game,pX,pY):
        super().__init__()

        self.game = game
        self.images = self.loadImage()
        self.image = self.images["blade1"]
        self.rect = self.image.get_rect()
        self.rect.center = (pX,pY)

        self.hitMode = False
        self.hitCounter = 1
        self.gapTime = 150
        self.gapTimeCounter = self.gapTime +1

    def loadImage(self):
        im = {}
        im.update({"blade1": self.pLoad("blade1")})
        im.update({"blade2": self.pLoad("blade2")})
        im.update({"blade3": self.pLoad("blade3")})
        im.update({"blade4": self.pLoad("blade4")})
        return im


    def pulling(self):
        self.hitCounter += 0.1
        if self.hitCounter > 5:
            self.hitCounter = 4
            self.hitMode = True
            self.gapTimeCounter = 0
        self.image = self.images[f"blade{int(self.hitCounter)}"]
        self.rect = self.image.get_rect(bottomleft=(self.currentLeft,self.currentBottom))

    def hiding(self):
        self.hitCounter -= 0.1
        if self.hitCounter < 1:
            self.hitCounter = 1
            self.hitMode = False
            self.gapTimeCounter = 0
        self.image = self.images[f"blade{int(self.hitCounter)}"]
        self.rect = self.image.get_rect(bottomleft=(self.currentLeft, self.currentBottom))

    def update(self):
        self.currentBottom = self.rect.bottom
        self.currentLeft = self.rect.left
        if not self.game.gameOver:
            if self.gapTimeCounter > self.gapTime:
                if self.hitMode:
                    self.hiding()
                else:
                    self.pulling()

            self.gapTimeCounter +=1

            if self.rect.colliderect(self.game.player.rect) and self.hitMode:
                self.game.player.speared()



    def draw(self,surface):
        #pygame.draw.rect(surface,(0,0,0,0),self.rect)
        surface.blit(self.image,self.rect)

