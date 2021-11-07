from pwn import xor
from Crypto.Util.number import long_to_bytes

input = "label"

output = xor(input.encode('utf-8'), 13)

print(output)