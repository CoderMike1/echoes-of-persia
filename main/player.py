import pygame,os
class Player(pygame.sprite.Sprite):
    path = os.path.join(os.path.dirname(os.getcwd()), 'images','player')
    PLAYER_WIDTH = 15
    PLAYER_HEIGHT = 50
    PLAYER_SCALE = 3
    SPEED = 5
    GRAVITY = 1
    def __init__(self,game,x,y):
        super().__init__()
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.path, 'playerIMG.png')),
                                       (self.PLAYER_WIDTH * self.PLAYER_SCALE, self.PLAYER_HEIGHT * self.PLAYER_SCALE)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = x,y
        self.vel_y = 0
        self.jump = False
        self.jumpCounter = 0
        self.direction = "right"

    def draw(self,surface):
        pygame.draw.rect(surface,(0,0,0,0),self.rect)
        surface.blit(self.image,self.rect)
        #surface.blit(self.mask_image,self.rect)

    def update(self):
        #grawitacja
        self.vel_y +=1
        if self.vel_y >10:
            self.vel_y = 10

        self.rect.y += self.vel_y

        #kolizja
        # for tile in self.game.tileHandler.tileMap:
        #     if self.rect.colliderect(tile):
        #         if self.jump:
        #             self.rect.bottom = tile.rect.top
        #             #self.jump = False

        if self.rect.bottom > self.game.HEIGHT-30:
            self.rect.bottom = self.game.HEIGHT-30


        self.jumpCounter +=1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.jump == False and self.jumpCounter >35:
            self.vel_y = -self.SPEED*2.5
            self.jumpCounter = 0
            self.jump = True
            self.direction = "jump"
        if keys[pygame.K_SPACE] == False:
            self.jump = False
        if keys[pygame.K_LEFT]:
            self.rect.move_ip([-self.SPEED, 0])
            self.direction = "left"
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip([self.SPEED, 0])
            self.direction = "right"
        # if keys[pygame.K_s]:
        #     self.rect.move_ip([0, SPEED])

