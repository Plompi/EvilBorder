import pygame


class Player:
    def __init__(self,size,position,tilesize,win):
        self.__win = win
        self.__tilesize = tilesize
        self.__size = size
        self.__position = position
        pygame.mouse.set_pos((self.__position[0] + self.__tilesize/2,self.__position[1] + self.__tilesize/2))
        self.__player = pygame.Rect(self.__position[0]+self.__tilesize/2 - self.__size/2,self.__position[1]+self.__tilesize/2 - self.__size/2,self.__size,self.__size)
        self.__level = 0
        self.__deaths = 0

    def changePosition(self,pos):
        if pos[0] - self.__size/2 < 0 or pos[1] - self.__size/2 < 0 or pos[0] + self.__size/2 > self.__win.get_width() or pos[1] + self.__size/2 > self.__win.get_height():
            return "wallCollision"
        self.__x, self.__y = pos[0]-self.__size/2,pos[1]-self.__size/2
        self.__player = pygame.Rect(self.__x,self.__y,self.__size,self.__size)

    def draw(self):
        pygame.draw.rect(self.__win,"#44AF69",self.__player)

    def restart(self):
        pygame.mouse.set_pos((self.__position[0] + self.__tilesize/2,self.__position[1] + self.__tilesize/2))
        self.changePosition(pygame.mouse.get_pos())

    def getRect(self):
        return self.__player

    def getlevel(self):
        return self.__level

    def setlevel(self):
        self.__level += 1

    def spawn_new_level(self,pos):
        self.__position = pos
        pygame.mouse.set_pos((self.__position[0] + self.__tilesize/2,self.__position[1] + self.__tilesize/2))

    def setdeaths(self):
        self.__deaths += 1

    def getdeaths(self):
        return self.__deaths