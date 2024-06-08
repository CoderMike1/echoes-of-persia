import time

import pygame,os
class Sound():
    path = os.path.join(os.path.dirname(os.getcwd()), 'sounds')
    def __init__(self):
        self.sounds = {}

        self.sounds.update({"playerPickUpSword":self.load_sounds("playerPickUpSword.ogg",0.5)})
        self.sounds.update({"swordHit":self.load_sounds("swordHit.ogg",0.5)})
        self.sounds.update({"swordSwing": self.load_sounds("swordSwing.ogg",0.5)})
        self.sounds.update({"playerGetDamage": self.load_sounds("playerGetDamage.ogg",0.5)})
        self.sounds.update({"enemyGetDamage": self.load_sounds("enemyGetDamage.ogg",0.5)})
        self.sounds.update({"playerHideSword": self.load_sounds("playerHideSword.ogg",0.5)})
        #playergetdamage, ten dzwiek do zmiany albo do sprawdzenia bo nie dziala

        self.sounds.update({"enemyDead": self.load_sounds("enemyDead.mp3",1)})
        self.sounds.update({"climb": self.load_sounds("climb.wav", 1)}) # tez do sprawdzenia
        self.sounds.update({"healing": self.load_sounds("healing.wav", 1)})
        self.sounds.update({"drinking": self.load_sounds("drinking.mp3", 1)})
        self.sounds.update({"trapDeploy": self.load_sounds("trapDeploy.mp3", 1)})
        self.sounds.update({"trapHide": self.load_sounds("trapHide.mp3", 1)})

        pygame.mixer.init()
        pygame.mixer.set_num_channels(8)


    def load_sounds(self,fileName,volume):
        sound = pygame.mixer.Sound(os.path.join(self.path,fileName))
        sound.set_volume(volume)
        return sound

    def playSound(self,fileName):
        print(f"leci {fileName}")
        self.sounds[fileName].play()

    def stopSound(self,fileName):
        print(f"stopujemy {fileName}")
        self.sounds[fileName].stop()
