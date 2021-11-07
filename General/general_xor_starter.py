from pwn import xor

input = "label"

output = xor(input.encode('utf-8'), 13)

print(output)