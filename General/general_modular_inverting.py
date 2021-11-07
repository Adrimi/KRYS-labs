def gcd(a, b):
  while b != 0:
    t = b
    b = a % b
    a = t
  return a

def invert(a, b):
  for i in range(1, b):
    if ((a * i) % b) == 1:
      return i


# what is 3 * d ≡ 1 mod 13

a = 3
b = 13
print(invert(a, b))

