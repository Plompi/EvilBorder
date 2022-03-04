import sys
import pygame
from button import *
from main import *
from editor import *

class Menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Evil Border')
        self.__standardcursor = pygame.mouse.get_cursor()
        self.__win = pygame.display.set_mode((700,700))
        self.__clock = pygame.time.Clock()
        self.__selected = 1
        self.__buttons = [
            Button('EVIL BORDER',100,(self.__win.get_width()/2,self.__win.get_height()/2-300),self.__win,1),
            Button('PLAY',100,(self.__win.get_width()/2,self.__win.get_height()/2-80),self.__win,-1),
            Button('EDITOR',100,(self.__win.get_width()/2,self.__win.get_height()/2),self.__win,1),
            Button('QUIT',100,(self.__win.get_width()/2,self.__win.get_height()/2+80),self.__win,1)
        ]

    def start(self):
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.__selected != 1:
                                self.__buttons[self.__selected-1].setSelected()
                                self.__buttons[self.__selected].setSelected()
                                self.__selected -=1

                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.__selected != 3:
                                self.__buttons[self.__selected+1].setSelected()
                                self.__buttons[self.__selected].setSelected()
                                self.__selected +=1



                    if event.key == pygame.K_RETURN:
                        if self.__selected == 1:
                            Main(self.__win,self.__standardcursor).playerinput()

                        if self.__selected == 2:
                            Editor(self.__win).createMap()

                        if self.__selected == 3:
                            pygame.quit()
                            sys.exit()

            self.__win.fill('#242933')

            for i in self.__buttons:
                i.draw()
            pygame.display.flip()
            self.__clock.tick(120)

if __name__ == "__main__":
    menu = Menu()
    menu.start()