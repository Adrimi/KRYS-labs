from functools import reduce
from math import floor, sqrt
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


def vector_normalize(u) -> List[float]:
    mag = vector_size(u)
    return list(map(lambda x: x / mag, u))


def vector_projection(u, v) -> List[float]:
    a = vector_dot(u, v) / vector_magnitude(u)
    return list(map(lambda x: x * a, u))


# algorithms

def legendre(x, p):
    if (pow(x, (p-1)//2, p)) == 1:
        return 1
    else:
        return 0


def vector_gaussian(v1, v2):
    while True:
        if vector_size(v2) < vector_size(v1):
            temp = v1
            v1 = v2
            v2 = temp

        m = floor(vector_dot(v1, v2) // vector_dot(v1, v1))
        if m == 0:
            return v1, v2

        v2 = vector_substract(v2, map(lambda x: m * x, v1))
