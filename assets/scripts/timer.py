import pygame

class Timer:
    def __init__(self,win):
        self.__win = win
        self.__timerstart = pygame.time.get_ticks()
        self.__font = pygame.font.SysFont(None,30)

    def draw(self):
        self.__timer = round((pygame.time.get_ticks() - self.__timerstart)/1000,2)
        self.__renderedfont = self.__font.render(f'{self.__timer}s',True,"#4056F4")
        self.__win.blit(self.__renderedfont,(10,10))

    def gettimer(self):
        return self.__timer