import pygame


class UI:
    def __init__(self,color):
        self.color = color

    def draw(self,surface):
        surface.fill(self.color)
        pass

    def update(self):
        pass

