"""
Compression Side Channel Attack:
https://www.venafi.com/blog/what-are-compression-side-channel-attacks

As in the description:
   "The attack takes advantage of an information leak in the compression ratio of TLS requests"
  
Key factor there is to send a message with a sample ASCII letter or digit
 and check if returned encrypted data is shorter (compressed). 
 If so, that must be the correct one. 

"""
import requests
import string


def main():
  solution_part = 'crypto{'
  allowed_characters = string.ascii_letters + string.digits + '_}'

  while True:
    sample_cipher = encrypt((solution_part + ';') * 2)

    for i in allowed_characters:
      cipher = encrypt((solution_part + i) * 2)

      if len(cipher) < len(sample_cipher):
        solution_part += i
        print("\r" + solution_part, flush=True, end='')

        if i == "}":
          print("\n DONE :)")
          exit

        break


def encrypt(plaintext):
  return requests.get('http://aes.cryptohack.org/ctrime/encrypt/' +
                      plaintext.encode('ascii').hex() +
                      '/').json()['ciphertext']


if __name__ == '__main__':
  main()