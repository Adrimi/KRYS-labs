from diffusion_permutation import inv_shift_rows, inv_mix_columns
from round_keys import add_round_key
from substitution import sub_bytes
from commons import bytes2matrix, matrix2bytes, asciiListToString
import resources as R

N_ROUNDS = 10


def main():
  key = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'
  ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd'

  print(decrypt(key, ciphertext))


def decrypt(key, ciphertext):
  # Remember to start from the last round key asnd work backwards through them when decrypting
  round_keys = expand_key(key, R.s_box())

  # Convert ciphertext to state matrix
  initial_matrix = bytes2matrix(ciphertext)

  # Initial add round key step
  iv = add_round_key(initial_matrix, round_keys[-1])

  for i in range(N_ROUNDS - 1, 0, -1):
    one = inv_shift_rows(iv)
    two = sub_bytes(one, R.inv_s_box())
    three = add_round_key(two, round_keys[i])
    four = inv_mix_columns(three)
    iv = four

  # Run final round (skips the InvMixColumns step)
  one = inv_shift_rows(iv)
  two = sub_bytes(one, R.inv_s_box())
  three = add_round_key(two, round_keys[0])

  # Convert state matrix to plaintext
  plaintext = asciiListToString(matrix2bytes(three))

  return plaintext


def expand_key(master_key, s_box):
  """
    Expands and returns a list of key matrices for the given master_key.
    """

  # Round constants https://en.wikipedia.org/wiki/AES_key_schedule#Round_constants
  r_con = (
      0x00,
      0x01,
      0x02,
      0x04,
      0x08,
      0x10,
      0x20,
      0x40,
      0x80,
      0x1B,
      0x36,
      0x6C,
      0xD8,
      0xAB,
      0x4D,
      0x9A,
      0x2F,
      0x5E,
      0xBC,
      0x63,
      0xC6,
      0x97,
      0x35,
      0x6A,
      0xD4,
      0xB3,
      0x7D,
      0xFA,
      0xEF,
      0xC5,
      0x91,
      0x39,
  )

  # Initialize round keys with raw key material.
  key_columns = bytes2matrix(master_key)
  iteration_size = len(master_key) // 4

  # Each iteration has exactly as many columns as the key material.
  i = 1
  while len(key_columns) < (N_ROUNDS + 1) * 4:
    # Copy previous word.
    word = list(key_columns[-1])

    # Perform schedule_core once every "row".
    if len(key_columns) % iteration_size == 0:
      # Circular shift.
      word.append(word.pop(0))
      # Map to S-BOX.
      word = [s_box[b] for b in word]
      # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
      word[0] ^= r_con[i]
      i += 1
    elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
      # Run word through S-box in the fourth iteration when using a
      # 256-bit key.
      word = [s_box[b] for b in word]

    # XOR with equivalent word from previous iteration.
    word = bytes(i ^ j for i, j in zip(word, key_columns[-iteration_size]))
    key_columns.append(word)

  # convert those stupid-ass bytes to list of bytes in int as it should be written xd
  for index, shit in enumerate(key_columns):
    if not isinstance(shit, list):
      key_columns[index] = list(shit)

  # Group key words in 4x4 byte matrices.
  return [key_columns[4 * i:4 * (i + 1)] for i in range(len(key_columns) // 4)]


if __name__ == '__main__':
  main()