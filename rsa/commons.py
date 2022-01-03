def toitent_of_N(p, q):
  return (p - 1) * (q - 1)


def modular_multiplicative_inverse(p, q, e):
  return pow(e, -1, toitent_of_N(p, q))