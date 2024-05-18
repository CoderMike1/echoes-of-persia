
import pygame

class Level:
    def __init__(self,game,currentMap):
        self.game = game
        self.currentMap = currentMap

    def update(self,level):
        if self.game.player.rect.left < 0:
            self.currentMap -=1
            self.game.tileHandler.loadMap(f"level{level}/map{self.currentMap}.txt")
            self.game.player.rect.right = self.game.WIDTH

        elif self.game.player.rect.right > self.game.WIDTH:
            self.currentMap +=1
            self.game.tileHandler.loadMap(f"level{level}/map{self.currentMap}.txt")
            self.game.player.rect.left = 0

class Level1(Level):
    def __init__(self,game,currentMap):
        super().__init__(game,currentMap)


    def getLevel(self):
        return 1


class Level2(Level):
    pass