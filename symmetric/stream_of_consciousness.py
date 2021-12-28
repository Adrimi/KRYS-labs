import requests
from itertools import combinations  # https://stackoverflow.com/a/36429743/10044077
from commons import byte_xor

# D(P1) ^ K = C1
# D(P2) ^ K = C2

# E(P1) ^ d2 = c1 ^ c2


def main():
  # combinations without repetitions
  tuples = combinations(sorted(TEXT, key=lambda x: len(x)), 2)

  # Since they are using the same KEY to encrypt I can XOR them
  # To try to get some message...
  xor_tuples = []
  for tuple in tuples:
    x, y = tuple[0], tuple[1]
    shorter_lenght = min(len(x), len(y))
    xor_tuples.append(
        byte_xor(bytes.fromhex(x[:shorter_lenght]),
                 bytes.fromhex(y[:shorter_lenght])))

  known_part = b'crypto{'

  # And then XOR the Ci ^ Ci+1 with a known part, the 'crypo{'
  xor_keyed = []
  for xor in xor_tuples:
    max_length = min(len(xor), len(known_part))
    xor_keyed.append(byte_xor(xor[:max_length], known_part[:max_length]))

  # There are some results among
  # [print(x) for x in xor_keyed]
  """
    b'What a '
    b"It can'"
    b'I shall'
    b'Three b'
    b"No, I'l"
    b'As if I'
    b'How pro'
    b'Why do '
    b'I shall'
    b'The ter'
    b'Would I'
    b'Perhaps'
    b"I'm unh"
    b'Love, p'
    b'Dolly w'
    b'These h'
    b'What a '
  """

  known_part = b"No, I'll"

  # And then XOR the Ci ^ Ci+1 with a known part, the 'No, I'll' -> guessing the letter 'l'
  xor_keyed = []
  for xor in xor_tuples:
    max_length = min(len(xor), len(known_part))
    xor_keyed.append(byte_xor(xor[:max_length], known_part[:max_length]))

  # There are some results among
  [print(x) for x in xor_keyed]
  """
    b'As if I '
    b'How prou'
    b'Why do t'
    b'I shall,'
    b'The terr'
    b'Would I '
    b'Perhaps '
    b"I'm unha"
    b'Love, pr'
    b'Dolly wi'
    b'These ho'
    b'What a l'
  """

  known_part = b"How proud"

  # And then XOR the Ci ^ Ci+1 with a known part, the 'No, I'll' -> guessing the letter 'l'
  xor_keyed = []
  for xor in xor_tuples:
    max_length = min(len(xor), len(known_part))
    xor_keyed.append(byte_xor(xor[:max_length], known_part[:max_length]))

  # There are some results among
  [print(x) for x in xor_keyed]
  """
  b'And I sha'
  b'What a na'
  b'How prowj'
  b"It can't "
  b'As if I h'
  b'Why do th'
  b'I shall, '
  b'The terri'
  b'Would I h'
  b'Perhaps h'
  b"I'm unhap"
  b'Love, pro'
  b'Dolly wil'
  b'These hor'
  """

  known_part = b"And I shall"

  # And then XOR the Ci ^ Ci+1 with a known part, the 'No, I'll' -> guessing the letter 'l'
  xor_keyed = []
  for xor in xor_tuples:
    max_length = min(len(xor), len(known_part))
    xor_keyed.append(byte_xor(xor[:max_length], known_part[:max_length]))

  # There are some results among
  [print(x) for x in xor_keyed]
  """
    b'Dress-makin'
    b'crypto{k3y5'
    b'What a nast'
    b"It can't be"
    b'I shall los'
    b'Three boys '
    b"No, I'll go"
    b'As if I had'
    b'How proud a'
    b'Why do they'
    b"I shall, I'"
    b'The terribl'
    b'Would I hav'
    b'Perhaps he '
    b"I'm unhappy"
    b'Love, proba'
    b'Dolly will '
    b'These horse'
  """

  while True:
    xor_keyed = []
    for xor in xor_tuples:
      max_length = min(len(xor), len(known_part))
      xor_keyed.append(byte_xor(xor[:max_length], known_part[:max_length]))

    # There are some results among us...
    [print(x) for x in xor_keyed]

    known_part = input("Put your guess :)\n").encode()

    # How proud and happy
    # What a nasty smell t
    # I shall, I'll lose everything
    # Love, probably? They don't know
    # crypto{k3y57r34m_r3u53_15_f474l}
    # FOUND !!


# At first I try to fetch all of the words
def get_texts():
  texts = []

  k = 0
  iterations = 30  # almost always returns 22 entities, so it is enough
  while k < iterations:
    encrypted_text = encrypt()
    if texts.count(encrypted_text) == 0:
      texts.append(encrypted_text)

    k += 1
    print("\r" + str(k), flush=True, end='')

  print(f'\nLength of the texts file is {len(texts)}')
  print(f'\n\n{texts}')

  return texts


def encrypt():
  return requests.get('http://aes.cryptohack.org/stream_consciousness/encrypt/'
                     ).json()['ciphertext']


# ALL OF THE TEXTS
TEXT = [
    '6c64222ec5603bfdb0bb5d705e7d57464796346169db04d502ff136000475917696e4f0af8996fc2a85162f005',
    '692b2723882c27afb3b64f7712611e036187257020d10c9b44e5572b00475a1766644c0af4826783b84921f25f8382af1ee4935c10a544da5962ba0304a65a1677125851c9933a8fa28bcf02b5d8bb390bd8bff56e0e8b5f5cfa8d5520',
    '6c64222ec5603bf1fc9d097912384d4c468a606c76d0118c17f91e2e090844512e635e0af49f6791a41775bb48cc86b912a69a500cab',
    '722c3032846d77b3bda75a6c5e6b4c465983607d68dc10d513f01e2e1a0845566a25',
    '712c2323c12c35b2a5a70e670b764f4a5b886c2970d9028c0aff10600f5c0d5f6179484fe3dc22b1af4278f451cb8afd',
    '712c3466d06925afb5b642705e6c494a5b8860607395179d02e55734064d0d476f784f0af3916cc5be1063fe0bd784ae5ce4944613a54ed61462a21945a05c17644f58',
    '612b3d2add2c20b4b0b80e6116714f48159b286874952ad20eb11b250f5e4459692b5a0ae395618da45421f35ed089bd5ca0db5209e10cdb5c6aa24a11ba560a755a190d8cc71bcaefbfca13fbdeab6b0fdaa2f56f03c25a56a89c536bed26de7f6e68da',
    '7521232ec57c24fdb4b10e7d1f6b014e5c9c336c6495179d06b103320f4143176f655f0af9832280ab536abb49dacbb25db3d51330e442db1466b91800f25b0d7d551a1688933b85eceb',
    '722c2866c06377a9b4b157351977014c5bcf306869db179c0df65721004c0d557b62574ef99e65c2ab5c6dbb5fcb8efc46ad965658',
    '67312566ed2c20b4b0b80e66167756035d862d27',
    '6d2b2666d47e38a8b8f44f7b1a384942459f392968d044990fb115254e5f4552602b534fb0976796b9106ce20bcd84a857e5',
    '722c3032846d77b1b3a00e7a1838554b5c81277a20c10b9417b103280b460d446b6e564ff4d0768dea5d64bb58cccbb153b68d560be943da472bb70401f246167148021e80893388eeaf9547b3cca87c4ad4beb6620b871351e69b5269a338ca79636e9aa4830791b5da13b3061d285f536c8f940bac013c65de3e58bc8b8ee0a34c8ca53f7141bc933875e1298d19474ff2bb36789e736289ab0bd7f4c1eb',
    '6c307125c56270a9fcb64b350a77534d1580357d2c95018017b11e344e4b4c592e695e0af9976c8db85565b5',
    '6b2b7d66ed2b3bb1fcb34135177601575acf04666cd91ad502ff13601a4d415b2e635e58b0837690ab5966f35f8384a946',
    '6c633c66d1623fbcaca457395e510147509c257b76d0439c17bd5734064d0d516f7e575eb783228fa35e64b70bc19ea8128ddc5e47f042c7557ba61345b35f1430481e1ac9943387e7e6990fbec1ae3907d3f5',
    '6437712fc22c1efdb4b54a351f7658034286336120c10cd501f457290008595f6b2b4943f79876c3ea7921f84acdcca813',
    '712c3435c12c3fb2aea74b665238554b5c9c606a61c7119c02f6126043084558792b720afc9f6396a25521f652d08eb054e4925d47f144c6472bb50b17a05a1977595652c9933a8ffbedcb02fbccb2754adeb2a6364680464ca8a11b7da530c07c206191a6ca55d0a8db56e71a106d461b64869211e266',
    '722b242ac02c1efdb4b558705e7a444f5c8a366c6495179d06ff573406495917472b5845e59c66c2b85560f8438398a951acdb5702f558c7472bb90c45ba461579501f1e9d8e3d84bd',
    '46362836d0632cb6efad1b220c2b154e6a9d737c35863cc456ce1174591c414a',
    '61363435d7213abcb7bd40725e794f4715a229656cdc0d9011e8',
    '642a3566ed2c24b5bdb84235177f4f4c478a6060749b', '6a312379845b3fa4fcbb5b6741'
]

if __name__ == '__main__':
  main()
