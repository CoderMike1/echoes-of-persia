import sys

import pygame,os

class Tile(pygame.sprite.Sprite):
    pathTiles = os.path.join(os.path.dirname(os.getcwd()), 'images','tiles')

    def __init__(self,image,c_x,c_y,col,row):
        super().__init__()
        self.image = pygame.image.load(os.path.join(self.pathTiles,image)).convert()
        self.rect = self.image.get_rect()
        self.rect.center = c_x,c_y
        self.row = row
        self.col = col

    def draw(self,surface):
        surface.blit(self.image,self.rect)


class TileHandler(pygame.sprite.Sprite):
    pathMaps = os.path.join(os.path.dirname(os.getcwd()), 'images/maps')
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.tileMap = []
        #self.all_sprites = pygame.sprite.Group()


    def loadMap(self,mapName):
        self.tileMap.clear()
        map = []
        with open(os.path.join(self.pathMaps,mapName) ,"r") as file:
            reader = file.readlines()
            for x in reader:
                map.append(x.split())

        row = 0
        col = 0
        for x in map:
            for y in x:
                if y == '1':
                    self.tileMap.append(Tile('tile1.png', col*self.game.PIXEL_SIZE,row*self.game.PIXEL_SIZE,col,row))
                    #self.all_sprites.add(Tile('tile1.png', col*self.game.PIXEL_SIZE,row*self.game.PIXEL_SIZE))
                col +=1

            col = 0
            row +=1

    def draw(self,surface):
        for tile in self.tileMap:
            tile.draw(surface)
        pass
