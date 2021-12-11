from functools import reduce


# Converts a 4x4 matrix into a 16-byte array.
def matrix2bytes(matrix):
  return reduce(list.__add__, matrix)


# Convert a list of ASCII Integers to a string
def asciiListToString(list):
  return reduce(lambda a, b: a + chr(b), list, "")
