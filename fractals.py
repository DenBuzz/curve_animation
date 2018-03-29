import math
import time

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def mag(vector):
    return ((vector)[0]**2 + (vector)[1]**2)**(1 / 2)


def unit_in_dir(angle):
    x = np.cos(angle)
    y = np.sin(angle)
    return np.array((x, y))


class Fractal():
    def __init__(self):
        self.x = []
        self.y = []
        self.points = []

    def set_points(self, points):
        self.points = points
        self.x = []
        self.y = []
        for p in points:
            self.x.append(p[0])
            self.y.append(p[1])

    def iterate(self, iter=1):
        for i in range(iter):
            new_data = []
            for i in range(len(self.points) - 1):
                new_data.extend(self.fract(self.points[i], self.points[i + 1]))
            self.set_points(new_data)

    def draw(self):
        fig = plt.figure(figsize=(15, 8))
        plt.plot(self.x, self.y)
        plt.axis('equal')
        plt.show()

    def fract(self, p1, p2):
        a, b = np.array(p1), np.array(p2)
        v1 = a + (b - a) / 3
        v3 = a + 2 * (b - a) / 3
        unit = (b - a) / mag(b - a)
        angle = np.arctan2(unit[1], unit[0])
        new_unit = unit_in_dir(angle + 0.5235987)
        hyp = mag(b - a) / (2 * np.cos(0.5235987))
        v2 = a + new_unit * hyp

        return a, v1, v2, v3, b


frac = Fractal()
frac.set_points([np.array((-1, 0)), np.array((0, 3**(1 / 2))), np.array((1, 0)), np.array((-1, 0))])
frac.draw()
for i in range(4):
    frac.iterate(1)
    frac.draw()
    time.sleep(2)
