def main():
  p = 28151
  # g**n % p
  # find the smallest g that cause to have H = {g, g**2, ...}

  omega = range(1, p)
  for g in omega:
    H = set([pow(g, n, p) for n in range(p)])
    if set(omega).issubset(H):
      print(f'Solution is {g}')
      break


if __name__ == '__main__':
  main()