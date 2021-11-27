from functools import reduce
from math import sqrt


def multiply(list):
    return reduce(lambda a, b: a * b, list)


def vector_size(v) -> float:
    return sqrt(vector_magnitude(v))


def vector_magnitude(v) -> float:
    return reduce(lambda a, b: a + b ** 2, v, 0)


def vector_dot(u, v) -> float:
    return reduce(lambda a, b: a + b, map(lambda x, y: x * y, u, v), 0)


def vector_substract(u, v):
    return list(map(lambda x, y: x - y, u, v))


def vector_normalize(u):
    mag = vector_size(u)
    return list(map(lambda x: x / mag, u))


def vector_projection(u, v):
    a = vector_dot(u, v) / vector_magnitude(u)
    return list(map(lambda x: x * a, u))
