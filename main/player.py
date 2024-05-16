import pygame,os
class Player(pygame.sprite.Sprite):
    path = os.path.join(os.path.dirname(os.getcwd()), 'images\player')
    PLAYER_WIDTH = 15
    PLAYER_HEIGHT = 50
    PLAYER_SCALE = 3
    SPEED = 5
    playerIMG = pygame.transform.scale(pygame.image.load(os.path.join(path, 'playerIMG.png')),
                                       (PLAYER_WIDTH * PLAYER_SCALE, PLAYER_HEIGHT * PLAYER_SCALE))
    def __init__(self,game,x,y):
        super().__init__()
        self.game = game
        self.rect = self.playerIMG.get_rect()
        self.rect.center = x,y

    def draw(self,surface):
        surface.blit(self.playerIMG,self.rect)

    def update(self):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     self.rect.move_ip([0, -SPEED])
        if keys[pygame.K_LEFT]:
            self.rect.move_ip([-self.SPEED, 0])
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip([self.SPEED, 0])
        # if keys[pygame.K_s]:
        #     self.rect.move_ip([0, SPEED])