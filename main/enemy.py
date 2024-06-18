import pygame,os,abc,math,random

class Enemy(pygame.sprite.Sprite,abc.ABC):
    path = os.path.join(os.path.dirname(os.getcwd()), 'images', 'enemy')
    ENEMY_SCALE = 3
    def __init__(self,game,lives,speed,enemyLevel,cx,cy,images,hitGapTime,currentMap):
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
        self.currentMap = currentMap

        self.collisionLeft = False
        self.collisionRight = False


        #zmienne
        self.attackMode = False
        self.attackCounter = 1

        self.hitMode = False
        self.hitCounter = 1
        self.hitGap = hitGapTime
        self.hitGapCounter = hitGapTime+1
        self.hitSoundFlag = False

        self.defendMode = False
        self.enemyDefendFlag = False

        self.getHitCounter = 0

        self.deadCounter = 1
        self.isDead = False
        self.deadSoundFlag = False

        self.isSpeared = False
        self.bladeX = None
        self.spearedSoundFlag = False



    @abc.abstractmethod
    def loadImage(self):
        pass
    def pLoad(self,fileName):
        i = pygame.image.load(os.path.join(self.path,fileName+".png")).convert_alpha()
        i = pygame.transform.scale(i,(i.get_width()*self.ENEMY_SCALE,i.get_height()*self.ENEMY_SCALE))

        return i

    def checkDistance(self):
        if self.direction == "right":
            return math.hypot(self.game.player.rect.left - self.rect.right, self.game.player.rect.y - self.rect.y)
        elif self.direction == "left":
            return math.hypot(self.game.player.rect.right - self.rect.left, self.game.player.rect.y - self.rect.y)

    def attacking(self):
        if self.defendMode:
            if self.direction == "right":
                self.image = self.images[f"{self.enemyLevel}EnemyDefend"]
                self.rect = self.image.get_rect(topleft=(self.currentLeft,self.currentTop))
            elif self.direction == "left":
                self.image = pygame.transform.flip(self.images[f"{self.enemyLevel}EnemyDefend"],True,False)
                self.rect = self.image.get_rect(topright=(self.currentRight,self.currentTop))
        else:
            distance = self.checkDistance()
            if self.rect.right < self.game.player.rect.left:
                # obracamy sie w prawa strone
                self.direction = "right"
            elif self.rect.left > self.game.player.rect.right:
                # obracamy sie w lewa strone
                self.direction = "left"
            if self.hitMode and self.hitGapCounter > self.hitGap:
                self.hitting()
            elif self.hitMode and distance < 50:
                self.hitGapCounter +=1
                if self.direction == "right":
                    self.vel_x = self.enemySpeed
                    self.image = self.images[f"{self.enemyLevel}EnemyAttack1"]
                    if self.collisionLeft:
                        self.rect = self.image.get_rect(topleft=(self.currentLeft, self.currentTop))
                    else:
                        self.rect = self.image.get_rect(topright=(self.currentRight, self.currentTop))
                elif self.direction == "left":
                    self.vel_x = -self.enemySpeed
                    self.image = pygame.transform.flip(self.images[f"{self.enemyLevel}EnemyAttack1"],True,False)
                    if self.collisionRight:
                        self.rect = self.image.get_rect(topright=(self.currentRight, self.currentTop))
                    else:
                        self.rect = self.image.get_rect(topleft=(self.currentLeft, self.currentTop))
            else:
                if self.direction == "right" and not self.collisionLeft:
                    self.attackCounter += 0.1
                    if self.attackCounter > 5:
                        self.attackCounter = 2
                    self.vel_x = self.enemySpeed
                    self.image = self.images[f"{self.enemyLevel}EnemyAttack{int(self.attackCounter)}"]
                    self.rect = self.image.get_rect(topleft=(self.currentLeft,self.currentTop))
                elif self.collisionLeft:
                    self.image = self.images[f"{self.enemyLevel}EnemyAttack1"]
                    self.rect = self.image.get_rect(topleft=(self.currentLeft, self.currentTop))
                elif self.direction == "left" and not self.collisionRight:
                    self.attackCounter += 0.1
                    if self.attackCounter > 5:
                        self.attackCounter = 2
                    self.vel_x = -self.enemySpeed
                    self.image = pygame.transform.flip(self.images[f"{self.enemyLevel}EnemyAttack{int(self.attackCounter)}"],True,False)
                    self.rect = self.image.get_rect(topright=(self.currentRight,self.currentTop))
                elif self.collisionRight:
                    self.image = pygame.transform.flip(
                        self.images[f"{self.enemyLevel}EnemyAttack1"], True, False)
                    self.rect = self.image.get_rect(topright=(self.currentRight, self.currentTop))

    def getHit(self):
        self.getHitCounter -=1
        if self.direction == "right":
            self.image = self.images[f"{self.enemyLevel}EnemyGetHit"]
            self.rect = self.image.get_rect(topleft=(self.currentLeft,self.currentTop))
        elif self.direction == "left":
            self.image = pygame.transform.flip(self.images[f"{self.enemyLevel}EnemyGetHit"],True,False)
            self.rect = self.image.get_rect(topright=(self.currentRight,self.currentTop))

    def hitting(self):
        distance = self.checkDistance()
        self.hitCounter += 0.1
        if self.hitCounter > 5:
            self.hitCounter = 1
            self.hitMode = False
            self.hitGapCounter = 0
            self.hitSoundFlag = False
            if distance < 50 and not self.game.player.defend:
                self.game.ui.playerLifes -=1
                self.game.player.getHitCounter = 20
                if not self.hitSoundFlag:
                    self.game.sounds.playSound("playerGetDamage")
                    self.hitSoundFlag = True
        if distance <50 and self.game.player.defend and self.hitCounter>1:
            if not self.hitSoundFlag:
                self.game.sounds.playSound("swordHit")
                self.hitSoundFlag = True

        if self.direction == "right":
            self.vel_x = self.enemySpeed
            self.image = self.images[f"{self.enemyLevel}EnemyHit{int(self.hitCounter)}"]
            if self.collisionLeft:
                self.rect = self.image.get_rect(topleft=(self.currentLeft, self.currentTop))
            else:
                self.rect = self.image.get_rect(topright=(self.currentRight, self.currentTop))
        elif self.direction == "left":
            self.vel_x = -self.enemySpeed
            self.image = pygame.transform.flip(self.images[f"{self.enemyLevel}EnemyHit{int(self.hitCounter)}"],
                                               True, False)
            if self.collisionRight:
                self.rect = self.image.get_rect(topright=(self.currentRight, self.currentTop))
            else:
                self.rect = self.image.get_rect(topleft=(self.currentLeft, self.currentTop))


    def patroling(self):
        if self.rect.left >= self.game.player.rect.left:
            #obracamy sie w lewa strone
            self.direction = "left"
            self.image = pygame.transform.flip(self.images[f"{self.enemyLevel}EnemyIdle"],True,False)
            self.rect = self.image.get_rect(topleft=(self.currentLeft,self.currentTop))
        elif self.rect.right <= self.game.player.rect.right:
            #obracamy sie w prawa strone
            self.direction = "right"
            self.image = self.images[f"{self.enemyLevel}EnemyIdle"]
            self.rect = self.image.get_rect(topright=(self.currentRight,self.currentTop))

        distance = self.checkDistance()
        if distance < 250:
            self.attackMode = True

    def dead(self):
        self.isDead = True

        self.deadCounter += 0.1
        if self.deadCounter > 8:
            self.deadCounter = 7
            if not self.deadSoundFlag:
                self.game.sounds.playSound("enemyDead")
                self.deadSoundFlag = True

        if self.direction == "right":
            self.image = self.images[f"{self.enemyLevel}EnemyDying{int(self.deadCounter)}"]
            self.rect = self.image.get_rect(topleft=(self.currentLeft,self.currentTop))
        elif self.direction == "left":
            self.image = pygame.transform.flip(self.images[f"{self.enemyLevel}EnemyDying{int(self.deadCounter)}"],True,False)
            self.rect = self.image.get_rect(topright=(self.currentRight,self.currentTop))


    def speared(self):
        self.isDead = self.isSpeared = True
        if not self.spearedSoundFlag:
            self.spearedSoundFlag = True
            self.game.sounds.playSound("stabbed")
        self.enemyLives = 0
        if self.direction == "right":
            self.image = self.images[f"{self.enemyLevel}EnemySpeared"]
            self.rect = self.image.get_rect(topleft=(self.bladeX,self.currentTop))
        elif self.direction == "left":
            self.image = pygame.transform.flip(self.images[f"{self.enemyLevel}EnemySpeared"],True,False)
            self.rect = self.image.get_rect(topright=(self.bladeX,self.currentTop))

    def update(self):
        self.currentLeft = self.rect.left
        self.currentRight = self.rect.right
        self.currentTop = self.rect.top
        self.currentBottom = self.rect.bottom

        self.vel_y +=1
        if self.vel_y > 10:
            self.vel_y = 10

        if self.enemyLives < 1 and not self.isSpeared:
            self.dead()
        elif self.enemyLives <1 and self.isSpeared:
            self.speared()
        else:
            if self.getHitCounter >0:
                self.getHit()
            else:
                if self.game.player.hit:
                    if self.enemyDefendFlag:
                        pass
                    else:
                        self.enemyDefendFlag = True
                        self.defendMode = random.choice([True,False,True])
                else:
                    self.defendMode = False
                    self.enemyDefendFlag = False

                #domyslnie patroluje
                if self.attackMode and not self.game.player.isDead:
                    self.attacking()
                else:
                    self.patroling()

        #wykrywamy czy enemy przechodzi do innej klatki mapy
        if self.rect.left < 0:
            self.currentMap -=1
        if self.rect.right > self.game.WIDTH:
            self.currentMap +=1

        self.collisionLeft = self.collisionRight = False

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
                    self.collisionLeft = True
                    self.collisionRight = False
                    self.rect.right = tile.rect.left
                    self.vel_x = 0
                elif self.vel_x < 0:
                    self.collisionRight = True
                    self.collisionLeft = False
                    self.rect.left = tile.rect.right
                    self.vel_x = 0

        #kolizja z graczem
        if self.game.player.rect.colliderect((self.rect.x + self.vel_x,self.rect.y,self.rect.width,self.rect.height)):
            if self.vel_x > 0:
                self.rect.right = self.game.player.rect.left
                self.vel_x = 0
                self.hitMode = True
            elif self.vel_x < 0:
                self.rect.left = self.game.player.rect.right
                self.vel_x = 0
                self.hitMode = True
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


    def draw(self,surface):
        #pygame.draw.rect(surface,(0,0,0,0),self.rect)
        surface.blit(self.image,self.rect)

class EnemyEasy(Enemy):
    def __init__(self,game,cx,cy,currentMap):
        lives = 3
        speed = 2
        enemyLevel = "easy"
        hitGapTime = 200
        super().__init__(game,lives,speed,enemyLevel,cx,cy,self.loadImage(),hitGapTime,currentMap)
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
        im.update({"easyEnemyAttack8": self.pLoad("easyEnemyAttack8")})

        im.update({"easyEnemyDefend": self.pLoad("easyEnemyDefend")})

        im.update({"easyEnemyHit1": self.pLoad("easyEnemyHit1")})
        im.update({"easyEnemyHit2": self.pLoad("easyEnemyHit2")})
        im.update({"easyEnemyHit3": self.pLoad("easyEnemyHit3")})
        im.update({"easyEnemyHit4": self.pLoad("easyEnemyHit4")})

        im.update({"easyEnemyGetHit": self.pLoad("easyEnemyGetHit")})

        im.update({"easyEnemyDying1": self.pLoad("easyEnemyDying1")})
        im.update({"easyEnemyDying2": self.pLoad("easyEnemyDying2")})
        im.update({"easyEnemyDying3": self.pLoad("easyEnemyDying3")})
        im.update({"easyEnemyDying4": self.pLoad("easyEnemyDying4")})
        im.update({"easyEnemyDying5": self.pLoad("easyEnemyDying5")})
        im.update({"easyEnemyDying6": self.pLoad("easyEnemyDying6")})
        im.update({"easyEnemyDying7": self.pLoad("easyEnemyDying7")})

        im.update({"easyEnemySpeared": self.pLoad("easyEnemySpeared")})

        return im


class EnemyMedium(Enemy):
    def __init__(self,game,cx,cy,currentMap):
        lives = 4
        speed = 3
        enemyLevel="medium"
        hitGapTime = 150
        super().__init__(game,lives,speed,enemyLevel,cx,cy,self.loadImage(),hitGapTime,currentMap)

    def loadImage(self):
        im = {}
        im.update({"mediumEnemyIdle": self.pLoad("mediumEnemyIdle")})

        im.update({"mediumEnemyAttack1": self.pLoad("mediumEnemyAttack1")})
        im.update({"mediumEnemyAttack2": self.pLoad("mediumEnemyAttack2")})
        im.update({"mediumEnemyAttack3": self.pLoad("mediumEnemyAttack3")})
        im.update({"mediumEnemyAttack4": self.pLoad("mediumEnemyAttack4")})
        im.update({"mediumEnemyAttack5": self.pLoad("mediumEnemyAttack5")})
        im.update({"mediumEnemyAttack6": self.pLoad("mediumEnemyAttack6")})
        im.update({"mediumEnemyAttack7": self.pLoad("mediumEnemyAttack7")})
        im.update({"mediumEnemyAttack8": self.pLoad("mediumEnemyAttack8")})

        im.update({"mediumEnemyDefend": self.pLoad("mediumEnemyDefend")})

        im.update({"mediumEnemyHit1": self.pLoad("mediumEnemyHit1")})
        im.update({"mediumEnemyHit2": self.pLoad("mediumEnemyHit2")})
        im.update({"mediumEnemyHit3": self.pLoad("mediumEnemyHit3")})
        im.update({"mediumEnemyHit4": self.pLoad("mediumEnemyHit4")})

        im.update({"mediumEnemyGetHit": self.pLoad("mediumEnemyGetHit")})

        im.update({"mediumEnemyDying1": self.pLoad("mediumEnemyDying1")})
        im.update({"mediumEnemyDying2": self.pLoad("mediumEnemyDying2")})
        im.update({"mediumEnemyDying3": self.pLoad("mediumEnemyDying3")})
        im.update({"mediumEnemyDying4": self.pLoad("mediumEnemyDying4")})
        im.update({"mediumEnemyDying5": self.pLoad("mediumEnemyDying5")})
        im.update({"mediumEnemyDying6": self.pLoad("mediumEnemyDying6")})
        im.update({"mediumEnemyDying7": self.pLoad("mediumEnemyDying7")})

        im.update({"mediumEnemySpeared": self.pLoad("mediumEnemySpeared")})

        return im

class EnemyHard(Enemy):
    def __init__(self,game,cx,cy,currentMap):
        lives = 5
        speed = 2.5
        enemyLevel = "hard"
        hitGapTime = 100
        super().__init__(game,lives,speed,enemyLevel,cx,cy,self.loadImage(),hitGapTime,currentMap)

    def loadImage(self):
        im = {}
        im.update({"hardEnemyIdle": self.pLoad("hardEnemyIdle")})

        im.update({"hardEnemyAttack1": self.pLoad("hardEnemyAttack1")})
        im.update({"hardEnemyAttack2": self.pLoad("hardEnemyAttack2")})
        im.update({"hardEnemyAttack3": self.pLoad("hardEnemyAttack3")})
        im.update({"hardEnemyAttack4": self.pLoad("hardEnemyAttack4")})
        im.update({"hardEnemyAttack5": self.pLoad("hardEnemyAttack5")})
        im.update({"hardEnemyAttack6": self.pLoad("hardEnemyAttack6")})
        im.update({"hardEnemyAttack7": self.pLoad("hardEnemyAttack7")})
        im.update({"hardEnemyAttack8": self.pLoad("hardEnemyAttack8")})

        im.update({"hardEnemyDefend": self.pLoad("hardEnemyDefend")})

        im.update({"hardEnemyHit1": self.pLoad("hardEnemyHit1")})
        im.update({"hardEnemyHit2": self.pLoad("hardEnemyHit2")})
        im.update({"hardEnemyHit3": self.pLoad("hardEnemyHit3")})
        im.update({"hardEnemyHit4": self.pLoad("hardEnemyHit4")})

        im.update({"hardEnemyGetHit": self.pLoad("hardEnemyGetHit")})

        im.update({"hardEnemyDying1": self.pLoad("hardEnemyDying1")})
        im.update({"hardEnemyDying2": self.pLoad("hardEnemyDying2")})
        im.update({"hardEnemyDying3": self.pLoad("hardEnemyDying3")})
        im.update({"hardEnemyDying4": self.pLoad("hardEnemyDying4")})
        im.update({"hardEnemyDying5": self.pLoad("hardEnemyDying5")})
        im.update({"hardEnemyDying6": self.pLoad("hardEnemyDying6")})
        im.update({"hardEnemyDying7": self.pLoad("hardEnemyDying7")})

        im.update({"hardEnemySpeared": self.pLoad("hardEnemySpeared")})

        return im