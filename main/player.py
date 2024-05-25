import pygame,os
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


        self.crouch = False
        self.crouchCounter = 1
        self.crouchUPColission = False

        self.attack = False
        self.attackCounter = 1
        self.hidedSword = False
        self.pickUpSwordCollisionRight = False
        self.pickUpSwordCollisionLeft = False

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

        return im

    def draw(self,surface):

        #czarny kwadrat zeby widziec kolizje
        #pygame.draw.rect(surface,(0,0,0,0),self.rect)
        surface.blit(self.image,self.rect)


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
            if tile.rect.colliderect((self.rect.x,self.rect.y - self.game.PIXEL_SIZE,self.rect.width,self.rect.height)):
                return False

            #II czy obok siebie ma dwa bloki
            if self.direction == "right":
                if tile.rect.colliderect((self.rect.x + self.game.PIXEL_SIZE, self.rect.y - self.game.PIXEL_SIZE*2, self.rect.width,self.rect.height)):
                    check2 = True
                    check1 = True
                    leftWall = tile.rect.left
                    bottomWall = tile.rect.bottom
                if tile.rect.colliderect((self.rect.x + self.game.PIXEL_SIZE, self.rect.y - (self.game.PIXEL_SIZE*4), self.rect.width,self.rect.height)):
                    check3 = False
            elif self.direction == "left":
                if tile.rect.colliderect((self.rect.x - self.game.PIXEL_SIZE, self.rect.y - self.game.PIXEL_SIZE*2,
                                          self.rect.width, self.rect.height)):
                    check2 = True
                    check1 = True
                    rightWall = tile.rect.right
                    bottomWall = tile.rect.bottom
                if tile.rect.colliderect((self.rect.x - self.game.PIXEL_SIZE, self.rect.y - (self.game.PIXEL_SIZE * 4),
                                          self.rect.width, self.rect.height)):
                    check3 = False

        if check1 and check2 and check3:
            self.climb = True
            self.vel_y = 0
            # jesli jest mozliwosc do wspinaczki -> wspinamy sie

            self.climbCounter += 0.1


            if 10 < int(self.climbCounter) < 18:
                self.vel_y -=1

            if self.direction == "right":
                if int(self.climbCounter) >18:
                    self.rect = self.image.get_rect(bottom=bottomWall-self.game.PIXEL_SIZE,right=self.rect.right+self.game.PIXEL_SIZE)
                    self.climb = False
                else:
                    self.image = pygame.transform.flip(self.images[f"climb{int(self.climbCounter)}"],True,False)
                    self.rect = self.image.get_rect(right=leftWall,top=self.rect.top,bottom=self.rect.bottom)

            elif self.direction == "left":
                if int(self.climbCounter) >18:
                    self.rect = self.image.get_rect(bottom=bottomWall+self.game.PIXEL_SIZE,right=self.rect.right-self.game.PIXEL_SIZE)
                    self.climb = False
                else:
                    self.image =self.images[f"climb{int(self.climbCounter)}"]
                    self.rect = self.image.get_rect(left=rightWall,top=self.rect.top,bottom=self.rect.bottom)


    def walking(self):
        print(self.collisionRight,self.collisionLeft)
        if self.direction == "right":
            if self.attack and not self.collisionRight:
                self.walkCounter += 0.07
                if self.walkCounter >4:
                    self.walkCounter = 1
                self.image = pygame.transform.flip(self.images[f"walkingSword{int(self.walkCounter)}"],True,False)
                if self.collisionLeft:
                    self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
                    self.collisionLeft = False
                else:
                    self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
                if self.pickUpSwordCollisionRight:
                    self.attack = False
                    self.vel_x = 0
                else:
                    self.vel_x = self.SPEED/3

            else:
                self.walkCounter += 0.1
                if self.walkCounter > 11:
                    self.walkCounter = 3
                self.image = pygame.transform.flip(self.images[f"walk{int(self.walkCounter)}"], True, False)
                if self.collisionLeft:
                    self.rect = self.image.get_rect(topleft=(self.current_left, self.current_top))
                    self.collisionLeft = False
                else:
                    self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
                self.vel_x = self.SPEED
            self.walk = True


        elif self.direction == "left":
            if self.attack and not self.collisionLeft:
                self.walkCounter += 0.07
                if self.walkCounter >4:
                    self.walkCounter = 1
                self.image = self.images[f"walkingSword{int(self.walkCounter)}"]
                if self.collisionRight:
                    self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
                    self.collisionRight = False
                else:
                    self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
                if self.pickUpSwordCollisionLeft:
                    self.attack = False
                    self.vel_x = 0
                else:
                    self.vel_x = -self.SPEED/3

            else:
                self.walkCounter += 0.1
                if self.walkCounter > 11:
                    self.walkCounter = 3
                self.image = self.images[f"walk{int(self.walkCounter)}"]
                if self.collisionRight:
                    self.rect = self.image.get_rect(right=self.current_right, bottom=self.current_bottom)
                    self.collisionRight = False
                else:
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
        self.crouchCounter += 0.3
        if self.crouchCounter > 11:
            self.crouchCounter = 11
        if self.direction == "right":
            self.image = pygame.transform.flip(self.images[f"crouch{int(self.crouchCounter)}"], True, False)
            # jesli jest kolizja po lewej stronie to przesuwam postac troszke prawej strony
            if self.collisionLeft:
                self.rect = self.image.get_rect(bottomleft=(self.current_left, self.current_bottom))
            else:
                self.rect = self.image.get_rect(bottomright=(self.current_right, self.current_bottom))
        elif self.direction == "left":
            self.image = self.images[f"crouch{int(self.crouchCounter)}"]
            if self.collisionRight:
                self.rect = self.image.get_rect(bottomright=(self.current_right, self.current_bottom))
            else:
                self.rect = self.image.get_rect(bottomleft=(self.current_left, self.current_bottom))

    def attacking(self):
        if self.attack and not self.walk:
            if self.attackCounter > 10:
                self.attackCounter = 10
            if self.direction == "right" and not self.pickUpSwordCollisionRight:
                self.attackCounter += 0.2
                self.image = pygame.transform.flip(self.images[f"pickUpSword{int(self.attackCounter)}"],True,False)
                if self.collisionLeft:
                    self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
                    self.collisionLeft = False
                else:
                    self.rect = self.image.get_rect(topleft=(self.current_left,self.current_top))
            elif self.direction == "left" and not self.pickUpSwordCollisionLeft:
                self.attackCounter += 0.2
                self.image = self.images[f"pickUpSword{int(self.attackCounter)}"]
                if self.collisionRight:
                    self.rect = self.image.get_rect(topright=(self.current_right,self.current_top))
                    self.collisionRight = False
                else:
                    self.rect = self.image.get_rect(topright=(self.current_right, self.current_top))


        elif not self.attack:
            if self.attackCounter >1:
                self.attackCounter -= 0.2
                if self.attackCounter <1:
                    self.attackCounter = 1
                    self.hidedSword = True

                if self.direction == "left":
                    self.image = self.images[f"pickUpSword{int(self.attackCounter)}"]
                    self.rect = self.image.get_rect(topright=(self.current_right, self.current_top))
                elif self.direction == "right":
                    self.image = pygame.transform.flip(self.images[f"pickUpSword{int(self.attackCounter)}"],True,False)
                    self.rect= self.image.get_rect(topleft=(self.current_left,self.current_top))
        self.pickUpSwordCollisionRight = self.pickUpSwordCollisionLeft = False

    def update(self):

        #reset oraz dodawanie do wartosci
        self.vel_x = 0
        self.jumpCounter +=1
        self.walk = False
        self.crouch = False
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
        if not self.walk and not self.climb and not self.attack:
            self.standing()

        #wspinanie sie
        if keys[pygame.K_UP]:
            self.climbing()
        else:
            self.climbCounter = 1
            self.climb = False

        # kucniecie
        if keys[pygame.K_DOWN] and not self.climb:
            self.crouch = True
        elif self.crouchUPColission:
            self.crouch = True
        else:
            self.crouchCounter = 1
        if self.crouch and not self.climb:
            self.crouching()

        self.crouchUPColission = False

        #skok
        if keys[pygame.K_SPACE] and not self.jump and self.jumpCounter > 35 and not self.climb and not self.crouch and not self.attack:
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

        self.attacking()

        #wykrywanie kolizji z przedmiotami
        for tile in self.game.tileHandler.tileMap:
            f_recY = pygame.Rect(self.rect.x,self.rect.y + self.vel_y,self.rect.width,self.rect.height)
            if self.crouch and tile.rect.colliderect((self.rect.x,self.rect.y - 1*self.game.PIXEL_SIZE,self.rect.width,self.rect.height)):
                self.crouchUPColission = True

            if tile.rect.colliderect((self.rect.x-10,self.rect.y-3,self.rect.width,self.rect.height)):
                self.pickUpSwordCollisionLeft = True
                self.collisionRight = False
            if tile.rect.colliderect((self.rect.right+10,self.rect.y-3,self.rect.width,self.rect.height)):
                self.pickUpSwordCollisionRight = True
                self.collisionLeft = False
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
        #ruch
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y










