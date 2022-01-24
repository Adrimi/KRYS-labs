from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from commons import *


def main():

  # Intercepted from Alice: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x280a9805110074f9aafe0b9c9e23d7d90f0b494a457ad2db0810f1724690a913f3204249ffe42ef1db414601fc521b5f848de01522b933df035a7c33d52355a493141ddce2d54eeaa764815ed038fc3c29922fa9a5b5a577c2e5539f5461a75c65907ab3ee588a7fda0f701710102953be6575bf6cfe49c6c83094d6628f16f75a406cc2b907814a3baa0469cd8319d1257c3b606ea7ad9f020ca38bad81e18e1ac812ba0f75238f95746e62cb64fe387cbb208cdce6acf372eb9050d4be6401"}
  # Intercepted from Bob: {"B": "0x8d79b69390f639501d81bdce911ec9defb0e93d421c02958c8c8dd4e245e61ae861ef9d32aa85dfec628d4046c403199297d6e17f0c9555137b5e8555eb941e8dcfd2fe5e68eecffeb66c6b0de91eb8cf2fd0c0f3f47e0c89779276fa7138e138793020c6b8f834be20a16237900c108f23f872a5f693ca3f93c3fd5a853dfd69518eb4bab9ac2a004d3a11fb21307149e8f2e1d8e1d7c85d604aa0bee335eade60f191f74ee165cd4baa067b96385aa89cbc7722e7426522381fc94ebfa8ef0"}
  # Intercepted from Alice: {"iv": "fa183f50bfb3cb5843d6f2435196da5b", "encrypted": "68b5170981d82c9dc0089c47efbf0b2fbb9d2266b5c531d50d33690ee64a1258"}

  # Alice wysyla p, g i A do Boba, Bob bierze g i p i wylicza swoje publiczne B = g^b (mod p)
  # jesli zamienimy g i A w wiadomości Alice, to Bob zamiast liczyc
  # B = g ^ b (mod p) policzy:
  # B = A ^ b (mod p) czyli nasz shared secret :)

  msg = {
      "iv":
          "fa183f50bfb3cb5843d6f2435196da5b",
      "encrypted":
          "68b5170981d82c9dc0089c47efbf0b2fbb9d2266b5c531d50d33690ee64a1258"
  }
  shared_secret = 0x6312213ad666aed2956953f8c4908b0810d8d521e349abccf399943c636a530f27865ded6798605cde24ef8d0f887ce4ba3ee3abba863f36be8f3a0b266c646f4c015aa3f71651a1474730ebecd376729e739d03c70ab04be80fcbd555f3c1f47d57db37f32427fba3a42fe4cd281e7f0ec241c03e31d34ab480bdbdea8b4f6ee589f9e07e75c59948605a330b0b8a50580b6f32b8f626dc6c019350eeba42a7c8637195158d3d7a25520eb1c3344cbbae94b0a30913611ff2e0660136d2346a

  iv = msg['iv']
  ciphertext = msg['encrypted']

  flag = decrypt_flag(shared_secret, iv, ciphertext)
  print(flag)
  # crypto{n07_3ph3m3r4l_3n0u6h}


if __name__ == '__main__':
  main()
