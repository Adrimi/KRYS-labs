# https://en.wikipedia.org/wiki/Weak_key#Weak_keys_in_DES

# Interdependent keys:
key = 'E0E0E0E0F1F1F1F1FEFEFEFEFEFEFEFE0101010101010101'

inv_key = '0101010101010101FEFEFEFEFEFEFEFEE0E0E0E0F1F1F1F1'

# And for every message with len multiply of 8 use inverted key to encrypt flag and then the result with mirrored key to instead of encoding get decoding :)

1. encrypt_flag(inv_key) -> 9f6ac7577c4d3f3424a02a66397f41395780be714c72eda4f3d51fece50395607775bb449307e472

2. encrypt(key, 1.) -> 63727970746f7b6e30745f346c6c5f6b3379735f3472335f673030645f6b3379737d060606060606

3. ASCII TO HEX -> crypto{n0t_4ll_k3ys_4r3_g00d_k3ys}
# THERE IS PADDING :)