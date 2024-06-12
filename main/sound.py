import time

import pygame,os
class Sound():
    path = os.path.join(os.path.dirname(os.getcwd()), 'sounds')
    def __init__(self):
        self.sounds = {}

        self.sounds.update({"playerPickUpSword":self.load_sounds("playerPickUpSword.ogg",0.5)})
        self.sounds.update({"swordHit":self.load_sounds("swordHit.ogg",0.5)})
        self.sounds.update({"swordSwing": self.load_sounds("swordSwing.ogg",0.5)})
        self.sounds.update({"playerGetDamage": self.load_sounds("playerGetDamage.wav",0.5)})
        self.sounds.update({"enemyGetDamage": self.load_sounds("enemyGetDamage.ogg",0.5)})
        self.sounds.update({"playerHideSword": self.load_sounds("playerHideSword.ogg",0.5)})

        self.sounds.update({"enemyDead": self.load_sounds("enemyDead.mp3",1)})
        self.sounds.update({"climb": self.load_sounds("climb.ogg", 1)}) # tez do sprawdzenia
        self.sounds.update({"healing": self.load_sounds("healing.wav", 1)})
        self.sounds.update({"drinking": self.load_sounds("drinking.mp3", 1)})
        self.sounds.update({"trapDeploy": self.load_sounds("trapDeploy.mp3", 0.5)})
        self.sounds.update({"trapHide": self.load_sounds("trapHide.mp3", 0.5)})
        self.sounds.update({"stabbed": self.load_sounds("stabbed.wav", 0.5)})
        self.sounds.update({"openDoor": self.load_sounds("opendoor.mp3", 0.5)})
        self.sounds.update({"getKey": self.load_sounds("collectKey.mp3", 0.5)})

        pygame.mixer.init()

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
