from math import sqrt


def main():
  p = 29
  ints = [14, 6, 11]

  quad_res = quadratic_residues(p)

  print(quad_res)

  for int in ints:
    for square_root, residue in quad_res:
      if int is residue:
        print(f'Answer is {square_root}')


def quadratic_residues(p):
  list = []

  for x in range(1, p - 1):
    residue = x * x % p
    if not residue in [x[1] for x in list]:
      list.append((x, residue))

  return list


if __name__ == '__main__':
  main()
