import pygame
import sys
from button import *
from main import *


class Gameover:
    def __init__(self,win,time,deaths):
        self.__win = win
        self.__clock = pygame.time.Clock()
        self.__selected = 1
        self.__buttons = [
            Button(f'{time}s | {deaths} Tode',100,(self.__win.get_width()/2,self.__win.get_height()/2-300),self.__win,1),
            Button('MENU',100,(self.__win.get_width()/2,self.__win.get_height()/2),self.__win,-1),
            Button('QUIT',100,(self.__win.get_width()/2,self.__win.get_height()/2+80),self.__win,1)
        ]
    def playerinput(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.__selected != 1:
                        self.__buttons[self.__selected-1].setSelected()
                        self.__buttons[self.__selected].setSelected()
                        self.__selected -=1

                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.__selected != 2:
                        self.__buttons[self.__selected+1].setSelected()
                        self.__buttons[self.__selected].setSelected()
                        self.__selected +=1

                    if event.key == pygame.K_RETURN:
                        if self.__selected == 1:
                            return

                        if self.__selected == 2:
                            pygame.quit()
                            sys.exit()

            self.__win.fill('#242933')
            for i in self.__buttons:
                i.draw()

            self.__clock.tick(120)
            pygame.display.flip()