
import pygame,abc
from enemy import EnemyEasy,EnemyMedium,EnemyHard
from trap import Blades
from tileHandler import healPotion
class Level(abc.ABC):
    def __init__(self,game,currentMap):
        self.game = game
        self.currentMap = currentMap
        self.enemies = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.potions = pygame.sprite.Group()
    def update(self,level):
        if self.game.player.rect.left < 0:
            self.currentMap -=1
            self.game.tileHandler.loadMap(f"level{level}/map{self.currentMap}.txt")
            self.game.player.rect.right = self.game.WIDTH

        elif self.game.player.rect.right > self.game.WIDTH:
            self.currentMap +=1
            self.game.tileHandler.loadMap(f"level{level}/map{self.currentMap}.txt")
            self.game.player.rect.left = 0

        for enemy in self.enemies:
            if enemy.currentMap == self.currentMap:
                enemy.update()

        for trap in self.traps:
            if trap.currentMap == self.currentMap:
                trap.update()

    def draw(self, surface):
        for enemy in self.enemies:
            if enemy.currentMap == self.currentMap:
                enemy.draw(surface)

        for trap in self.traps:
            if trap.currentMap == self.currentMap:
                trap.draw(surface)

class Level1(Level):
    def __init__(self,game,currentMap):
        super().__init__(game,currentMap)

        self.enemies.add(EnemyEasy(game,400,6*48,11))
        self.traps.add(Blades(game, 300, 640,10))


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


        #self.enemies.add(EnemyEasy(game,200,100,11))
        self.traps.add(Blades(game,700,640,11))


        self.potions.add(healPotion(12*48,672-44,11))


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

        for potion in self.potions:
            potion.draw(surface)