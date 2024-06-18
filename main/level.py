
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

        #tymczasowo klucz obok drzwi
        #self.key = Key(3 * 48, 13 * 48 + 15, 13, game)



        self.key = Key(1*48,3*48+15,10,game)





    def getLevel(self):
        return 1


class Level2(Level):
    def __init__(self,game,currentMap):
        super().__init__(game,currentMap)


        self.traps.add(Blades(game,9.5*48,13.3*48+3,10),Blades(game,5*48,7.3*48+3,13),
                       Blades(game,13.5*48,11.3*48+3,13),Blades(game,16.5*48,13.3*48+3,12),
                       Blades(game,13.5*48,13.3*48+3,12),Blades(game,10.5*48,13.3*48+3,12),
                       Blades(game,7.5*48,13.3*48+3,12),Blades(game,4.5*48,13.3*48+3,12),
                       Blades(game,1.5*48,13.3*48+3,12),Blades(game,15.5*48,13.3*48,21))
        self.potions.add(healPotion(5*48,8*48+6,2),wrongPotion(3*48,8*48+6,0))

        self.enemies.add(self.enemyList[self.game.difficult](game, 11 * 48, 13 * 48, 12),
                         self.enemyList[self.game.difficult](game, 11 * 48, 13 * 48, 22),
                         self.enemyList[self.game.difficult](game, 4 * 48, 13 * 48, 21) )


        self.door = Door(10 * 48, 11 * 48 - 6, 20, game)

        #tymczasowy klucz
        #self.key = Key(6 * 48, 13 * 48 + 15, 20, game)




        self.key = Key(6 * 48, 9 * 48 + 15, 22, game)


    def getLevel(self):
        return 2
