from Crypto.Cipher import AES
import hashlib
import random


def main():
  ciphertext = bytes.fromhex(
      'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66')
  partial_flag = b'crypto'
  words = []

  # load words
  with open("symmetric/password_as_keys_words") as f:
    words = [w.strip() for w in f.readlines()]

  # brute force attack
  for w in words:

    # create MD5 hash from the word `w`
    key = hashlib.md5(w.encode()).digest()

    # create new AES cipher from the key
    cipher = AES.new(key, AES.MODE_ECB)

    # try to decrypt the message with the key in this iteration
    decrypted = cipher.decrypt(ciphertext)

    # messsage should have partial flag as alwayss :)
    if partial_flag in decrypted:
      print("plaintext", decrypted)
      exit


if __name__ == '__main__':
  main()
