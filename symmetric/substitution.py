from commons import *
import resources as R


def main():
  s_box, inv_s_box, state = R.substitution()

  substituted_state = sub_bytes(state, sbox=inv_s_box)
  print(asciiListToString(matrix2bytes(substituted_state)))


def sub_bytes(s, sbox):
  return list(map(lambda x: list(map(lambda x: sbox[x], x)), s))


if __name__ == '__main__':
  main()