import pygame

class Tile:
    def __init__(self,name:str,position,size,color,win):
        self.__win = win
        self.__name = name
        self.__tile = pygame.Rect(position[0]*size,position[1]*size,size,size)
        self.__color = color

    def draw(self):
        pygame.draw.rect(self.__win,self.__color,self.__tile)

    def getName(self):
        return self.__name

    def getRect(self):
        return self.__tile