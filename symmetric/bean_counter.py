from commons import byte_xor
import requests


def main():

  # every PNG image begins with the following 16 plaintext bytes.
  png_header = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
  cipher_image = bytes.fromhex(get_encoded_string())

  cipher_blocks = [
      cipher_image[i:i + 16] for i in range(0, len(cipher_image), 16)
  ]
  key_stream_block = byte_xor(cipher_blocks[0], png_header)

  # The counter in the challenge does not function properly.
  # in with open block: `block = f.read(16)`
  # in while block: `block = f.read(16)`
  # So we can decrypt by just XORing every block with the same keystream_block
  with open("flag.png", "wb") as f:
    for block in cipher_blocks:
      plaintext_block = byte_xor(key_stream_block, block)
      f.write(plaintext_block)

  # Then just open the file to see the flag: crypto{hex_bytes_beans}


def get_encoded_string():
  return requests.get(
      'https://aes.cryptohack.org/bean_counter/encrypt/').json()['encrypted']


if __name__ == '__main__':
  main()
