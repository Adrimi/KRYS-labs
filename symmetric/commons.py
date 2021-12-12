from functools import reduce
import numpy as np


# Converts a 16-byte array into a 4x4 matrix.
def bytes2matrix(text):
  return [list(text[i:i + 4]) for i in range(0, len(text), 4)]


# Converts a 4x4 matrix into a 16-byte array.
def matrix2bytes(matrix):
  return reduce(list.__add__, matrix)


# Convert a list of ASCII Integers to a string
def asciiListToString(list):
  return reduce(lambda a, b: a + chr(b), list, "")


def bitwiseXOR(a, b):
  return (np.array(a) ^ np.array(b)).tolist()


def byte_xor(ba1, ba2):
  return bytes([a ^ b for a, b in zip(ba1, ba2)])