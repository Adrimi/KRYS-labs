from commons import *


def main():
  state = [
      [108, 106, 71, 86],
      [96, 62, 38, 72],
      [42, 184, 92, 209],
      [94, 79, 8, 54],
  ]

  a = inv_mix_columns(state)
  b = inv_shift_rows(a)
  c = asciiListToString(matrix2bytes(b))

  print(c)


def inv_shift_rows(s):
  s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
  s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
  s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]
  return s


def shift_rows(s):
  s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
  s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
  s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]
  return s


def xtime(a):
  return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
  # see Sec 4.1.2 in The Design of Rijndael
  t = a[0] ^ a[1] ^ a[2] ^ a[3]
  u = a[0]
  a[0] ^= t ^ xtime(a[0] ^ a[1])
  a[1] ^= t ^ xtime(a[1] ^ a[2])
  a[2] ^= t ^ xtime(a[2] ^ a[3])
  a[3] ^= t ^ xtime(a[3] ^ u)

  return a


def mix_columns(s):
  return [mix_single_column(s[i]) for i in range(4)]


def inv_mix_columns(s):
  # see Sec 4.1.3 in The Design of Rijndael
  for i in range(4):
    u = xtime(xtime(s[i][0] ^ s[i][2]))
    v = xtime(xtime(s[i][1] ^ s[i][3]))
    s[i][0] ^= u
    s[i][1] ^= v
    s[i][2] ^= u
    s[i][3] ^= v

  return mix_columns(s)


if __name__ == '__main__':
  main()