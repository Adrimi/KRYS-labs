# The same as in ECB CBC WTF :)
# But C2 and C3 is redundant, C1 is a Input Vector


def main():
  cookie = '4f6f1ce3bcaa76171ed334a01235c7ab3615af06b599849db52a11c2f61cfe2c2db96d54215c569546be4ca4f2b59aa0'
  iv = cookie[:32]
  c2_block = b'admin=False;....'
  c3_block = b'admin=True;.....'

  admin_cookie = byte_xor(bytes.fromhex(iv), c2_block)
  admin_cookie = byte_xor(admin_cookie, c3_block)

  print(f'Cookie is: {cookie[32:]}')
  print(f'Input Vector is: {bytes.hex(admin_cookie)}')


def byte_xor(ba1, ba2):
  return bytes([a ^ b for a, b in zip(ba1, ba2)])


if __name__ == '__main__':
  main()