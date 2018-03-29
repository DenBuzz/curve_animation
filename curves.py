import math
import time

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def animate_functions(x, curves, frames, interval):
    sig_points = np.linspace(-10, 10, frames // (len(curves) - 1))
    y_min = np.min([np.min(f(x)) for f in curves])
    y_max = np.max([np.max(f(x)) for f in curves])
    shift = (y_max - y_min) / 10

    factor = frames // (len(curves) - 1)

    def update_lines(i):
        f = curves[(i - 1) // factor]
        g = curves[1 + (i - 1) // factor]
        y_mid = f(x) + (g(x) - f(x)) * sigmoid(sig_points[(i - 1) % factor])
        line.set_data(x, y_mid)
        return line,

    fig = plt.figure(figsize=(8, 6))
    ax = plt.subplot(111)
    line, = plt.plot([], [])
    for curve in curves:
        plt.plot(x, curve(x), '--', linewidth=0.5)
    plt.xlim(x[0], x[-1])
    plt.ylim(y_min - shift, y_max + shift)
    line_ani = animation.FuncAnimation(fig, update_lines, frames, interval=interval, blit=True)

    plt.show()


x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)


def h(x): return 0 * x
def f(x): return np.sin(x)
def g(x): return np.cos(x)
def m(x): return np.sin(0.5 * x) + np.cos(2 * x)
def t(x): return (1 / 180) * (x**3 - 10 * x)
animate_functions(x, [h, f, m, t, g, h], 1000, 10)
