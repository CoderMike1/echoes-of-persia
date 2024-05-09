import sys

import pygame,os
import Main
pathTiles = os.path.join(os.path.dirname(os.getcwd()), 'images/tiles')
pathMaps = os.path.join(os.path.dirname(os.getcwd()), 'images/maps')
class Tile(pygame.sprite.Sprite):
    def __init__(self,image,c_x,c_y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(pathTiles,image))
        self.rect = self.image.get_rect()
        self.rect.center = c_x,c_y

    def draw(self,surface):
        surface.blit(self.image,self.rect)


class TileHandler(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tileMap = []
        self.all_sprites = pygame.sprite.Group()


    def loadMap(self,mapName):
        map = []
        with open(os.path.join(pathMaps,mapName) ,"r") as file:
            reader = file.readlines()
            for x in reader:
                map.append(x.split())

        row = 0
        col = 0
        for x in map:
            for y in x:
                if y == '1':
                    self.tileMap.append(Tile('tile1.png', col*Main.PIXEL_SIZE,row*Main.PIXEL_SIZE))
                    self.all_sprites.add(Tile('tile1.png', col*Main.PIXEL_SIZE,row*Main.PIXEL_SIZE))
                col +=1

            col = 0
            row +=1

    def draw(self,surface):
        for tile in self.tileMap:
            tile.draw(surface)
        pass





