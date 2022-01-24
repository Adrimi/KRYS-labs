from Crypto.Util.number import inverse
from sage.all import *
from commons import *


def main():
  P = 2
  N = 50
  E = 31337

  c = load_matrix("./flag.enc", P)
  totient = c.multiplicative_order()

  d = pow(E, -1, totient)
  p = c**d

  p = mat_to_binstr(p, N)
  pt = hex(int(p, 2))[2:70]
  print(bytes.fromhex(pt).decode())


def load_matrix(fname, P):
  data = open(fname, 'r').read().strip()
  rows = [list(map(int, row)) for row in data.splitlines()]
  return Matrix(GF(P), rows)


def mat_to_binstr(mat, N):
  binstr = ""
  for i in range(N):
    for j in range(N):
      binstr += str(mat[j][i])
  return binstr


# z pliku sage

FLAG = b'crypto{??????????????????????????}'
N = 50


def bytes_to_binary(s):
  bin_str = ''.join(format(b, '08b') for b in s)
  bits = [int(c) for c in bin_str]
  return bits


def generate_mat():
  while True:
    msg = bytes_to_binary(FLAG)
    msg += [random.randint(0, 1) for _ in range(N * N - len(msg))]

    # wiersze
    rows = [msg[i::N] for i in range(N)]

    # macierz 50x50 RSA
    mat = Matrix(GF(2), rows)

    if mat.determinant() != 0 and mat.multiplicative_order() > 10 ^ 12:
      return mat


if __name__ == '__main__':
  main()