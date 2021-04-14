from settings import *
from random import randint
from math import tan as tg, cos, sin, degrees, pi, radians


def raycasting(sP, eP, angD):
    angR = radians(angD)
    xm, ym = 0, 0
    ct1, ct2 = False, False
    xd = (sP[0] // 72) * 72
    yd = (sP[1] // 72) * 72
    a_cos = cos(angR) if cos(angR) else 0.0000001
    a_sin = sin(angR) if sin(angR) else 0.0000001

    if 270 <= angD <= 360 or 0 <= angD <= 90:
        xd += 72
        for i in range(int(abs(sP[0] - eP[0]) // 72) + 1):
            dist = abs(xd - sP[0]) / a_cos
            y = dist * a_sin + sP[1]
            if xd // 72 > 9:
                xd = 648
            if xd // 72 < 0:
                xd = 0
            try:
                if mapp[int(y // 72)][int(abs(xd + sP[0] - (sP[0] // 72) * 72) // 72)] != ' ' and abs(dist) <= DISTANCE:
                    ct1 = True
                    break
            except IndexError:
                pass

            xd += 72
    else:
        for i in range(int(abs(eP[0] - sP[0]) // 72) + 1):
            dist = ((sP[0] - xd) / a_cos)
            y = sP[1] - dist * a_sin
            if xd // 72 > 9:
                xd = 648
            if xd // 72 < 0:
                xd = 72
            try:
                if mapp[int(y // 72)][int(abs(xd - sP[0] + (sP[0] // 72) * 72) // 72)] != ' ' and abs(dist) <= DISTANCE:
                    ct1 = True
                    break
            except IndexError:
                pass

            xd -= 72
    if 180 >= angD >= 0:
        yd += 72
        for i in range(int(abs(sP[1] - eP[1]) // 72) + 1):
            dist = abs(yd - sP[1]) / a_sin
            x = dist * a_cos + sP[0]
            if yd // 72 > 9:
                yd = 648
            if yd // 72 < 0:
                yd = 0
            try:
                if mapp[int(abs(yd + sP[1] - (sP[1] // 72) * 72) // 72)][int(x // 72)] != ' ' and abs(dist) <= DISTANCE:
                    ct2 = True

                    break
            except IndexError:
                pass

            yd += 72
    else:
        for i in range(int(abs(eP[1] - sP[1]) // 72) + 1):
            dist = ((sP[1] - yd) / a_sin)
            x = sP[0] - dist * a_cos
            if yd // 72 > 9:
                yd = 648
            if yd // 72 < 0:
                yd = 72
            try:
                if mapp[int(abs(yd - sP[1] + (sP[1] // 72) * 72) // 72)][int(x // 72)] != ' ' and abs(dist) <= DISTANCE:
                    ct2 = True
                    break
            except IndexError:
                pass

            yd -= 72
    num = None
    if ct2:
        if (((sP[0] - xd) ** 2 + (sP[1] - y) ** 2) ** 0.5 <= ((sP[0] - x) ** 2 + (sP[1] - yd) ** 2) ** 0.5) and ct1:
            # pygame.draw.circle(screen, RED, [xd, y], 5)
            num = [xd, y, ((sP[0] - xd) ** 2 + (sP[1] - y) ** 2) ** 0.5]
        else:
            # pygame.draw.circle(screen, RED, [x, yd], 5)
            num = [x, yd, ((sP[0] - x) ** 2 + (sP[1] - yd) ** 2) ** 0.5]
    elif ct1:
        # pygame.draw.circle(screen, RED, [xd, y], 5)
        num = [xd, y, ((sP[0] - xd) ** 2 + (sP[1] - y) ** 2) ** 0.5]

    return int(num[0] * cos(player.angleR-angR)), int(num[1] * cos(player.angleR-angR)), num[2]