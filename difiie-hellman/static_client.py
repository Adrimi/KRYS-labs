from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from commons import *


def main():
  # Bob wysyła nam swój publiczny klucz B (g^b mod p), a shared_secret wylicza po wysłaniu mu przez Alice wartości A jako A^b mod p
  # Jeżeli po tym jak Bob się do nas połączy wyślemy mu A (otrzymane od Alice) pod przykrywką g, to chłop nam wyliczy z marszu A^b mod p, czyli da nam na tacy sekret

  # W payloadzie wysłanym do Boba wysłałem to samo p, g z wartością A, A z wartością g (dlatego że terminal krzyczał że za dużo znaków xd)

  # iv i flaga od Alice, bo na tych od Boba się sypało
  msg = {
      "iv":
          "2270f5a7cf91a9a4a0f8c4702280641f",
      "encrypted":
          "5426415151d0125cd89c9cf3f8bd842493d6cce28222b478b9d3dd3716a5d632"
  }
  shared_secret = "0x3237a9955c7abfa0b4bcc476b7bf2ad513a9146e2a5d14abfc12551411e682c1da4d6bcb5d96cefe9ef1a080710d66369349f30491b70206627acfdcfd1baa2506f9717f3f629691b581cc74bd537cdb9a3b16f31bfa5cd3c74e44ceaf5484fc47c2a3f51885820026b9334390cb46c69bfff8fae036e6e73803164518dada7a15ffcd18fc54099598c4cd385deaf068b611413ed4436f4234d9d0e933ea5209a16247bf4e3b291204a56e4d1c88f56268035e9386eb6dc2436c562e5afb6259"

  iv = msg['iv']
  ciphertext = msg['encrypted']

  flag = decrypt_flag(int(shared_secret, 16), iv, ciphertext)
  print(flag)
  # crypto{n07_3ph3m3r4l_3n0u6h}


if __name__ == '__main__':
  main()
