from commons import *
import requests
import string
import binascii, json


def main():
  flag = ''
  input = 'A' * 32  #Let's assume flag length is between 16-32
  iteration = 0
  allowed_characters = string.ascii_letters + string.digits + '}{_'

  while iteration < len(input):
    for i in allowed_characters:
      current_block = encrypt(hex(input[:-1]))[:64]
      next_block = encrypt(hex(input[:-1] + flag + i))[:64]

      # If blocks equals that means a character is a part of the flag
      print(
          f'\rFLAG: {flag} | Current block {current_block} | Next block length {next_block}',
          flush=True,
          end='')
      if next_block == current_block:
        flag += i
        break

    iteration += 1

    input = input[:-1]


# adding '/' avoids redirections (thanks Proxyman)
def encrypt(text):
  return requests.get('http://aes.cryptohack.org/ecb_oracle/encrypt/' + text +
                      '/').json()['ciphertext']


def hex(p):
  return (binascii.hexlify(p.encode())).decode()


if __name__ == '__main__':
  main()
"""
Logic is to take a reference block and compare with a block iterating ascii
Assume flag is      : crypto{wow}
Elignment is        : crypto{w ow}xxxxx (x is padding)
Send 'A'*15 now
the elignment is    : AAAAAAAA AAAAAAAc rypto{wo w}xxxxxx
                      -----------------
                       reference block
Send 'A'*15+'a-z'
now the elignment
is                  : AAAAAAAA AAAAAAAAa crypto{w ow}xxxxx
                      ------------------
                       identifier block
if reference block matches identifier block then we got the first letter. So this way we can obtain total flag ;)
"""