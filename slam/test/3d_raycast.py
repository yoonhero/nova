import numpy as np
from matplotlib import pyplot as plt
import keyboard
import pygame
import time
import sys
from pygame.locals import QUIT

pygame.init()

mepa = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]]


class Minimap():
    def __init__(self, map, posx, posy, exitx, exity):
        self.map = map

        self.exitx = exitx
        self.exity = exity

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        self.size = (100*len(map[0]), 100*len(map))

        self.w = 100*len(map[0])
        self.h = 100*len(map)

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("3d Ray Casting")
        self.draw_map(posx, posy)
        self.screen.fill(self.WHITE)

        self.FPSCLOCK = pygame.time.Clock()

    def draw_map(self, posx, posy):
        self.screen.fill(self.WHITE)

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] != 0:
                    self.draw_rect(i, j)
        self.draw_rect(self.exitx, self.exity, self.BLUE)
        self.draw_circle(posx, posy)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # pygame.time.Clock().tick(30)
        pygame.display.update()

    def draw_rect(self, x, y, c=(0, 0, 0)):
        pygame.draw.rect(self.screen, c,
                         pygame.Rect([x*100, y*100, 100, 100]))

    def draw_circle(self, x, y):
        pygame.draw.circle(self.screen, self.GREEN, (x*100+10, y*100+10), 20)

    def quit(self):
        pygame.quit()


for i in range(len(mepa)):
    for j in range(len(mepa[i])):
        if mepa[i][j] == 1:
            mepa[i][j] = list(np.random.uniform(0, 1, 3))


# player position
posx, posy = (1, 1)
exitx, exity = (3, 3)

# player rotation pi/4 = 45%
rot = np.pi / 4

minimap = Minimap(mepa, posx, posy, exitx, exity)


while True:
    plt.hlines(-0.6, 0, 60, colors="gray", lw=165, alpha=0.5)
    plt.hlines(0.6, 0, 60, colors="lightblue", lw=165, alpha=0.5)
    tilex, tiley, tilec = ([], [], [])

    for i in range(60):
        # rot - 30 ~ rot + 30
        rot_i = rot + np.deg2rad(i - 30)
        x, y = (posx, posy)
        sin, cos = (0.02*np.sin(rot_i), 0.02*np.cos(rot_i))
        n = 0

        while True:
            xx, yy = (x, y)
            x, y = (x + cos, y + sin)
            n = n + 1
            if abs(int(3*xx) - int(3*x)) > 0 or abs(int(3*yy)-int(3*y)) > 0:
                tilex.append(i)
                tiley.append(-1/(0.02*n))
                if int(x) == exitx and int(y) == exity:
                    tilec.append("b")
                else:
                    tilec.append("k")
            if mepa[int(x)][int(y)] != 0:
                h = np.clip(1/(0.02 * n), 0, 1)
                c = np.asarray(mepa[int(x)][int(y)])*(0.3 + 0.7 * h**2)
                break

        plt.vlines(i, -h, h, lw=8, colors=c)

    plt.scatter(tilex, tiley, c=tilec)

    plt.axis("off")
    plt.tight_layout()
    plt.axis([0, 60, -1.2, 1.2])
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

    key = keyboard.read_key()
    x, y = (posx, posy)

    if key == "up":
        x, y = (x+0.3*np.cos(rot), y+0.3*np.sin(rot))
    elif key == "down":
        x, y = (x-0.3*np.cos(rot), y-0.3*np.sin(rot))
    elif key == "left":
        rot = rot - np.pi/8
    elif key == "right":
        rot = rot + np.pi/8
    elif key == "esc":
        break

    minimap.draw_map(posx, posy)

    if mepa[int(x)][int(y)] == 0:
        if int(posx) == exitx and int(posy) == exity:
            minimap.quit()
            break
        posx, posy = (x, y)

plt.close()
