import sys,pygame,math
from pygame.locals import *
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

Display_width = 800
Display_height = 600

FPS = 80
def BG(x,y):
    global Display, BackGround
    Display.blit(BackGround, (x,y))

def Airplane(x,y):
    global Display, Aircraft
    Display.blit(Aircraft,(x,y))

def RunGame():
    global Display,Aircraft,Clock,BackGround

    x = Display_width * 0.05
    y = Display_height * 0.8
    y_change = 0

    BackGround_x = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == QUIT:
                crahsed = True
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.K_DOWN:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0
        y += y_change

        Display.fill(WHITE)
        BG(BackGround_x, 0)
        Airplane(x,y)
        pygame.display.update()
        Clock.tick(FPS)

    pygame.quit()
    quit()

def initGame():
    global Display,Aircraft,Clock,BackGround

    pygame.init()
    Display = pygame.display.set_mode((Display_width,Display_height))
    pygame.display.set_caption('슈팅스타')
    Aircraft = pygame.image.load('AirPlane_1.png')
    BackGround = pygame.image.load('Galaxy.png')

    Clock = pygame.time.Clock()
    RunGame()

if __name__=='__main__':
    initGame()