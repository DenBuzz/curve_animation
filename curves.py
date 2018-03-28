import math
import time

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


# y = [sigmoid(n) for n in x]
# plt.plot(x, y)
# plt.show()


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def animate_lines(x, f, g, frames, interval):

    sig_points = np.linspace(-5, 5, frames)

    def update_lines(i):
        if i == 0:
            time.sleep(1)
        y_mid = f(x) + (g(x) - f(x)) * sigmoid(sig_points[i])
        line.set_data(x, y_mid)
        return line,

    fig = plt.figure(figsize=(8, 6))
    ax = plt.subplot(111)
    ax.grid()
    plt.plot(x, f(x), '--')
    plt.plot(x, g(x), '--')
    line, = plt.plot(x, f(x))
    plt.xlim(x[0], x[-1])
    plt.ylim(-1.2, 1.2)
    line_ani = animation.FuncAnimation(fig, update_lines, frames, interval=interval, blit=True)

    plt.show()


x = np.arange(-4 * np.pi, 4 * np.pi, 0.1)


def f(x): return np.sin(x)**2


def g(x): return np.cos(x)


animate_lines(x, f, g, 1000, 3)
