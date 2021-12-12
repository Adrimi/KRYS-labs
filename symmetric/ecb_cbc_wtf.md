## This is whole ciphertext. 48 bytes, but AES use 16 bit, so split on three parts:
### https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation
## From the how CBC works we know that all of them are dependent of each other

Steps to reproduce:

1. Split whole ciphertext to three 16-bytes parts
C1: 9f17f2a3a4c612ec41b09849f9e03c02
C2: 029f1c6f27e69972c91b01d17ffe6e8d
C3: 2c1f5684b0a32b0bf1347016d68e8a62

2. From the how CBC works we know that all of them are dependent of each other
C1 = D(IV ^ Plaintext_1)
C2 = D(C1 ^ Plaintext_2)
C3 = D(C2 ^ Plaintext_3)

## And a ^ b = c the same as a = b ^ c, then

Plaintext_2 = D(C2) ^ C1
Plaintext_3 = D(C3) ^ C2

## and then

Plaintext_2 = D(029f1c6f27e69972c91b01d17ffe6e8d) ^ 9f17f2a3a4c612ec41b09849f9e03c02
Plaintext_3 = D(2c1f5684b0a32b0bf1347016d68e8a62) ^ 029f1c6f27e69972c91b01d17ffe6e8d

3. Decrypt 029f1c6f27e69972c91b01d17ffe6e8d and 2c1f5684b0a32b0bf1347016d68e8a62
Plaintext_2 = fc658bd3d0a969df22d2c77c8c835737 ^ 9f17f2a3a4c612ec41b09849f9e03c02
Plaintext_3 = 5dab6a5f1682c643fe4420f05edf4ff0 ^ 029f1c6f27e69972c91b01d17ffe6e8d

4. XOR them
Plaintext_2 = 63727970746f7b3363625f3575636b35
Plaintext_3 = 5f34763031645f31375f21212121217d

5. Connect to one piece
Plaintext_2 + Plaintext_3 = 63727970746f7b3363625f3575636b355f34763031645f31375f21212121217d

6. From HEX to string is:
crypto{3cb_5uck5_4v01d_17_!!!!!}