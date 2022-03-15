import pygame
from tiles import *

class Tilemap:
    def __init__(self,levelmap,win):
        self.__size = win.get_height()/len(levelmap)
        self.__tilemap = [[] for i in range (len(levelmap))]
        self.__colors = {   'w':'#242933',
                            'p':'#FFFFFF',
                            's':"#470FF4",
                            'e':"#CE2D4F"}

        for numi,i in enumerate(levelmap):
            for numj, j in enumerate(i):
                self.__tilemap[numi].append(Tile(j,[numj,numi],self.__size,self.__colors[j],win))
                if j == 's':
                    self.__start = (self.__tilemap[-1][-1],(numj,numi))

    def getMap(self):
        return self.__tilemap

    def getTilesize(self):
        return self.__size

    def getStartTile(self):
        return self.__start