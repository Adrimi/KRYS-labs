from commons import modular_multiplicative_inverse


def main():
  p = 857504083339712752489993810777
  q = 1029224947942998075080348647219
  e = 65537

  d = modular_multiplicative_inverse(p, q, e)

  print(f'Solution is {d}')


if __name__ == '__main__':
  main()