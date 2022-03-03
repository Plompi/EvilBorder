import pygame

class Tile:
    def __init__(self,name:str,position,size,color,win):
        self.__win = win
        self.__name = name
        self.__x, self.__y = position[0]*size,position[1]*size
        self.__tile = pygame.Rect(self.__x,self.__y,size,size)
        self.__color = color

    def draw(self):
        pygame.draw.rect(self.__win,self.__color,self.__tile)

    def getName(self):
        return self.__name

    def getRect(self):
        return self.__tile