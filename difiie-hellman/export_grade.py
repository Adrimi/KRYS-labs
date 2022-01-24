from sympy.ntheory import discrete_log
from commons import *


def main():
  # nc socket.cryptohack.org 13379
  # {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
  # {"supported": ["DH64"]}
  # {"chosen": "DH64"}
  # Diffie Hellman 64 to najprostszy klucz, więc i najłatwiejsze złamanie
  # przy 64 bitowym p da się policzyć dyskretny logarytm w przeciągu kilku sekund

  #  From Alice
  p = 0xde26ab651b92a129
  g = 0x2
  A = 0xb2a04dfa827e6d0f
  # From Bob
  B = 0x6d0f055b5b9f0ddf

  # brakuje tylko a: g^a = A (mod p)
  # ale DH64 jest słaby i mozna wyliczyc to od razu! przekształcając na logarytm
  # ale2 tutaj jest modulo, wiec trzeba uzyc:
  # discrete_log(n, a, b): Compute the discrete logarithm of a to the base b modulo n.
  # wyznaczamy sobie a, dzięki czemu z wiadomości B od Boba uzyskamy sobie shared_secret
  a = discrete_log(p, A, g)
  shared_key = pow(B, a, p)

  shared_secret = shared_key
  iv = "3c46b989236f3c1e307cb6ace9a42c67"
  ciphertext = "4a6a3e3e8eb40f7fda89ed55853145d042c2e71ffb853f31ec0e8b013d2cfa92"

  result = decrypt_flag(shared_secret, iv, ciphertext)
  print(f'Solution is {result}')


if __name__ == '__main__':
  main()
