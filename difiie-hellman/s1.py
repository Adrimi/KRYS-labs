from Crypto.Util.number import inverse


def main():
  p = 991
  g = 209
  d = inverse(g, p)
  print(f'Solution is {d}')


if __name__ == '__main__':
  main()