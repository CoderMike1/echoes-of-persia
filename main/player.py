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
        self.walkingCounter =  1
        self.walk = False
        self.collision = False

    def pLoad(self,fileName,flip=False):
        i = pygame.image.load(os.path.join(self.path,fileName+".png")).convert_alpha()
        i = pygame.transform.scale(i,(i.get_width()*self.PLAYER_SCALE,i.get_height()*self.PLAYER_SCALE))
        flip = False
        if flip:
            i = pygame.transform.flip(i,True,False)

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
        return im

    def draw(self,surface):

        #pygame.draw.rect(surface,(0,0,0,0),self.rect)
        surface.blit(self.image,self.rect)

    def update(self):
        #aktualne polozenie na prawo i lewo
        current_right = self.rect.right
        current_left = self.rect.left
        self.walk = False
        self.jumpCounter+=1
        self.vel_x = self.SPEED
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10

        keys = pygame.key.get_pressed()
        for tile in self.game.tileHandler.tileMap:

            #gora
            if tile.rect.colliderect(self.rect.x, self.rect.y - self.SPEED*2, self.rect.width,self.rect.height):
                if self.rect.top - self.SPEED < tile.rect.bottom:
                    print(self.rect.top)
                    print(tile.rect.bottom)
                    print('kolizo')
                    self.rect.top = tile.rect.bottom
                    self.vel_y +=1



            #dół
            if tile.rect.colliderect(self.rect.x, self.rect.y + self.SPEED, self.rect.width, self.rect.height):
                if self.vel_y >= 0:
                    self.vel_y = 0



            #prawa strona
            if tile.rect.colliderect(self.rect.x + self.SPEED, self.rect.y-20, self.rect.width, self.rect.height):
                if keys[pygame.K_RIGHT] and self.rect.right + self.SPEED > tile.rect.left:
                    self.vel_x = 0


            #lewa strona
            if tile.rect.colliderect(self.rect.x - self.SPEED, self.rect.y -20, self.rect.width, self.rect.height):
                if keys[pygame.K_LEFT] and self.rect.left - self.SPEED < tile.rect.right:
                    self.vel_x = 0


        self.rect.y += self.vel_y


        if keys[pygame.K_SPACE] and not self.jump and self.jumpCounter > 35:
            self.vel_y = -self.SPEED * 2.5
            self.jumpCounter = 0
            self.jump = True
        if not keys[pygame.K_SPACE]:
            self.jump = False

        if keys[pygame.K_LEFT]:
            self.direction = "left"
            self.walkingCounter += 0.1
            if self.walkingCounter > 11:
                self.walkingCounter = 3
            self.image = self.images[f"walk{int(self.walkingCounter)}"]
            self.rect = self.image.get_rect(topleft=(current_left, self.rect.top))
            self.rect.x -= self.vel_x
            self.walk = True


        elif keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.walkingCounter += 0.1
            if self.walkingCounter > 11:
                self.walkingCounter = 3
            self.image = pygame.transform.flip(self.images[f"walk{int(self.walkingCounter)}"], True,
                                               False)
            self.rect = self.image.get_rect(topright=(current_right, self.rect.top))
            self.rect.x += self.vel_x
            self.walk = True

        if not self.walk:
            self.walkingCounter = 1

            if self.direction == "right":
                self.image = pygame.transform.flip(self.images[f"idle1"],True,False)
                self.rect = self.image.get_rect(topright=(current_right, self.rect.top))
            else:
                self.image = self.images[f"idle1"]
                self.rect = self.image.get_rect(topleft=(current_left, self.rect.top))


        # if keys[pygame.K_s]:
        #     self.rect.move_ip([0, SPEED])





