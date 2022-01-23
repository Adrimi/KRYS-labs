from Crypto.Util.number import inverse
from sage.all import *
from commons import *


def main():
  P = 2
  N = 50
  E = 31337

  c = load_matrix("./flag.enc", P)
  mod = c.multiplicative_order()

  D = pow(E, -1, mod)
  p = c**(D)

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


if __name__ == '__main__':
  main()