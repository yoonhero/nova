import numpy as np
from matplotlib import pyplot as plt
import keyboard

mepa = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]]


# player position
posx, posy = (1, 1)
exitx, exity = (3, 3)

# player rotation pi/4 = 45%
rot = np.pi / 4


for i in range(60):
    # rot - 30 ~ rot + 30
    rot_i = rot + np.deg2rad(i - 30)
    x, y = (posx, posy)
    sin, cos = (0.02*np.sin(rot_i), 0.02*np.cos(rot_i))
    n = 0

    while True:
        x, y = (x + cos, y + sin)
        n = n + 1
        if mepa[int(x)][int(y)] != 0:
            h = 1 / (0.2 * n)
            break

    plt.vlines(i, -h, h)

plt.show()
