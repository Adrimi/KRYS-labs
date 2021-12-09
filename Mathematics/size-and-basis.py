from math import sqrt
from functools import reduce


def main():
  v = [4, 6, 2, 5]

  size = sqrt(reduce(lambda a, b: a + b**2, v, 0))

  print(f'Solution is {size}')


if __name__ == '__main__':
  main()
