import pygame
import sys
import json
from tilemap import *

class Editor:
    def __init__(self,win):
        self.__win = win
        self.__clock = pygame.time.Clock()
        self.__tiles = [['p',"#FFFFFF"],['s',"#470FF4"],['e',"#CE2D4F"]]
        self.__index = 0
        self.__worldindex = -1
        self.__click = False
        self.__delete = False
        self.__map = [  ["w","w","w","w","w","w","w","w","w","w"],
                        ["w","w","w","w","w","w","w","w","w","w"],
                        ["w","w","w","w","w","w","w","w","w","w"],
                        ["w","w","w","w","w","w","w","w","w","w"],
                        ["w","w","w","w","w","w","w","w","w","w"],
                        ["w","w","w","w","w","w","w","w","w","w"],
                        ["w","w","w","w","w","w","w","w","w","w"],
                        ["w","w","w","w","w","w","w","w","w","w"],
                        ["w","w","w","w","w","w","w","w","w","w"],
                        ["w","w","w","w","w","w","w","w","w","w"]]

    def createMap(self):
        while True:
            if self.__worldindex == -1:
                if self.__click == True:
                    if self.__map[self.__tile[1]][self.__tile[0]] == 'w' or (self.__map[self.__tile[1]][self.__tile[0]] == 'p' and self.__index != 0):
                        self.__map[self.__tile[1]][self.__tile[0]] = self.__tiles[self.__index][0]
                        if self.__index == 1 and ['s',"#470FF4"] in self.__tiles:
                            self.__tiles.remove(['s',"#470FF4"])
                            self.__index = 0
                            self.__click = False
                        if self.__index == 2 and ['e',"#CE2D4F"] in self.__tiles or (self.__index == 1 and ['s',"#470FF4"] not in self.__tiles):
                            self.__tiles.remove(['e',"#CE2D4F"])
                            self.__index = 0
                            self.__click = False

                if self.__delete == True:
                    if self.__map[self.__tile[1]][self.__tile[0]] == 's':
                        self.__tiles.insert(1,['s',"#470FF4"])
                    if self.__map[self.__tile[1]][self.__tile[0]] == 'e':
                        self.__tiles.append(['e',"#CE2D4F"])
                    self.__map[self.__tile[1]][self.__tile[0]] = 'w'
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.__worldindex >= -1:
                    if (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                        self.__direction = 1
                    elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.__worldindex >= 0:
                        self.__direction = -1
                    else:
                        break
                    try:
                        with open('assets/levels/levels.json', 'r') as f:
                            self.__welt = json.load(f)[self.__worldindex+self.__direction]

                        self.__map1 = Tilemap(self.__welt,self.__win)
                        self.__tilemap = self.__map1.getMap()
                        self.__worldindex += self.__direction
                    except:
                        break

                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and self.__worldindex >= -1:
                    try:
                        with open("assets/levels/levels.json",'r') as level:
                            self.__file_data = json.load(level)
                        self.__file_data.pop(self.__worldindex)
                        with open("assets/levels/levels.json",'w') as level:
                            json.dump(self.__file_data, level)
                    except:
                        self.__worldindex = -1

                    if len(self.__file_data) < self.__worldindex+1:
                        self.__worldindex -=1

                    try:
                        with open('assets/levels/levels.json', 'r') as f:
                            self.__welt = json.load(f)[self.__worldindex]

                        self.__map1 = Tilemap(self.__welt,self.__win)
                        self.__tilemap = self.__map1.getMap()
                    except:
                        break

                if self.__worldindex == -1:

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        with open("assets/levels/levels.json",'r') as level:
                            self.__file_data = json.load(level)
                        self.__file_data.append(self.__map)
                        with open("assets/levels/levels.json",'w') as level:
                            json.dump(self.__file_data, level)
                        return

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.__click = True

                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        self.__click = False
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                        self.__delete = True
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                        self.__delete = False
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                        if self.__index != len(self.__tiles):
                            self.__index += 1
                        if self.__index == len(self.__tiles):
                            self.__index = 0

            if self.__worldindex == -1:
                self.__tile = (pygame.mouse.get_pos()[0]//70,pygame.mouse.get_pos()[1]//70)
                self.__win.fill('#242933')

                s = pygame.Surface((70,70)) 
                s.set_alpha(40)                
                s.fill(self.__tiles[self.__index][1])     

                for numi,i in enumerate(self.__map):
                    for numj, j in enumerate(i):
                        if j == "p":
                            pygame.draw.rect(self.__win,(255,255,255),pygame.Rect(numj*70,numi*70,70,70))

                        if j == "s":
                            pygame.draw.rect(self.__win,"#470FF4",pygame.Rect(numj*70,numi*70,70,70))

                        if j == "e":
                            pygame.draw.rect(self.__win,"#CE2D4F",pygame.Rect(numj*70,numi*70,70,70))

                self.__win.blit(s, (self.__tile[0]*70,self.__tile[1]*70))

            if self.__worldindex >= 0:
                for i in self.__tilemap:
                    for j in i:
                        j.draw()

            pygame.display.flip()

            self.__clock.tick(120)