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
  decrypted_message = bytes_to_long(flag)
  ct = pow(decrypted_message, e, n)

  print(f"n = {n}")
  print(f"e = {e}")
  print(f"ct = {ct}")

  n = 742449129124467073921545687640895127535705902454369756401331
  e = 3
  ct = 39207274348578481322317340648475596807303160111338236677373

  # 1600 bits but thats over multiplication, really p and q has only 100 bits long
  # taht allows sage tool to factor them easily from the N
  pq_factorio = factor(n)

  # take first pair of p and q
  factorized = [int(t[0]) for t in pq_factorio]

  # print them to check if thats correct
  print(factorized)
  p = factorized[0]
  q = factorized[1]
  phi = (p - 1) * (q - 1)

  # calculate decryption key
  d = inverse(e, phi)

  # decrypt
  decrypted_message = decrypt(ct, d, n)
  readable_message = long_to_bytes(decrypted_message)
  print(f'Solution is {readable_message}')


if __name__ == '__main__':
  main()
