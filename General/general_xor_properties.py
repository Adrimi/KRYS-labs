from pwn import xor

# step 1
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")

# step 2
key2 = xor(
    bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"), key1)

# step 3
key23 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

# step 4
key1_key23 = xor(key1, key23)

flag = xor(
    bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"),
    key1_key23)
print(flag)
