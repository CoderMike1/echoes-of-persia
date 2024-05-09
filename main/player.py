import pygame.sprite,os

import Main
path = os.path.join(os.path.dirname(os.getcwd()), 'images\player')
print(path)
playerIMG = pygame.image.load(os.path.join(path,'playerIMG.png'))

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