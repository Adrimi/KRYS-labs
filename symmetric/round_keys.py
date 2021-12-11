import numpy as np
from commons import *


def main():

  state = [
      [206, 243, 61, 34],
      [171, 11, 93, 31],
      [16, 200, 91, 108],
      [150, 3, 194, 51],
  ]

  round_key = [
      [173, 129, 68, 82],
      [223, 100, 38, 109],
      [32, 189, 53, 8],
      [253, 48, 187, 78],
  ]

  print(asciiListToString(matrix2bytes(add_round_key(state, round_key))))


# XOR the current state `s` with the current round key `k`
def add_round_key(s, k):
  return list(map(bitwiseXOR, s, k))


def bitwiseXOR(a, b):
  return (np.array(a) ^ np.array(b)).tolist()


if __name__ == '__main__':
  main()