from functools import reduce
from typing import List


def main():
    b = [2, 3, 5]
    n = [5, 11, 17]
    N = mul(n)
    print(f'Solution is in a range 0 <= x < {N}')

    x = solve_x(b, n)

    k = 1
    while k * N < x:
        k += 1

    a = x - (k - 1) * N
    print(f'Solution is {a}')


def solve_x(b, n):
    N = mul(n)
    N_ = [int(N / i) for i in n]

    products: List[int] = []

    # for one case
    for b_i, n_i, N_i in zip(b, n, N_):
        k = N_i % n_i

        x = 1
        while (k * x) % n_i != 1:
            x += 1

        products.append(b_i * N_i * x)

    return sum(products)


def mul(list):
    return reduce(lambda a, b: a * b, list)


if __name__ == '__main__':
    main()
