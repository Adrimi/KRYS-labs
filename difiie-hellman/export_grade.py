from sympy.ntheory import discrete_log
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from commons import *


def main():
  # wymusiłem DH64, żeby mieć jak najprosze p
  # przy 64 bitowym p da się policzyć dyskretny logarytm w przeciągu kilku sekund

  p = 0xde26ab651b92a129
  g = 0x2
  A = 0xb2a04dfa827e6d0f
  B = 0x6d0f055b5b9f0ddf

  # discrete_log(n, a, b): Compute the discrete logarithm of a to the base b modulo n.
  # wyznaczamy sobie a, dzięki czemu z wiadomości B od Boba uzyskamy sobie shared_secret
  a = discrete_log(p, A, g)
  shared_key = pow(B, a, p)

  shared_secret = shared_key
  iv = "3c46b989236f3c1e307cb6ace9a42c67"
  ciphertext = "4a6a3e3e8eb40f7fda89ed55853145d042c2e71ffb853f31ec0e8b013d2cfa92"

  print(shared_secret)
  flag = decrypt_flag(shared_secret, iv, ciphertext)
  print(flag)


if __name__ == '__main__':
  main()
