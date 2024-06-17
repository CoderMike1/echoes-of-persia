import time

import pygame,os
class Sound():
    path = os.path.join(os.path.dirname(os.getcwd()), 'sounds')
    def __init__(self):
        self.sounds = {}
        self.soundVolume = 1

        self.sounds.update({"playerPickUpSword":self.load_sounds("playerPickUpSword.ogg",0.5*self.soundVolume)})
        self.sounds.update({"swordHit":self.load_sounds("swordHit.ogg",0.5*self.soundVolume)})
        self.sounds.update({"swordSwing": self.load_sounds("swordSwing.ogg",0.5*self.soundVolume)})
        self.sounds.update({"playerGetDamage": self.load_sounds("playerGetDamage.wav",0.5*self.soundVolume)})
        self.sounds.update({"enemyGetDamage": self.load_sounds("enemyGetDamage.ogg",0.5*self.soundVolume)})
        self.sounds.update({"playerHideSword": self.load_sounds("playerHideSword.ogg",0.5*self.soundVolume)})

        self.sounds.update({"enemyDead": self.load_sounds("enemyDead.mp3",1*self.soundVolume)})
        self.sounds.update({"climb": self.load_sounds("climb.ogg", 1*self.soundVolume)}) # tez do sprawdzenia
        self.sounds.update({"healing": self.load_sounds("healing.wav", 1*self.soundVolume)})
        self.sounds.update({"drinking": self.load_sounds("drinking.mp3", 1*self.soundVolume)})
        self.sounds.update({"trapDeploy": self.load_sounds("trapDeploy.mp3", 0.5*self.soundVolume)})
        self.sounds.update({"trapHide": self.load_sounds("trapHide.mp3", 0.5*self.soundVolume)})
        self.sounds.update({"stabbed": self.load_sounds("stabbed.wav", 0.5*self.soundVolume)})
        self.sounds.update({"openDoor": self.load_sounds("opendoor.mp3", 0.5*self.soundVolume)})
        self.sounds.update({"getKey": self.load_sounds("collectKey.mp3", 0.5*self.soundVolume)})

        self.sounds.update({"1level": self.load_sounds("firstLevel.mp3", 0.6 * self.soundVolume)})

        self.sounds.update({"music": self.load_sounds("music.mp3", 0.3 * self.soundVolume)})
        self.sounds.update({"music2": self.load_sounds("music2.mp3", 0.4 * self.soundVolume)})
        self.sounds.update({"menuMusic": self.load_sounds("menuMusic.mp3", 0.4 * self.soundVolume)})
        self.sounds.update({"gameover": self.load_sounds("gameover.mp3", 0.8 * self.soundVolume)})
        self.sounds.update({"nextLevel": self.load_sounds("nextLevel.mp3", 0.8 * self.soundVolume)})
        self.sounds.update({"gamewin": self.load_sounds("gamewin.mp3", 0.5 * self.soundVolume)})

        pygame.mixer.init()

    def load_sounds(self,fileName,volume):
        sound = pygame.mixer.Sound(os.path.join(self.path,fileName))
        sound.set_volume(volume)
        return sound

    def playSound(self,fileName):
        print(f"leci {fileName}")
        if fileName == "music" or fileName == "menuMusic" or fileName == "music2":
            self.sounds[fileName].play(loops=-1)
        else:
            self.sounds[fileName].play()

    def stopSound(self,fileName):
        print(f"stopujemy {fileName}")
        self.sounds[fileName].stop()
