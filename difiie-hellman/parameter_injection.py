from commons import *


def main():
  # from Alice:
  p = 'ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff'
  g = '02'
  A = '9fce7cdfebf6a9246048cdf3bbb9349fd64713ae61b0f9b0dc857bbcb7b1bd6a68f7d10d0e0ea723e0ad6a3e5a98a92c40f97e013e1603321f7350566d77296f3e330225db5cac503ff4b0e7eab547aeef18296e5e7471f36432732d22e1dcab962bd86f4d2e30de51ec1013acbc42ede880e62ae65d14549f0e6dc6fdfc22db5801a11980609607e6d1651f857c504087b093f178dda1d10b92562f8774026418c062726ca027465afef36553a129c0894912ec1133a144a1589d4e4f2e0d24'

  p = int(p, 16)
  g = int(g, 16)
  A = int(A, 16)

  # random value for my private key
  private_key = 3
  public_key = pow(g, private_key, p)
  shared_key = pow(A, private_key, p)

  # repaste Alice reponse straight to BOB, does not matter what he says
  # send to Alice my parameter, not bobs

  # {"B": "0x8"}
  print(f'Public key {hex(public_key)}')
  # {"B": "0xb136520dbaeee5072d386b5ca4332d421dcacb5092e040960fc05e505e6b7cc839369c60fb6574c32d16a9bdda2fdd6daf75c4b698f610321b0917c9d1825e6de0f011c92049f7cdc2a7f8ec3edef678c528bad6f18912ea0ef94c1d658d283fc06b87ce9c792e4ce7b51e2ea1fa538f810012af35f73eb53a6f79342cf3920cf4359abc2124d5c17e076fb1740947ef8bfdc73dede24be2069168eb3553254e22d9fe7cee95ca98d47281d0173bc35958d8785b71e3588b67ac8a24c8108c49"}
  print(f'Shared key {hex(shared_key)}')

  alice_response = {
      "iv":
          "8f77bcb60579fdced13108964a253be1",
      "encrypted_flag":
          "f7b11f1b90360a4d88274a9f6f82359f47aa548a88f5995011fd168123baf3f9"
  }

  print(shared_key)
  print(alice_response['iv'])
  print(alice_response['encrypted_flag'])
  result = decrypt_flag(shared_key, alice_response['iv'],
                        alice_response['encrypted_flag'])
  print(f'Solution is {result}')


if __name__ == '__main__':
  main()