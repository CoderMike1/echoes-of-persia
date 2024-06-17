import time

import pygame,os,math
from level import Level1,Level2
class Player(pygame.sprite.Sprite):
    path = os.path.join(os.path.dirname(os.getcwd()), 'images','player')
    PLAYER_WIDTH = 15
    PLAYER_HEIGHT = 50
    PLAYER_SCALE = 3
    SPEED = 5
    GRAVITY = 1
    BLACK = (0,0,0)
    def __init__(self,game,x,y):
        super().__init__()
        self.game = game
        self.images = self.loadImages()
        self.image = self.images['idle1']
        self.rect = self.image.get_rect()
        self.rect.center = x,y
        self.vel_y = 0
        self.vel_x = 0
        self.jump = False
        self.jumpCounter = 35
        self.direction = "right"
        self.walkCounter =  1
        self.walk = False

        self.collisionRight = False
        self.collisionLeft = False

        self.climbCounter = 1
        self.climb = False
        self.climb4blockFlag = False
        self.amountblocksWall = 0
        self.climbSoundFlag = False


        self.crouch = False
        self.crouchCounter = 1
        self.crouchWalkCounter = 1
        self.crouchUPColision = False
        self.crouchCollisionRight = False
        self.crouchCollisionLeft = False

        self.attack = False
        self.attackCounter = 1
        self.hidedSword = False
        self.pickUpSwordCollisionRight = False
        self.pickUpSwordCollisionLeft = False
        self.pickUpSwordSoundFlag = False

        self.hit = False
        self.hitCounter =1
        self.hitGapCounter = 101
        self.hitSoundFlag = False

        self.defend = False

        self.nearestEnemy = None

        self.getHitCounter = 0

        self.isDead = False
        self.deadCounter = 1
        self.isSpeared = False
        self.bladeX = None
        self.spearedSoundFlag = False

        self.getPotionMode = False
        self.getPotionCounter = 1
        self.getPotionSoundFlag = False
        self.getPotionName = ""

        self.getKey = False

        self.enterDoorCounter = 1



    def pLoad(self,fileName):
        i = pygame.image.load(os.path.join(self.path,fileName+".png")).convert_alpha()
        i = pygame.transform.scale(i,(i.get_width()*self.PLAYER_SCALE,i.get_height()*self.PLAYER_SCALE))


        return i
    def loadImages(self):
        im = {}
        im.update({"idle1":self.pLoad("idle1")})
        im.update({"walk1": self.pLoad("walk1")})
        im.update({"walk2": self.pLoad("walk2")})
        im.update({"walk3": self.pLoad("walk3")})
        im.update({"walk4":self.pLoad("walk4")})
        im.update({"walk5": self.pLoad("walk5")})
        im.update({"walk6": self.pLoad("walk6")})
        im.update({"walk7": self.pLoad("walk7")})
        im.update({"walk8": self.pLoad("walk8")})
        im.update({"walk9": self.pLoad("walk9")})
        im.update({"walk10": self.pLoad("walk10")})
        im.update({"walk11": self.pLoad("walk11")})

        im.update({"crouch1":self.pLoad("crouch1")})
        im.update({"crouch2": self.pLoad("crouch2")})
        im.update({"crouch3": self.pLoad("crouch3")})
        im.update({"crouch4": self.pLoad("crouch4")})
        im.update({"crouch5": self.pLoad("crouch5")})
        im.update({"crouch6": self.pLoad("crouch6")})
        im.update({"crouch7": self.pLoad("crouch7")})
        im.update({"crouch8": self.pLoad("crouch8")})
        im.update({"crouch9": self.pLoad("crouch9")})
        im.update({"crouch10": self.pLoad("crouch10")})
        im.update({"crouch11": self.pLoad("crouch11")})

        im.update({"climb1": self.pLoad("climb1")})
        im.update({"climb2": self.pLoad("climb2")})
        im.update({"climb3": self.pLoad("climb3")})
        im.update({"climb4": self.pLoad("climb4")})
        im.update({"climb5": self.pLoad("climb5")})
        im.update({"climb6": self.pLoad("climb6")})
        im.update({"climb7": self.pLoad("climb7")})
        im.update({"climb8": self.pLoad("climb8")})
        im.update({"climb9": self.pLoad("climb9")})
        im.update({"climb10": self.pLoad("climb10")})
        im.update({"climb11": self.pLoad("climb11")})
        im.update({"climb12": self.pLoad("climb12")})
        im.update({"climb13": self.pLoad("climb13")})
        im.update({"climb14": self.pLoad("climb14")})
        im.update({"climb15": self.pLoad("climb15")})
        im.update({"climb16": self.pLoad("climb16")})
        im.update({"climb17": self.pLoad("climb17")})
        im.update({"climb18": self.pLoad("climb18")})


        im.update({"pickUpSword1": self.pLoad("pickUpSword1")})
        im.update({"pickUpSword2": self.pLoad("pickUpSword2")})
        im.update({"pickUpSword3": self.pLoad("pickUpSword3")})
        im.update({"pickUpSword4": self.pLoad("pickUpSword4")})
        im.update({"pickUpSword5": self.pLoad("pickUpSword5")})
        im.update({"pickUpSword6": self.pLoad("pickUpSword6")})
        im.update({"pickUpSword7": self.pLoad("pickUpSword7")})
        im.update({"pickUpSword8": self.pLoad("pickUpSword8")})
        im.update({"pickUpSword9": self.pLoad("pickUpSword9")})
        im.update({"pickUpSword10": self.pLoad("pickUpSword10")})

        im.update({"walkingSword1": self.pLoad("walkingSword1")})
        im.update({"walkingSword2": self.pLoad("walkingSword2")})
        im.update({"walkingSword3": self.pLoad("walkingSword3")})

        im.update({"crouchWalking1": self.pLoad("crouchWalking1")})
        im.update({"crouchWalking2": self.pLoad("crouchWalking2")})
        im.update({"crouchWalking3": self.pLoad("crouchWalking3")})
        im.update({"crouchWalking4": self.pLoad("crouchWalking4")})

        im.update({"attack1": self.pLoad("attack1")})
        im.update({"attack2": self.pLoad("attack2")})
        im.update({"attack3": self.pLoad("attack3")})
        im.update({"attack4": self.pLoad("attack4")})
        im.update({"attack5": self.pLoad("attack5")})

        im.update({"defend1": self.pLoad("defend1")})

        im.update({"getHit": self.pLoad("getHit")})

        im.update({"dying1": self.pLoad("dying1")})
        im.update({"dying2": self.pLoad("dying2")})
        im.update({"dying3": self.pLoad("dying3")})
        im.update({"dying4": self.pLoad("dying4")})
        im.update({"dying5": self.pLoad("dying5")})
        im.update({"dying6": self.pLoad("dying6")})

        im.update({"speared": self.pLoad("speared")})

        im.update({"gethealPotion1":self.pLoad("gethealPotion1")})
        im.update({"gethealPotion2": self.pLoad("gethealPotion2")})
        im.update({"gethealPotion3": self.pLoad("gethealPotion3")})
        im.update({"gethealPotion4": self.pLoad("gethealPotion4")})
        im.update({"gethealPotion5": self.pLoad("gethealPotion6")})
        im.update({"gethealPotion6": self.pLoad("gethealPotion5")})
        im.update({"gethealPotion7": self.pLoad("gethealPotion6")})
        im.update({"gethealPotion8": self.pLoad("gethealPotion7")})
        im.update({"gethealPotion9": self.pLoad("gethealPotion8")})
        im.update({"gethealPotion10": self.pLoad("gethealPotion9")})
        im.update({"gethealPotion11": self.pLoad("gethealPotion10")})
        im.update({"gethealPotion12": self.pLoad("gethealPotion11")})
        im.update({"gethealPotion13": self.pLoad("gethealPotion12")})
        im.update({"gethealPotion14": self.pLoad("gethealPotion13")})

        im.update({"getwrongPotion1": self.pLoad("getwrongPotion1")})
        im.update({"getwrongPotion2": self.pLoad("getwrongPotion2")})
        im.update({"getwrongPotion3": self.pLoad("getwrongPotion3")})
        im.update({"getwrongPotion4": self.pLoad("getwrongPotion4")})
        im.update({"getwrongPotion5": self.pLoad("getwrongPotion6")})
        im.update({"getwrongPotion6": self.pLoad("getwrongPotion5")})
        im.update({"getwrongPotion7": self.pLoad("getwrongPotion7")})
        im.update({"getwrongPotion8": self.pLoad("getwrongPotion8")})
        im.update({"getwrongPotion9": self.pLoad("getwrongPotion9")})
        im.update({"getwrongPotion10": self.pLoad("getwrongPotion10")})
        im.update({"getwrongPotion11": self.pLoad("getwrongPotion11")})
        im.update({"getwrongPotion12": self.pLoad("getwrongPotion12")})
        im.update({"getwrongPotion13": self.pLoad("getwrongPotion13")})
        im.update({"getwrongPotion14": self.pLoad("getwrongPotion14")})





        im.update({"ending1": self.pLoad("ending1")})
        im.update({"ending2": self.pLoad("ending2")})
        im.update({"ending3": self.pLoad("ending3")})
        im.update({"ending4": self.pLoad("endingv4")})
        im.update({"ending5": self.pLoad("endingv5")})
        im.update({"ending6": self.pLoad("endingv6")})
        im.update({"ending7": self.pLoad("endingv7")})
        im.update({"ending8": self.pLoad("endingv11")})
        im.update({"ending9": self.pLoad("endingv9")})
        im.update({"ending10": self.pLoad("endingv10")})
        im.update({"ending11": self.pLoad("endingv11")})




        return im



    def draw(self,surface):

        #czarny kwadrat zeby widziec kolizje
        #pygame.draw.rect(surface,(0,0,0,0),self.rect)
        surface.blit(self.image,self.rect)

    def checkDistance(self):
        try:
            if self.direction == "right":
                return math.hypot(self.game.player.rect.right - self.nearestEnemy.rect.left, self.game.player.rect.y - self.nearestEnemy.rect.y)
            elif self.direction == "left":
                return math.hypot(self.game.player.rect.left - self.nearestEnemy.rect.right, self.game.player.rect.y - self.nearestEnemy.rect.y)
        except AttributeError:
            return float('inf')

    def climbing(self):
        #sprawdzamy czy gracz ma mozliwosc skoku
        check1 = False
        check2 = False
        check3 = True
        leftWall = None
        bottomWall = None
        rightWall = None

        for tile in self.game.tileHandler.tileMap:
            # I czy nie ma blokow nad soba
            if tile.rect.colliderect((self.rect.x,self.rect.top - self.game.PIXEL_SIZE,self.rect.width,self.rect.height)):
                return False
            #II czy obok siebie ma dwa bloki
            if self.direction == "right":
                if tile.rect.colliderect((self.rect.x + self.game.PIXEL_SIZE, self.rect.y - (self.game.PIXEL_SIZE*2),
                                          self.rect.width, self.rect.height)):
                    check2 = check1 = True
                    leftWall = tile.rect.left
                    bottomWall = tile.rect.bottom
                    if not self.climb4blockFlag:
                        self.amountblocksWall = 3
                    if tile.rect.colliderect(self.rect.x + self.game.PIXEL_SIZE, self.rect.y - (self.game.PIXEL_SIZE * 3),self.rect.width, self.rect.height):
                        self.climb4blockFlag = True
                        self.amountblocksWall = 4
                    if tile.rect.colliderect(
                            (self.rect.x + self.game.PIXEL_SIZE, self.rect.y - (self.game.PIXEL_SIZE * 4),
                             self.rect.width, self.rect.height)):
                        check3 = False

            elif self.direction == "left":
                if tile.rect.colliderect((self.rect.x - self.game.PIXEL_SIZE, self.rect.y - (self.game.PIXEL_SIZE*2),
                                          self.rect.width, self.rect.height)):
                    check2 = check1 = True
                    rightWall = tile.rect.right
                    bottomWall = tile.rect.bottom
                    if not self.climb4blockFlag:
                        self.amountblocksWall = 3
                    if tile.rect.colliderect(
                            (self.rect.x - self.game.PIXEL_SIZE, self.rect.y - (self.game.PIXEL_SIZE * 3),
                             self.rect.width, self.rect.height)):
                        self.climb4blockFlag = True
                        self.amountblocksWall = 4
                if tile.rect.colliderect((self.rect.x - self.game.PIXEL_SIZE, self.rect.y - (self.game.PIXEL_SIZE * 4),
                                          self.rect.width, self.rect.height)):
                    check3 = False
        if check1 and check2 and check3:
            self.climb = True
            self.vel_y = 0
            # jesli jest mozliwosc do wspinaczki -> wspinamy sie
            if self.amountblocksWall == 3 and not self.climb4blockFlag:
                self.climbCounter += 0.1
                if 10 < int(self.climbCounter) < 16:
                    if not self.climbSoundFlag:
                        self.climbSoundFlag = True
                        self.game.sounds.playSound("climb")
                        self.game.sounds.playSound("climb")
                    self.vel_y -= 0.5
                if int(self.climbCounter) >= 16:
                    self.vel_y -= 0.8

                if self.direction == "right":
                    if int(self.climbCounter) > 18:
                        self.rect = self.image.get_rect(bottom=bottomWall - self.game.PIXEL_SIZE,
                                                        right=self.rect.right + self.game.PIXEL_SIZE)
                        self.climb = False
                        self.climbSoundFlag = False
                    else:
                        self.image = pygame.transform.flip(self.images[f"climb{int(self.climbCounter)}"], True, False)
                        self.rect = self.image.get_rect(right=leftWall, top=self.rect.top, bottom=self.rect.bottom)

                elif self.direction == "left":
                    if int(self.climbCounter) > 18:
                        self.rect = self.image.get_rect(bottom=bottomWall + self.game.PIXEL_SIZE,
                                                        right=self.rect.right - self.game.PIXEL_SIZE)
                        self.climb = False
                        self.climbSoundFlag = False
                    else:
                        self.image = self.images[f"climb{int(self.climbCounter)}"]
                        self.rect = self.image.get_rect(left=rightWall, top=self.rect.top, bottom=self.rect.bottom)
            if self.amountblocksWall == 4:
                self.climbCounter += 0.1
                if 10 < int(self.climbCounter) < 18:
                    if not self.climbSoundFlag:
                        self.climbSoundFlag = True
                        self.game.sounds.playSound("climb")
                    self.vel_y -=1
                if self.direction == "right":
                    if int(self.climbCounter) >18:
                        self.rect = self.image.get_rect(bottom=bottomWall+self.game.PIXEL_SIZE,right=self.rect.right+self.game.PIXEL_SIZE)
                        self.climb = False
                        self.climbSoundFlag = False
                        self.climb4blockFlag = False
                    else:
                        self.image = pygame.transform.flip(self.images[f"climb{int(self.climbCounter)}"],True,False)
                        self.rect = self.image.get_rect(right=leftWall,top=self.rect.top,bottom=self.rect.bottom)

                elif self.direction == "left":
                    if int(self.climbCounter) >18:
                        self.rect = self.image.get_rect(bottom=bottomWall-self.game.PIXEL_SIZE,right=self.rect.right-self.game.PIXEL_SIZE)
                        self.climb = False
                        self.climbSoundFlag = False
                        self.climb4blockFlag = False
                    else:
                        self.image =self.images[f"climb{int(self.climbCounter)}"]
                        self.rect = self.image.get_rect(left=rightWall,top=self.rect.top,bottom=self.rect.bottom)


    def walking(self):

        if self.direction == "right":
            if self.attack and not self.collisionRight:
                self.attackCounter = 10
                self.walkCounter += 0.07
                if self.walkCounter >4:
                    self.walkCounter = 1
                self.image = pygame.transform.flip(self.images[f"walkingSword{int(self.walkCounter)}"],True,False)
                if self.pickUpSwordCollisionRight:
                    self.attack = False
                    self.current_left -= 15
                    self.rect = self.image.get_rect(topleft=(self.current_left, self.current_top))
                else:
                    if self.collisionLeft:
                        self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
                        #self.collisionLeft = False
                    else:
                        self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
                self.vel_x = self.SPEED/3
            elif not self.attack:
                self.walkCounter += 0.1
                if self.walkCounter > 11:
                    self.walkCounter = 3
                self.image = pygame.transform.flip(self.images[f"walk{int(self.walkCounter)}"], True, False)
                if self.collisionLeft:
                    self.rect = self.image.get_rect(topleft=(self.current_left, self.current_top))
                    self.collisionLeft = False
                else:
                    self.collisionRight = False
                    self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
                self.vel_x = self.SPEED
            self.walk = True


        elif self.direction == "left":
            if self.attack and not self.collisionLeft:
                self.attackCounter = 10
                self.walkCounter += 0.07
                if self.walkCounter >4:
                    self.walkCounter = 1
                self.image = self.images[f"walkingSword{int(self.walkCounter)}"]
                if self.pickUpSwordCollisionLeft:
                    self.attack = False
                    self.current_right += 15
                    self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
                else:
                    if self.collisionRight:
                        self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
                        self.collisionRight = False
                    else:
                        self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
                self.vel_x = -self.SPEED/3

            elif not self.attack:
                self.walkCounter += 0.1
                if self.walkCounter > 11:
                    self.walkCounter = 3
                self.image = self.images[f"walk{int(self.walkCounter)}"]
                if self.collisionRight:
                    self.rect = self.image.get_rect(right=self.current_right, bottom=self.current_bottom)
                    #self.collisionRight = False
                else:
                    self.collisionLeft = False
                    self.rect = self.image.get_rect(topleft=(self.current_left, self.current_top))
                self.vel_x = -self.SPEED
            self.walk = True


    def standing(self):
        self.walkCounter = 1
        self.climbCounter = 1
        if self.direction == "right":
            self.image = pygame.transform.flip(self.images[f"idle1"], True, False)
            if self.hidedSword:
                self.rect = self.image.get_rect(topleft=(self.current_left, self.current_top))
                self.hidedSword = False
            else:
                if self.collisionLeft:
                    self.rect = self.image.get_rect(topright=(self.current_right, self.current_top))
                    self.collisionLeft = False
                else:
                    self.rect = self.image.get_rect(bottomright=(self.current_right, self.current_bottom))
        elif self.direction == "left":
            self.image = self.images[f"idle1"]
            if self.hidedSword:
                self.rect = self.image.get_rect(topright=(self.current_right, self.current_top))
                self.hidedSword = False
            else:
                if self.collisionRight:
                    self.rect = self.image.get_rect(topleft=(self.current_left, self.current_top))
                    self.collisionRight = False
                else:
                    self.rect = self.image.get_rect(bottomleft=(self.current_left, self.current_bottom))

    def crouching(self):
        if not self.walk:
            if self.direction == "right":
                if not self.crouchCollisionLeft:
                    self.crouchCounter += 0.3
                    if self.crouchCounter > 11:
                        self.crouchCounter = 11
                    self.image = pygame.transform.flip(self.images[f"crouch{int(self.crouchCounter)}"], True, False)
                    # jesli jest kolizja po lewej stronie to przesuwam postac troszke prawej strony
                    if self.collisionLeft:
                        self.rect = self.image.get_rect(bottomleft=(self.current_left, self.current_bottom))
                    else:
                        self.rect = self.image.get_rect(bottomright=(self.current_right, self.current_bottom))
                else:
                    self.crouchCounter = 1
            elif self.direction == "left":
                if not self.crouchCollisionRight:
                    self.crouchCounter += 0.3
                    if self.crouchCounter > 11:
                        self.crouchCounter = 11
                    self.image = self.images[f"crouch{int(self.crouchCounter)}"]
                    if self.collisionRight:
                        self.rect = self.image.get_rect(bottomright=(self.current_right, self.current_bottom))
                    else:
                        self.rect = self.image.get_rect(bottomleft=(self.current_left, self.current_bottom))
                else:
                    self.crouchCounter = 1
        else:
            self.crouchCounter = 11
            self.crouchWalkCounter+= 0.2
            if self.crouchWalkCounter >5:
                self.crouchWalkCounter = 1
            if self.direction == "right":
                self.image = pygame.transform.flip(self.images[f"crouchWalking{int(self.crouchWalkCounter)}"],True,False)
                if self.collisionLeft:
                    self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
                else:
                    self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
            elif self.direction == "left":
                self.image = self.images[f"crouchWalking{int(self.crouchWalkCounter)}"]
                if self.collisionRight:
                    self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
                else:
                    self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
    def attacking(self):
        if self.defend:
            if self.direction == "right":
                self.image = pygame.transform.flip(self.images[f"defend1"],True,False)
                self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
            elif self.direction == "left":
                self.image = self.images[f"defend1"]
                self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
        elif self.hit:
            self.hitCounter += 0.15
            if self.hitCounter > 6:
                self.hitCounter = 1
                self.attackCounter = 10
                self.hit = False
                self.hitSoundFlag = False
                if self.checkDistance() < 50 and self.nearestEnemy.defendMode == False:
                    self.nearestEnemy.enemyLives -= 1
                    self.nearestEnemy.getHitCounter = 20
                    if not self.hitSoundFlag:
                        self.game.sounds.playSound("enemyGetDamage")
                        self.hitSoundFlag = True
            if self.checkDistance() < 50 and self.nearestEnemy.defendMode and self.hitCounter >1:
                if not self.hitSoundFlag:
                    self.game.sounds.playSound("swordHit")
                    self.hitSoundFlag = True
            elif self.checkDistance() > 50 and self.hitCounter >1:
                if not self.hitSoundFlag:
                    self.game.sounds.playSound("swordSwing")
                    self.hitSoundFlag = True
            if self.direction == "right":
                self.image = pygame.transform.flip(self.images[f"attack{int(self.hitCounter)}"], True, False)
                self.rect = self.image.get_rect(topleft=(self.current_left, self.current_top))
            elif self.direction == "left":
                self.image = self.images[f"attack{int(self.hitCounter)}"]
                self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))

        else:
            if self.attack and not self.walk:
                if self.attackCounter > 10:
                    self.attackCounter = 10
                    self.pickUpSwordSoundFlag = False
                if self.direction == "right" and not self.pickUpSwordCollisionRight:
                    if not self.pickUpSwordSoundFlag and self.attackCounter < 10:
                        self.game.sounds.playSound("playerPickUpSword")
                        self.pickUpSwordSoundFlag = True
                    self.attackCounter += 0.2
                    self.image = pygame.transform.flip(self.images[f"pickUpSword{int(self.attackCounter)}"],True,False)
                    if self.collisionLeft:
                        self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
                        self.collisionLeft = False
                    else:
                        self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
                elif self.direction == "left" and not self.pickUpSwordCollisionLeft:
                    if not self.pickUpSwordSoundFlag and self.attackCounter < 10:
                        self.game.sounds.playSound("playerPickUpSword")
                        self.pickUpSwordSoundFlag = True
                    self.attackCounter += 0.2
                    self.image = self.images[f"pickUpSword{int(self.attackCounter)}"]
                    if self.collisionRight:
                        self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
                        self.collisionRight = False
                    else:
                        self.rect = self.image.get_rect(topright=(self.current_right, self.current_top))
                elif self.pickUpSwordCollisionLeft:
                    print("wtf")
                    self.attack = False
                    self.rect = self.image.get_rect(topright=(self.current_right, self.current_top))
                elif self.pickUpSwordCollisionRight:
                    print("wtf2")
                    self.attack = False
                    self.rect = self.image.get_rect(topleft=(self.current_left, self.current_top))
            elif not self.attack:
                if self.attackCounter >1:
                    self.attackCounter -= 0.2
                    if not self.pickUpSwordSoundFlag:
                        self.game.sounds.playSound("playerHideSword")
                        self.pickUpSwordSoundFlag = True
                    if self.attackCounter <1:
                        self.attackCounter = 1
                        self.hidedSword = True
                        self.pickUpSwordSoundFlag = False
                    if self.direction == "left":
                        self.image = self.images[f"pickUpSword{int(self.attackCounter)}"]
                        self.rect = self.image.get_rect(topright=(self.current_right, self.current_top))
                    elif self.direction == "right":
                        self.image = pygame.transform.flip(self.images[f"pickUpSword{int(self.attackCounter)}"],True,False)
                        self.rect= self.image.get_rect(topleft=(self.current_left,self.current_top))
        self.pickUpSwordCollisionRight = self.pickUpSwordCollisionLeft = False

    def getHit(self):
        self.getHitCounter -=1
        if self.direction == "right":
            self.image = pygame.transform.flip(self.images["getHit"],True,False)
            self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
        elif self.direction == "left":
            self.image = self.images["getHit"]
            self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))

    def getPotion(self):
        if self.getPotionMode:
            self.getPotionCounter += 0.1
            if not self.getPotionSoundFlag:
                self.game.sounds.playSound("drinking")
                self.getPotionSoundFlag = True
            if self.getPotionCounter > 15:
                self.game.sounds.stopSound("drinking")

                self.getPotionCounter = 1
                self.getPotionMode = False
                self.getPotionSoundFlag = False
                if self.getPotionName == "healPotion":
                    self.game.sounds.playSound("healing")
                    self.game.ui.playerLifes = self.game.ui.playerLifes + 1 if self.game.ui.playerLifes < self.game.ui.playerMaxLifes else self.game.ui.playerMaxLifes
                elif self.getPotionName == "wrongPotion":
                    self.game.sounds.playSound("playerGetDamage")
                    self.game.ui.playerLifes -=1
            if self.direction == "right":
                self.image = pygame.transform.flip(self.images[f"get{self.getPotionName}{int(self.getPotionCounter)}"],True,False)
                self.rect = self.image.get_rect(bottomleft=(self.current_left,self.current_bottom))
            elif self.direction == "left":
                self.image = self.images[f"get{self.getPotionName}{int(self.getPotionCounter)}"]
                self.rect = self.image.get_rect(bottomright=(self.current_right,self.current_bottom))
    def speared(self):
        self.isDead = self.isSpeared =True
        if not self.spearedSoundFlag:
            self.spearedSoundFlag = True
            self.game.sounds.playSound("stabbed")
        if self.direction == "right":
            self.image = pygame.transform.flip(self.images["speared"], True, False)
            self.rect = self.image.get_rect(bottomleft=(self.bladeX,self.current_bottom))
        elif self.direction == "left":
            self.image = self.images["speared"]
            self.rect = self.image.get_rect(bottomright=(self.bladeX,self.current_bottom))
        self.game.gameOver = True
        self.game.ui.playerLifes = 0
        self.game.sounds.playSound("gameover")
    def dead(self):
        self.isDead = True
        self.deadCounter += 0.1
        if self.deadCounter >7:

            self.deadCounter = 6
            self.game.gameOver = True
            self.game.sounds.playSound("gameover")

        if self.direction == "right":
            self.image = pygame.transform.flip(self.images[f"dying{int(self.deadCounter)}"],True,False)
            self.rect = self.image.get_rect(bottomleft=(self.current_left,self.current_bottom))
        elif self.direction == "left":

            self.image = self.images[f"dying{int(self.deadCounter)}"]
            self.rect = self.image.get_rect(bottomright=(self.current_right,self.current_bottom))

    def enterDoor(self):
        self.enterDoorCounter += 0.1
        # if self.enterDoorCounter > 12:
        #     self.enterDoorCounter = 11
        #     self.game.newLevel(self.game.level.getLevel()+1)
        # if self.enterDoorCounter < 8:
        #     self.vel_x = 0.5
        # if self.enterDoorCounter%2:
        #     self.vel_y =-0.1
        # self.image = self.images[f"ending{int(self.enterDoorCounter)}"]
        # self.rect = self.image.get_rect(top=self.current_top,left=self.current_left)

        if self.enterDoorCounter > 9:
            self.enterDoorCounter = 8
            self.game.newLevel(self.game.level.getLevel()+1)
        if self.enterDoorCounter < 8:
            self.vel_x = 0.5
        if self.enterDoorCounter%2:
            self.vel_y =-0.1
        self.image = self.images[f"ending{int(self.enterDoorCounter)}"]
        self.rect = self.image.get_rect(top=self.current_top,left=self.current_left)



    def update(self):
        #reset oraz dodawanie do wartosci
        self.vel_x = 0
        self.jumpCounter +=1
        self.hitGapCounter+=1
        self.walk = False
        self.crouch = False
        self.defend = False
        self.current_left = self.rect.left
        self.current_right = self.rect.right
        self.current_bottom = self.rect.bottom
        self.current_top = self.rect.top

        keys = pygame.key.get_pressed()

        if not self.climb:
            #grawitacja
            self.vel_y +=1
            if self.vel_y > 10:
                self.vel_y = 10
        if self.game.ui.playerLifes <1 and not self.isSpeared:
            self.dead()
        elif self.game.ui.playerLifes <1 and self.isSpeared:
            self.speared()
        else:

            if self.getHitCounter > 0:
                self.getHit()
            else:
            #poruszanie sie postacia
            #w prawo
                if keys[pygame.K_RIGHT] and not self.climb:
                    self.direction = "right"
                    self.walking()

                #w lewo
                if keys[pygame.K_LEFT] and not self.climb:
                    self.direction = "left"
                    self.walking()



                #jesli postac przestanie isc
                if not self.walk and not self.climb and not self.attack and not self.getPotionMode:
                    self.standing()

                #wspinanie sie
                if keys[pygame.K_UP]:
                    if self.attack:
                        self.defend = True
                    else:
                        self.climbing()
                else:
                    self.climbCounter = 1
                    self.climb = False

                # kucniecie
                if keys[pygame.K_DOWN] and not self.climb:
                    self.crouch = True
                elif self.crouchUPColision:
                    self.crouch = True
                else:
                    self.crouchCounter = 1
                if self.crouch and not self.climb:
                    self.crouching()

                self.crouchUPColision = self.crouchCollisionLeft = self.crouchCollisionRight = False

                # podnoszenie eliksiru
                for potion in self.game.level.potions:
                    if self.direction == "right":
                        if potion.rect.colliderect((self.rect.x + self.game.PIXEL_SIZE, self.rect.y, self.rect.width, self.rect.height)) and keys[pygame.K_UP] and not self.attack and potion.currentMap == self.game.level.currentMap:
                            self.getPotionMode = True
                            self.getPotionName = potion.name
                            potion.kill()

                    elif self.direction == "left":
                        if potion.rect.colliderect((self.rect.x - self.game.PIXEL_SIZE, self.rect.y, self.rect.width, self.rect.height)) and keys[pygame.K_UP] and not self.attack and potion.currentMap == self.game.level.currentMap:
                            self.getPotionMode = True
                            self.getPotionName = potion.name
                            potion.kill()

                if keys[pygame.K_UP] and self.game.level.door.openable and not self.game.level.door.open and self.getKey:
                    self.getKey = False
                    self.game.level.door.open = True
                    self.game.sounds.playSound("openDoor")
                if self.game.level.door.open:
                    self.enterDoor()


                #podnoszenie klucza
                if keys[pygame.K_UP] and self.game.level.key.pickable and not self.getKey and self.game.level.key.currentMap == self.game.level.currentMap:
                    self.getKey = True
                    self.game.sounds.playSound("getKey")
                    self.game.level.key.rect.x = -150
                #skok
                if keys[pygame.K_SPACE] and not self.jump and self.jumpCounter > 35 and not self.climb and not self.crouch and not self.attack and not self.getPotionMode:
                    self.vel_y = -self.SPEED * 2.5
                    self.jumpCounter = 0
                    self.jump = True
                if not keys[pygame.K_SPACE]:
                    self.jump = False

                #atak
                if keys[pygame.K_LCTRL]:
                    if self.direction == "right" and not self.collisionRight and not self.pickUpSwordCollisionRight:
                        self.attack = True
                    elif self.direction == "left" and not self.collisionLeft and not self.pickUpSwordCollisionLeft:
                        self.attack = True
                if keys[pygame.K_RCTRL]:
                    self.attack = False

                if self.attack and keys[pygame.K_SPACE] and self.hitGapCounter > 100:
                    self.hit = True
                    self.hitGapCounter = 0


                self.getPotion()
                self.attacking()

        #wykrywanie kolizji z przedmiotami
        for tile in self.game.tileHandler.tileMap:
            f_recY = pygame.Rect(self.rect.x,self.rect.y + self.vel_y,self.rect.width,self.rect.height)
            if self.crouch:
                if tile.rect.colliderect((self.rect.x,self.rect.y - 1*self.game.PIXEL_SIZE,self.rect.width,self.rect.height)):
                    self.crouchUPColision = True
                if tile.rect.colliderect((self.rect.right+13,self.rect.y - 1,self.rect.width,self.rect.height)) and self.crouchCounter <2:

                    self.crouchCollisionRight = True
                if tile.rect.colliderect((self.rect.left-24,self.rect.y-1,self.rect.width,self.rect.height)) and self.crouchCounter <2:
                    self.crouchCollisionLeft = True
            if tile.rect.colliderect((self.rect.left-26,self.rect.y-20,self.rect.width,self.rect.height)):
                self.pickUpSwordCollisionLeft = True
            if tile.rect.colliderect((self.rect.right+11,self.rect.y-3,self.rect.width,self.rect.height)):
                self.pickUpSwordCollisionRight = True
            if tile.rect.colliderect(f_recY):
                if self.vel_y < 0:
                    #skacze
                    self.rect.top = tile.rect.bottom
                    self.vel_y = 0

                elif self.vel_y >0:
                    #spada
                    self.rect.bottom = tile.rect.top
                    self.vel_y = 0

            f_recX = pygame.Rect(self.rect.x + self.vel_x,self.rect.y, self.rect.width,self.rect.height)

            if tile.rect.colliderect(f_recX):
                if self.vel_x > 0:
                    # w prawo
                    self.collisionRight  = True
                    self.collisionLeft = False
                    self.rect.right = tile.rect.left
                    self.vel_x = 0

                elif self.vel_x < 0:
                    #w lewo
                    self.collisionLeft = True
                    self.collisionRight = False
                    self.rect.left = tile.rect.right
                    self.vel_x = 0
        #wykrywanie kolizji z wrogami
        for enemy in self.game.level.enemies:
            if enemy.rect.colliderect((self.rect.x + self.vel_x*2,self.rect.y,self.rect.width,self.rect.height)) and not enemy.isDead and enemy.currentMap == self.game.level.currentMap:
                self.nearestEnemy = enemy
                if self.vel_x > 0:
                    self.rect.right = enemy.rect.left
                    self.vel_x = 0
                elif self.vel_x < 0:
                    self.rect.left = enemy.rect.right
                    self.vel_x = 0



        #ruch
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y












