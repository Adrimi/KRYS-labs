#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
from sage.all import factor
from commons import *


def main():
  n = 742449129124467073921545687640895127535705902454369756401331
  e = 3
  ct = 39207274348578481322317340648475596807303160111338236677373

  # n will be 8 * (100 + 100) = 1600 bits strong which is pretty good
  while True:
    p = getPrime(100)
    q = getPrime(100)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    if d != -1 and GCD(e, phi) == 1:
      break

  n = p * q

  flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
  pt = bytes_to_long(flag)
  ct = pow(pt, e, n)

  print(f"n = {n}")
  print(f"e = {e}")
  print(f"ct = {ct}")

  n = 742449129124467073921545687640895127535705902454369756401331
  e = 3
  ct = 39207274348578481322317340648475596807303160111338236677373

  pq_factorio = factor(n)
  factorized = [int(t[0]) for t in pq_factorio]
  print(factorized)
  p = factorized[0]
  q = factorized[1]
  phi = (p - 1) * (q - 1)
  d = inverse(e, phi)

  pt = pow(ct, d, n)
  decrypted = long_to_bytes(pt)
  print(f'Decrypted is {decrypted}')


if __name__ == '__main__':
  main()
