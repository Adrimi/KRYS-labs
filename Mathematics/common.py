from functools import reduce
from math import sqrt
from typing import List


def multiply(list):
    return reduce(lambda a, b: a * b, list)


def vector_size(v) -> float:
    return sqrt(vector_magnitude(v))


def vector_magnitude(v) -> float:
    return reduce(lambda a, b: a + b ** 2, v, 0)


def vector_dot(u, v) -> float:
    return reduce(lambda a, b: a + b, map(lambda x, y: x * y, u, v), 0)


def vector_substract(u, v) -> List[float]:
    return list(map(lambda x, y: x - y, u, v))


def vector_sum(u) -> List[float]:
    return list(reduce(lambda a, b: map(lambda x, y: x + y, a, b), u))


# def vector_normalize(u) -> List[float]:
#     mag = vector_size(u)
#     return list(map(lambda x: x / mag, u))


def vector_projection(u, v) -> List[float]:
    a = vector_dot(u, v) / vector_magnitude(u)
    return list(map(lambda x: x * a, u))
