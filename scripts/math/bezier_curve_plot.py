import matplotlib.pyplot as plt
import numpy as np


# Plot a bezier curve
def plot_bezier_curve(teather1, teather2, hook1, hook2, n_points=500):

    points = [teather1, hook1, hook2, teather2]
    t = np.linspace(0, 1, n_points)
    x = points[0][0] * (1 - t)**3 + points[1][0] * 3 * t * (1 - t)**2 + points[2][0] * 3 * t**2 * (1 - t) + points[3][0] * t**3
    y = points[0][1] * (1 - t)**3 + points[1][1] * 3 * t * (1 - t)**2 + points[2][1] * 3 * t**2 * (1 - t) + points[3][1] * t**3

    plt.scatter(points[0][0], points[0][1], c='g', marker='o')
    plt.scatter(points[1][0], points[1][1], c='r', marker='o')
    plt.scatter(points[2][0], points[2][1], c='r', marker='o')
    plt.scatter(points[3][0], points[3][1], c='b', marker='o')
    plt.plot(x, y)
#END

plot_bezier_curve((0, 0), (0, 10), (10, 0), (3, 2))
plt.show()
