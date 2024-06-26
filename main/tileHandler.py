import sys

import pygame,os,math

class Tile(pygame.sprite.Sprite):
    pathTiles = os.path.join(os.path.dirname(os.getcwd()), 'images','tiles')

    def __init__(self,image,c_x,c_y,col,row,name,scale=1):
        super().__init__()
        self.image = pygame.image.load(os.path.join(self.pathTiles,image)).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width() * scale, self.image.get_height() * scale))
        self.rect = self.image.get_rect()
        self.rect.center = c_x,c_y
        self.row = row
        self.col = col
        self.name = name

    def draw(self,surface):
        surface.blit(self.image,self.rect)

class healPotion(Tile):
    def __init__(self,c_x,c_y,currentMap):
        super().__init__("potion.png",c_x,c_y,c_x/48,c_y/48,"healPotion")

        self.image = pygame.transform.scale(self.image,(self.image.get_width() * 3, self.image.get_height() * 3))
        self.currentMap = currentMap
class wrongPotion(Tile):
    def __init__(self,c_x,c_y,currentMap):
        super().__init__("wrongpotion.png",c_x,c_y,c_x/48,c_y/48,"wrongPotion")

        self.image = pygame.transform.scale(self.image,(self.image.get_width() * 3, self.image.get_height() * 3))
        self.currentMap = currentMap
class Door(Tile):
    def __init__(self,c_x,c_y,currentMap,game):
        super().__init__("closedDoor.png", c_x, c_y, c_x / 48, c_y / 48, "Door")
        self.game = game
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2.5, self.image.get_height() * 2.5))
        self.currentMap = currentMap

        self.openable = False

        self.open = False


    def update(self):
        if self.game.player.direction == "right":
            distance =  math.hypot(self.game.player.rect.right - self.rect.right,
                              self.game.player.rect.top - self.rect.top)
        elif self.game.player.direction == "left":
            distance =  math.hypot(self.game.player.rect.left - self.rect.right,
                              self.game.player.rect.top - self.rect.top)


        if distance <50:
            self.openable = True
        else:
            self.openable = False

        if self.open:
            self.openDoor()


    def openDoor(self):

        self.image = pygame.image.load(os.path.join(self.pathTiles,"openDoor.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2.5, self.image.get_height() * 2.5))

class Key(Tile):
    def __init__(self,c_x,c_y,currentMap,game):
        super().__init__("key.png", c_x, c_y, c_x / 48, c_y / 48, "Key")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.currentMap = currentMap
        self.game = game

        self.pickable = False

    def update(self):
        if self.game.player.direction == "right":
            distance =  math.hypot(self.game.player.rect.right - self.rect.left,
                              self.game.player.rect.bottom - self.rect.top)
        elif self.game.player.direction == "left":
            distance =  math.hypot(self.game.player.rect.left - self.rect.right,
                              self.game.player.rect.bottom - self.rect.top)
        if distance <50:
            self.pickable = True
        else:
            self.pickable = False





class TileHandler(pygame.sprite.Sprite):
    pathMaps = os.path.join(os.path.dirname(os.getcwd()), 'images/maps')
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.tileMap = []
        self.mapname = None
        #self.all_sprites = pygame.sprite.Group()

        self.backgrounds = {
            0: pygame.image.load(os.path.join(self.pathMaps, 'background3.png')),
            1:pygame.image.load(os.path.join(self.pathMaps,'background1.png')),
            2: pygame.image.load(os.path.join(self.pathMaps, 'background2.png')),
            3: pygame.image.load(os.path.join(self.pathMaps, 'background3.png')),
        }


    def loadMap(self,mapName):
        self.mapname = mapName
        self.background = self.backgrounds[int(mapName.split("/")[1].strip(".txt"))%4]
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
                    self.tileMap.append(Tile('new1.png', col*self.game.PIXEL_SIZE,row*self.game.PIXEL_SIZE,col,row,"tile1",scale=3))
                if y == '2':
                    self.tileMap.append(
                        Tile('new2.png', col * self.game.PIXEL_SIZE, row * self.game.PIXEL_SIZE, col, row, "tile1",scale=3))
                    #self.all_sprites.add(Tile('tile1.png', col*self.game.PIXEL_SIZE,row*self.game.PIXEL_SIZE))
                if y == '3':
                    self.tileMap.append(
                        Tile('new3.png', col * self.game.PIXEL_SIZE, row * self.game.PIXEL_SIZE, col, row, "tile1",
                             scale=3))
                if y == '4':
                    self.tileMap.append(
                        Tile('new4.png', col * self.game.PIXEL_SIZE, row * self.game.PIXEL_SIZE, col, row, "tile1",
                             scale=3))

                if y == '5':
                    self.tileMap.append(
                        Tile('l2t1.png', col * self.game.PIXEL_SIZE, row * self.game.PIXEL_SIZE, col, row, "tile1",
                             scale=3))
                if y == '6':
                    self.tileMap.append(
                        Tile('l2t2.png', col * self.game.PIXEL_SIZE, row * self.game.PIXEL_SIZE, col, row, "tile1",
                             scale=3))

                if y == '7':
                    self.tileMap.append(
                        Tile('l2t3.png', col * self.game.PIXEL_SIZE, row * self.game.PIXEL_SIZE, col, row, "tile1",
                             scale=3))
                if y == '8':
                    self.tileMap.append(
                        Tile('l2t4.png', col * self.game.PIXEL_SIZE, row * self.game.PIXEL_SIZE, col, row, "tile1",
                             scale=3))
                if y == '9':
                    self.tileMap.append(
                        Tile('l2t5.png', col * self.game.PIXEL_SIZE, row * self.game.PIXEL_SIZE, col, row, "tile1",
                             scale=3))

                col +=1

            col = 0
            row +=1

    def draw(self,surface):
        surface.blit(self.background,(0,0))
        for tile in self.tileMap:
            tile.draw(surface)
