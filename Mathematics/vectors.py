from vector import obj

# TASK: Calculate 3*(2*v - w) ∙ 2*u


def main():
  v = obj(x=2, y=6, z=3)
  w = obj(x=1, y=0, z=0)
  u = obj(x=7, y=7, z=2)

  result = (3 * (2 * v - w)) @ (2 * u)

  print(f'Solution is {result}')


if __name__ == '__main__':
  main()
