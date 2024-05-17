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


        self.crouch = False
        self.crouchCounter = 1

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
        return im

    def draw(self,surface):
        #pygame.draw.rect(surface,(0,0,0,0),self.rect)
        surface.blit(self.image,self.rect)

    def update(self):
        #reset oraz dodawanie do wartosci
        self.vel_x = 0
        self.jumpCounter +=1
        self.walk = False
        current_left = self.rect.left
        current_right = self.rect.right
        current_bottom = self.rect.bottom
        current_top = self.rect.top


        #grawitacja
        self.vel_y +=1
        if self.vel_y > 10:
            self.vel_y = 10

        keys = pygame.key.get_pressed()


        #poruszanie sie postacia
        if keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.walkCounter += 0.1
            if self.walkCounter > 11:
                self.walkCounter = 3
            self.image = pygame.transform.flip(self.images[f"walk{int(self.walkCounter)}"],True,False)
            self.rect = self.image.get_rect(right=current_right,bottom=current_bottom)
            self.walk = True
            self.vel_x = self.SPEED

        if keys[pygame.K_LEFT]:
            self.direction = "left"
            self.walkCounter += 0.1
            if self.walkCounter >11:
                self.walkCounter = 3
            self.image = self.images[f"walk{int(self.walkCounter)}"]
            self.rect = self.image.get_rect(right=current_right,bottom=current_bottom,left=current_left)

            self.walk = True
            self.vel_x = -self.SPEED

        #jesli postac przestanie isc
        if not self.walk:
            self.walkCounter = 1

            if self.direction == "right":
                self.image = pygame.transform.flip(self.images[f"idle1"], True, False)
                self.rect = self.image.get_rect(topright=(current_right, current_top), topleft=(current_left,current_top))
            else:
                self.image = self.images[f"idle1"]
                self.rect = self.image.get_rect(topleft=(current_left, current_top),topright=(current_right, current_top))




        #skok
        if keys[pygame.K_SPACE] and not self.jump and self.jumpCounter > 35:
            self.vel_y = -self.SPEED * 2.5
            self.jumpCounter = 0
            self.jump = True
        if not keys[pygame.K_SPACE]:
            self.jump = False
        for tile in self.game.tileHandler.tileMap:
            f_recY = pygame.Rect(self.rect.x,self.rect.y + self.vel_y,self.rect.width,self.rect.height)
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
                    self.rect.right = tile.rect.left
                    self.vel_x = 0

                elif self.vel_x <0:
                    #w lewo
                    self.rect.left = tile.rect.right
                    self.vel_x = 0




        #ruch
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y










