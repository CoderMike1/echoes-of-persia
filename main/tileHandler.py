import sys

import pygame,os

class Tile(pygame.sprite.Sprite):
    pathTiles = os.path.join(os.path.dirname(os.getcwd()), 'images','tiles')

    def __init__(self,image,c_x,c_y,col,row,name):
        super().__init__()
        self.image = pygame.image.load(os.path.join(self.pathTiles,image)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = c_x,c_y
        self.row = row
        self.col = col
        self.name = name

    def draw(self,surface):
        surface.blit(self.image,self.rect)

class healPotion(Tile):
    def __init__(self,c_x,c_y,currentLevel):
        super().__init__("potion.png",c_x,c_y,c_x/48,c_y/48,"healPotion")

        self.image = pygame.transform.scale(self.image,(self.image.get_width() * 3, self.image.get_height() * 3))
        self.currentLevel = currentLevel
class Door(Tile):
    def __init__(self,c_x,c_y,currentLevel):
        super().__init__("closedDoor.png", c_x, c_y, c_x / 48, c_y / 48, "Door")

        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2.5, self.image.get_height() * 2.5))
        self.currentLevel = currentLevel


    def openDoor(self,game):
        game.sounds.playSound("openDoor")
        self.image = pygame.image.load(os.path.join(self.pathTiles,"openDoor.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2.5, self.image.get_height() * 2.5))

class TileHandler(pygame.sprite.Sprite):
    pathMaps = os.path.join(os.path.dirname(os.getcwd()), 'images/maps')
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.tileMap = []
        self.background = pygame.image.load(os.path.join(self.pathMaps,'background1.png'))
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
                    self.tileMap.append(Tile('tile1.png', col*self.game.PIXEL_SIZE,row*self.game.PIXEL_SIZE,col,row,"tile1"))
                    #self.all_sprites.add(Tile('tile1.png', col*self.game.PIXEL_SIZE,row*self.game.PIXEL_SIZE))
                col +=1

            col = 0
            row +=1

    def draw(self,surface):
        surface.blit(self.background,(0,0))
        for tile in self.tileMap:
            tile.draw(surface)
