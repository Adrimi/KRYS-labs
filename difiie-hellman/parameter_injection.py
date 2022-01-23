from commons import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long


def main():
  # from Alice:
  p = '0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff'
  g = '0x02'
  A = '0xe9e14772c509d77b3ae4afd69d6d6946ab1cf3bb5ddf1a125a87534d224b9064278c14e0690af6700a0d09c622ea5009bd1c469232e24d88a51627e5f416076793ef0526a74961f4a0ac05905374bd3437c205964b4bb0601f7e6b380e74060742efc39130e9cd10410706adb8064de7b426ef1075cae3f3c2a313eebe3a80029b754760021140c6349e72d8a609f9ea01598aa3616763e82fbec550ad58027d0649ab89a349042d9f5e759c39e6aa35007caffe7ad625feb62250e6e8eadde6'

  p = int(p, 16)
  g = int(g, 16)
  A = int(A, 16)

  # random value
  b = 3452348950283495
  B = pow(g, b, p)
  shared_key = pow(A, B, p)

  # repaste Alice reponse straight to BOB, does not matter what he says
  # send to Alice my parameter, not bobs
  print(hex(shared_key))

  alice_response = {
      "iv":
          "202b77bc911a75b547a9662b6c504af1",
      "encrypted_flag":
          "4d50ad053bafb99c112184df1fafe78041ffbc82b257d70f7b40f7ec30b37fc8"
  }

  print(shared_key)
  print(alice_response['iv'])
  print(alice_response['encrypted_flag'])
  result = decrypt_flag(shared_key, alice_response['iv'],
                        alice_response['encrypted_flag'])
  print(f'Solution is {result}')


if __name__ == '__main__':
  main()