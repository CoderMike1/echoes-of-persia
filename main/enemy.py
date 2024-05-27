import pygame,os,abc,math,random

class Enemy(pygame.sprite.Sprite,abc.ABC):
    path = os.path.join(os.path.dirname(os.getcwd()), 'images', 'enemy')
    ENEMY_SCALE = 3
    def __init__(self,game,lives,speed,enemyLevel,cx,cy,images,hitGapTime):
        super().__init__()
        self.game = game
        self.enemyLives = lives
        self.enemySpeed = speed
        self.images = images
        self.image = self.images[f"{enemyLevel}EnemyIdle"]
        self.direction = "right"
        self.rect = self.image.get_rect()
        self.rect.center = (cx,cy)
        self.vel_x = self.vel_y = 0
        self.enemyLevel = enemyLevel


        self.attackMode = False
        self.hit = False
        self.hitGapTime = hitGapTime



    def pLoad(self,fileName):
        i = pygame.image.load(os.path.join(self.path,fileName+".png")).convert_alpha()
        i = pygame.transform.scale(i,(i.get_width()*self.ENEMY_SCALE,i.get_height()*self.ENEMY_SCALE))

        return i


    @abc.abstractmethod
    def attacking(self):
        pass
    @abc.abstractmethod
    def defending(self):
        pass

    def patroling(self):
        distance = math.hypot(self.game.player.rect.x - self.rect.x, self.game.player.rect.y - self.rect.y)
        if distance < 250:
            self.attackMode = True
        if self.direction == "right":
            self.image = self.images[f"{self.enemyLevel}EnemyIdle"]
        elif self.direction == "left":
            self.image = pygame.transform.flip(self.images[f"{self.enemyLevel}EnemyIdle"],True,False)



    def update(self):
        self.currentLeft = self.rect.left
        self.currentRight = self.rect.right
        self.currentTop = self.rect.top
        self.currentBottom = self.rect.bottom


        self.vel_y +=1
        if self.vel_y > 10:
            self.vel_y = 10


        if self.rect.right <= self.game.player.rect.left:
            self.direction = "right"
        elif self.rect.left >= self.game.player.rect.right:
            self.direction = "left"

        if self.attackMode:
            self.attacking()
            self.defending()
        else:
            self.patroling()

        for tile in self.game.tileHandler.tileMap:
            rect_Y = pygame.Rect(self.rect.x, self.rect.y + self.vel_y,self.rect.width,self.rect.height)
            if tile.rect.colliderect(rect_Y):
                if self.vel_y >0:
                    #spada
                    self.rect.bottom = tile.rect.top
                    self.vel_y = 0
                elif self.vel_y <0:
                    #skacze
                    self.rect.top = tile.rect.bottom
                    self.vel_y = 0
            rect_X = pygame.Rect(self.rect.x+ self.vel_x,self.rect.y,self.rect.width,self.rect.height)
            if tile.rect.colliderect(rect_X):
                if self.vel_x >0:
                    self.rect.right = tile.rect.left
                    self.vel_x = 0
                elif self.vel_x < 0:
                    self.rect.left = tile.rect.right
                    self.vel_x

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


    def draw(self,surface):
        surface.blit(self.image,self.rect)

class EnemyEasy(Enemy):
    def __init__(self,game,cx,cy):
        super().__init__(game,3,2,"easy",cx,cy,self.loadImage(),200)

        self.hitCounter = self.hitGapTime + 1

    def loadImage(self):
        im = {}
        im.update({"easyEnemyIdle": self.pLoad("easyEnemyIdle")})

        im.update({"easyEnemyAttack1": self.pLoad("easyEnemyAttack1")})
        im.update({"easyEnemyAttack2": self.pLoad("easyEnemyAttack2")})
        im.update({"easyEnemyAttack3": self.pLoad("easyEnemyAttack3")})
        im.update({"easyEnemyAttack4": self.pLoad("easyEnemyAttack4")})
        im.update({"easyEnemyAttack5": self.pLoad("easyEnemyAttack5")})
        im.update({"easyEnemyAttack6": self.pLoad("easyEnemyAttack6")})
        im.update({"easyEnemyAttack7": self.pLoad("easyEnemyAttack7")})



        return im

    def attacking(self):
        if self.direction == "right":
            self.vel_x = self.enemySpeed
        elif self.direction == "left":
            self.vel_x = - self.enemySpeed

        if math.hypot(self.game.player.rect.x - self.rect.x,self.game.player.rect.y - self.rect.y) < 50:
            self.vel_x = 0
            if self.hitCounter > self.hitGapTime:
                print("hit")
                self.hitCounter = 0

            self.hitCounter +=1

        pass

    def defending(self):
        if self.attackMode and self.game.player.hit:
            print("unik!")

