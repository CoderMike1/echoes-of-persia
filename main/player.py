import pygame.sprite,os

import Main
path = os.path.join(os.path.dirname(os.getcwd()), 'images\player')
print(path)
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 50
PLAYER_SCALE = 3
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

    def update(self):
        pass