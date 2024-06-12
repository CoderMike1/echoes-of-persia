
import pygame,abc
from enemy import EnemyEasy,EnemyMedium,EnemyHard
from trap import Blades
from tileHandler import healPotion,Door,Key,wrongPotion
class Level(abc.ABC):
    def __init__(self,game,currentMap):
        self.game = game
        self.currentMap = currentMap
        self.enemies = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.potions = pygame.sprite.Group()

        self.key =self.door  =None

        self.enemyList = {
            "EASY":EnemyEasy,
            "MEDIUM":EnemyMedium,
            "HARD":EnemyHard
        }
    def update(self,level):
        if self.game.player.rect.left < 0:
            self.currentMap -=1
            self.game.tileHandler.loadMap(f"level{level}/{self.currentMap}.txt")
            self.game.player.rect.right = self.game.WIDTH

        elif self.game.player.rect.right > self.game.WIDTH:
            self.currentMap +=1
            self.game.tileHandler.loadMap(f"level{level}/{self.currentMap}.txt")
            self.game.player.rect.left = 0

        elif self.game.player.rect.top > self.game.HEIGHT:
            self.currentMap += 10
            self.game.tileHandler.loadMap(f"level{level}/{self.currentMap}.txt")
            self.game.player.rect.top = 0

        for enemy in self.enemies:
            if enemy.currentMap == self.currentMap:
                enemy.update()

        for trap in self.traps:
            if trap.currentMap == self.currentMap:
                trap.update()

        self.door.update()
        self.key.update()

    def draw(self, surface):
        for enemy in self.enemies:
            if enemy.currentMap == self.currentMap:
                enemy.draw(surface)

        for trap in self.traps:
            if trap.currentMap == self.currentMap:
                trap.draw(surface)

        for potion in self.potions:
            if potion.currentMap == self.currentMap:
                potion.draw(surface)

        if self.key.currentMap == self.currentMap:
            self.key.draw(surface)

class Level1(Level):
    def __init__(self,game,currentMap):
        super().__init__(game,currentMap)
        self.potions.add(wrongPotion(5*48,9*48+4,0), healPotion(7*48,8*48+4,4), healPotion(15*48,8*48+4,11))

        self.traps.add(Blades(game,6*48,13*48+16,2),Blades(game,15*48,13*48+16,2), Blades(game,10*48,13*48+16,12))


        self.enemies.add(self.enemyList[self.game.difficult](game,12*48,13*48,3),self.enemyList[self.game.difficult](game,10*48,14*48,11))



        self.door = Door(9.3*48,11*48-6,13,game)



        self.key = Key(1*48,3*48+15,10,game)





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


        #self.enemies.add(EnemyEasy(game,900,100,11))
        #self.traps.add(Blades(game,500,640,11))


        self.potions.add(wrongPotion(15*48,672-44,11))
        self.potions.add(healPotion(4 * 48, 672 - 44, 11))
        self.door = Door(500,525,11,game)


        self.key = Key(300,645,11,game)




    def getLevel(self):
        return 1

    def update(self,level):
        for enemy in self.enemies:
            enemy.update()

        for trap in self.traps:
            trap.update()
        #
        self.door.update()
        self.key.update()

    def draw(self,surface):
        for enemy in self.enemies:
            enemy.draw(surface)

        for trap in self.traps:
            trap.draw(surface)

        for potion in self.potions:
            potion.draw(surface)

        self.key.draw(surface)