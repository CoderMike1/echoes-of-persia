import pygame,os,abc

class Enemy(pygame.sprite.Sprite,abc.ABC):
    path = os.path.join(os.path.dirname(os.getcwd()), 'images', 'enemy')
    ENEMY_SCALE = 3
    def __init__(self,game,lives,speed,imageName,cx,cy):
        super().__init__()
        self.game = game
        self.enemyLives = lives
        self.enemySpeed = speed
        self.image = pygame.image.load(os.path.join(self.path,f"{imageName}EnemyIdle.png"))
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*self.ENEMY_SCALE,self.image.get_height()*self.ENEMY_SCALE))
        self.rect = self.image.get_rect()
        self.rect.center = (cx,cy)

    @abc.abstractmethod
    def attack(self):
        pass
    @abc.abstractmethod
    def defend(self):
        pass

    def draw(self,surface):
        surface.blit(self.image,self.rect)

class EnemyEasy(Enemy):
    def __init__(self,game,cx,cy):
        super().__init__(game,3,2,"easy",cx,cy)

    def attack(self):
        pass

    def defend(self):
        pass

