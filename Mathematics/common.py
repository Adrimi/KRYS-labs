from functools import reduce


def mul(list):
    return reduce(lambda a, b: a * b, list)
