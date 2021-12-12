import requests


def main():

  # So the same 96 hex string (48 bytes), that is split as usual: initial vector is first 32 bytes
  encoded_string = get_encoded_string()
  iv = encoded_string[:32]
  ciphertext = encoded_string[32:]

  plain_hex = encrypt(iv, ciphertext)
  plaintext = bytes.fromhex(plain_hex)
  print(f'Soultion is {plaintext}')


def encrypt(iv, ciphertext):
  return requests.get(
      f'http://aes.cryptohack.org/symmetry/encrypt/{ciphertext}/{iv}/').json(
      )['ciphertext']


def get_encoded_string():
  return requests.get(
      'http://aes.cryptohack.org/symmetry/encrypt_flag/').json()['ciphertext']


if __name__ == '__main__':
  main()
