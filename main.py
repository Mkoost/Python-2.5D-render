import pygame
from settings import *
import sys
from math import cos, sin, radians
from raycasting import raycasting

pygame.init()


def terminate():
    pygame.quit()
    sys.exit()


def main():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    player.update()

    screen.fill(BLACK)
    # for i in range(len(mapp)):
    #     for j in range(len(mapp[i])):
    #         if mapp[i][j] != ' ':
    #             pygame.draw.rect(screen, WHITE, (
    #             int(HEIGHT / len(mapp[i])) * j, int(HEIGHT / len(mapp[i])) * i, int(HEIGHT / len(mapp[i])),
    #             int(HEIGHT / len(mapp[i]))), 5)
    #         else:
    #             pygame.draw.rect(screen, BLUE, (
    #                 int(HEIGHT / len(mapp[i])) * j, int(HEIGHT / len(mapp[i])) * i, int(HEIGHT / len(mapp[i])),
    #                 int(HEIGHT / len(mapp[i]))), 1)
    screen.fill(GRAY, [0, 360, 720, 360])
    screen.fill(BLUE, [0, 0, 720, 360])
    for i in range(400):
        ang = player.angleD - 22.5 + 0.1125 * i
        if ang >= 360:
            ang %= 360
        if ang <= 0:
            ang += 360
        pos = raycasting(player.xy, [int(DISTANCE * cos(radians(ang))) + player.xy[0],
                                     int(DISTANCE * sin(radians(ang))) + player.xy[1]], ang)

        if pos is not None:
            # pygame.draw.line(screen, RED, player.xy,
            #                  [pos[0], pos[1]])
            d = 720 * (DISTANCE / pos[2] * 0.1) / 2
            color = [int(255 * (1 - pos[2] / DISTANCE)), int(255 * (1 - pos[2] / DISTANCE)),
                     255]
            pygame.draw.line(screen, color, [int(i * 1.8), 360], [int(i * 1.8), int(360 - d)], 2)
            pygame.draw.line(screen, color, [int(i * 1.8), 360], [int(i * 1.8), int(360 + d)], 2)
    # pygame.draw.circle(screen, GREEN, player.xy, 5)
    text_fps = font.render(str(int(clock.get_fps())), False, WHITE)
    screen.blit(text_fps,  [680, 10])
    pygame.display.flip()
    clock.tick(FPS)


while RUNNING:
    main()

terminate()
