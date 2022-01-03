from commons import *


def main():
  N = 882564595536224140639625987659416029426239230804614613279163
  c = 77578995801157823671636298847186723593814843845525223303932
  d = 121832886702415731577073962957377780195510499965398469843281

  result = decrypt(c, d, N)

  print(f'Solution is {result}')


def decrypt(ciphertext, d, N):
  return pow(ciphertext, d, N)


if __name__ == '__main__':
  main()