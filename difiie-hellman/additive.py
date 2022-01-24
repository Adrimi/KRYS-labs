from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse
from commons import *


def main():

  # nc socket.cryptohack.org 13380

  p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
  g = 0x02
  A = 0x9b86c17e8248d424e6c9f6372a8cb381821b4b18f8390dd0d5f3b637d2e24800831f9194932c8972005fb1901887701825df6e50b18dad402fc5c1d70a481bf59ead7461be0e2ecb03429835dd4b4260f3788add9c02559a05468f48d109655b7368422bebef77691d6ddb3b165524dbea835d8b244e012c8b019744a1c45cdb60934412578d8a1bbf9c47a4b1f1d91384cfcfe66084c6910b29fe762b357a20ffddb2058d727b6453e2850a8ae5a4f45d3dfa56132288320411354fbd570719
  B = 0xffe424cde8566d117db756025f7822f3969639029fa16baa8a572764325e5ee0f1823fb2c8114ec014db80aca5942611b7d3803044dab8123c412745da8aeb30ebfb7ae34aec1373ecc2dac033fa4e7342490d4d687647c842ff51b0c851465a079609b971af9ebf5a75549fe6056e9b7675d6eb3f2abe280934f53cbbbdac74f5f2aa6dfe041310adc1dcdceb5de3dad669a799951df788d1ac0bb7144d020f0165e20b6f59520b9ae83f1fb6b0ef9bfd224ab0ac342a6f4fe716637df33a8f
  iv = "28b7d215ad0b2b24b7ffab7a466d4761"
  encrypted = "e32d81d3dab4ca4a4490be8e40a7c4c7d1316479fbf9ac55624267e24fd469f5562855dd3e9a359de5c024839efef6fc"

  # gdy grupa jest addytywna a nie multiplikatywna,
  # to przed modulo nie mamy potęgi (g^a), tylko mnożenie:
  # A = g * a (mod p)
  # czyli mozna policzyc sekret a:
  # a = A * 1/g (mod p) - to jest latwe do policzenia
  a = (A * inverse(g, p)) % p

  # i w takim sekret to nie B ^ a tylko znowu mnozenie:
  shared_secret = (B * a) % p

  flag = decrypt_flag(shared_secret, iv, encrypted)
  print(f'Solutions is {flag}')


if __name__ == '__main__':
  main()
