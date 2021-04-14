from settings import *
from math import radians, cos, sin


class Object:
    def __init__(self, xy, ang):
        self.xy = xy
        self.angleD = ang
        self.angleR = radians(ang)

    def update(self):
        global FPS
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.rotate(-2)
        if keystate[pygame.K_d]:
            self.rotate(2)
        if keystate[pygame.K_w]:
            self.move(5, 5)
        if keystate[pygame.K_s]:
            self.move(-5, -5)
        if keystate[pygame.K_SPACE]:
            self.xy = [360, 360]

    def move(self, x, y):
        self.xy = [x * cos(self.angleR) + self.xy[0], y * sin(self.angleR) + self.xy[1]]

    def rotate(self, ang):
        self.angleD += ang
        if self.angleD >= 360:
            self.angleD %= 360
        if self.angleD <= 0:
            self.angleD += 360
        self.angleR = radians(self.angleD)
