import numpy as np


def create_ball(img, r):
    img_center = tuple((ni - 1) / 2 for ni in img.shape)
    I, J = np.meshgrid(*[np.arange(ni) for ni in img.shape], indexing="ij")
    R = sum((ind - ci) ** 2 for (ind, ci) in zip([I, J], img_center))
    return np.where(R <= r**2, True, False)


def create_circle(n, r):
    theta = np.linspace(0, 1, n + 1)[:-1]
    points = np.array(
        [[r * np.cos(2 * np.pi * t), r * np.sin(2 * np.pi * t)] for t in theta]
    )
    edges = np.array([[i % n, (i + 1) % n] for i in range(n)])
    return points, edges
