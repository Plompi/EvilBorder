from tilemap import *
from player import *
import sys
import pygame
import json
from timer import *
from gameover import *

class Main:
    def __init__(self,win):
        self.__win = win
        self.__clock = pygame.time.Clock()
        self.__timer = Timer(self.__win)

        with open('assets/levels/levels.json', 'r') as f:
            self.__welt = json.load(f)[0]

        self.__map = Tilemap(self.__welt,self.__win)
        self.__tilemap = self.__map.getMap()
        self.__starttile = self.__map.getStartTile()[0]
        self.__playerstart = self.__map.getStartTile()[1]
        self.__player = Player(40,(self.__playerstart[0]*self.__map.getTilesize(),self.__playerstart[1]*self.__map.getTilesize()),self.__map.getTilesize(),self.__win)


    def playerinput(self):
        while True:
            for i in self.__tilemap:
                for j in i:
                    j.draw()
            self.__player.draw()
            self.__timer.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

                if event.type == pygame.MOUSEMOTION:
                    if self.__player.changePosition(pygame.mouse.get_pos()) == "wallCollision":
                        if not self.__player.getRect().colliderect(self.__starttile.getRect()):
                            self.__player.setdeaths()
                        self.__player.restart()

                    if self.check_map() == 'menu':
                        return

            self.__clock.tick(120)

    def check_map(self):
        for i in self.__tilemap:
            for j in i:
                name = j.getName()
                if name == 'w':
                    if self.__player.getRect().colliderect(j.getRect()):
                        if not self.__player.getRect().colliderect(self.__starttile.getRect()):
                            self.__player.setdeaths()
                        self.__player.restart()
                        
                if name == 'e':
                    if self.__player.getRect().colliderect(j.getRect()):
                        self.__player.setlevel()
                        try:
                            with open('assets/levels/levels.json', 'r') as f:
                                self.__welt = json.load(f)[self.__player.getlevel()]
                            self.__map = Tilemap(self.__welt,self.__win)
                            self.__tilemap = self.__map.getMap()

                            for numi,i in enumerate(self.__tilemap):
                                for numj,j in enumerate(i):
                                    if j.getName() == 's':
                                        self.__playerstart = (numj,numi)
                                        self.__starttile = j
                            self.__player.spawn_new_level((self.__playerstart[0]*self.__map.getTilesize(),self.__playerstart[1]*self.__map.getTilesize()))

                        except:
                            Gameover(self.__win,self.__timer.gettimer(),self.__player.getdeaths()).playerinput()
                            return 'menu'