import pygame,os

import Main
path = os.path.join(os.path.dirname(os.getcwd()), 'images\player')
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 50
PLAYER_SCALE = 3
SPEED = 5

playerIMG = pygame.transform.scale(pygame.image.load(os.path.join(path,'playerIMG.png')),(PLAYER_WIDTH*PLAYER_SCALE,PLAYER_HEIGHT*PLAYER_SCALE))
#40x10
class Player(pygame.sprite.Sprite):
    def __init__(self,c_x,c_y):
        super().__init__()
        self.image = playerIMG
        self.rect = self.image.get_rect()
        self.rect.center = c_x,c_y

    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def update(self,keyPressed):
        if keyPressed[pygame.K_w]:
            self.rect.move_ip([0,-SPEED])
        if keyPressed[pygame.K_a]:
            self.rect.move_ip([-SPEED,0])
        if keyPressed[pygame.K_d]:
            self.rect.move_ip([SPEED,0])



        pass