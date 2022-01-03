def main():
  p = 857504083339712752489993810777
  q = 1029224947942998075080348647219

  # N = p * q
  # p and q are pairwise prime numbers
  # https://leimao.github.io/article/RSA-Algorithm/

  toitent_of_N = (p - 1) * (q - 1)

  print(f'Solution is {toitent_of_N}')


if __name__ == '__main__':
  main()