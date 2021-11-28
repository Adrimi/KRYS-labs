from math import floor
from common import *


def main():
    v = (846835985, 9834798552)
    u = (87502093, 123094980)

    product = gaussian(u, v)
    result = vector_dot(product[0], product[1])

    print(f'Solution is {result}')


def gaussian(v1, v2):
    while True:
        # a
        if vector_size(v2) < vector_size(v1):
            temp = v1
            v1 = v2
            v2 = temp

        # b
        m = floor(vector_dot(v1, v2) // vector_dot(v1, v1))

        # c
        if m == 0:
            return v1, v2

        # d
        v2 = vector_substract(v2, map(lambda x: m * x, v1))


if __name__ == '__main__':
    main()
