def main():
  cipernumber = 12
  e = 65537
  p = 17
  q = 23

  N = p * q
  result = pow(cipernumber, e, N)

  print(f'Solution is {result}')


if __name__ == '__main__':
  main()