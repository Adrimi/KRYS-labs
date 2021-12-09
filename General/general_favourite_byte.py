from pwn import xor

input = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

for index, byte in enumerate(range(0, 127)):
  output = xor(bytes.fromhex(input), byte)

  # print(index, output)

  krypto = ""
  for i in output:
    krypto = krypto + "".join(chr(i))

  if krypto.startswith('crypto'):
    print(krypto)