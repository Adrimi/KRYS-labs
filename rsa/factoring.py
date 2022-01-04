from sage.all import factor


def main():
  number = 510143758735509025530880200653196460532653147

  factorize = factor(number)

  print(f'Solution is {factorize}')


if __name__ == '__main__':
  main()