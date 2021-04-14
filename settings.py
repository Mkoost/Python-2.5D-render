import pygame
from Object import Object

pygame.init()

player = Object([512, 360], 0)

BROWN = (150, 75, 0, 255)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
YELLOW = (255, 255, 0, 255)
GRAY = (128, 128, 128, 255)
PINK = (255, 41, 77, 255)
RUNNING = True
FPS = 60
DISTANCE = 720

mapp = ["##########",
        "#    #   #",
        "#    #   #",
        "##       #",
        "#        #",
        "#        #",
        "####     #",
        "#  #     #",
        "#     #  #",
        "##########", ]

HEIGHT, WIDTH = 720, 720
font = pygame.font.Font('files\\fonts\\JetBrainsMonoNL-ExtraBold.ttf', 24)

screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()
