from common import *
from functools import reduce


def main():
  v1 = [4, 1, 3, -1]
  v2 = [2, 1, -3, 4]
  v3 = [1, 0, -2, 7]
  v4 = [6, 2, 9, -5]
  vectors_v = [v1, v2, v3, v4]

  result = gram_schmidt(vectors_v)

  print('Solution is %.5f' % result[-1][1])


def gram_schmidt(input_vectors):
  ouptut_vectors = []

  for v in input_vectors:
    products = []
    for temp in ouptut_vectors:
      products.append(vector_projection(temp, v))

    if len(products) > 0:
      u = vector_substract(v, vector_sum(products))
    else:
      u = v

    ouptut_vectors.append(u)

  return ouptut_vectors


if __name__ == '__main__':
  main()
