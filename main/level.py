
import pygame,abc
from enemy import EnemyEasy
from trap import Blades
class Level(abc.ABC):
    def __init__(self,game,currentMap):
        self.game = game
        self.currentMap = currentMap
        self.enemies = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
    def update(self,level):
        if self.game.player.rect.left < 0:
            self.currentMap -=1
            self.game.tileHandler.loadMap(f"level{level}/map{self.currentMap}.txt")
            self.game.player.rect.right = self.game.WIDTH

        elif self.game.player.rect.right > self.game.WIDTH:
            self.currentMap +=1
            self.game.tileHandler.loadMap(f"level{level}/map{self.currentMap}.txt")
            self.game.player.rect.left = 0


        if self.game.ui.playerLifes < 1:
            print("game over")

class Level1(Level):
    def __init__(self,game,currentMap):
        super().__init__(game,currentMap)


    def getLevel(self):
        return 1


class Level2(Level):
    def __init__(self,game,currentMap):
        super().__init__(game,currentMap)

    def getLevel(self):
        return 2



class WorkingLevel(Level):
    def __init__(self,game,currentMap):
        super().__init__(game,currentMap)


        #self.enemies.add(EnemyEasy(game,800,100))
        self.traps.add(Blades(game,300,640))




    def getLevel(self):
        return 1

    def update(self,level):
        for enemy in self.enemies:
            enemy.update()

        for trap in self.traps:
            trap.update()

    def draw(self,surface):
        for enemy in self.enemies:
            enemy.draw(surface)

        for trap in self.traps:
            trap.draw(surface)