# The same with ECB CBC WTF. CBC cipher text blocks are dependent on each other

plaintext_1 = D(C1) XOR C0
plaintext_0 = D(C0) XOR IV

plaintext_1 XOR plaintext_1 = D(C0) XOR D(C1) XOR C0 XOR IV

# Then when all ciphertexts blocks as zeros:
D(0) XOR D(0) XOR 0 XOR IV = IV

# So then steps are:
1. Receive(0000000000000000000000000000000000000000000000000000000000000000) -> 1f8a7951758a7ffa56275ea7a9f672f352b92c49ac7199d416afae9fdfbe9068
2. Split to two blocks: 
  1f8a7951758a7ffa56275ea7a9f672f3 
  52b92c49ac7199d416afae9fdfbe9068
3. XOR them -> 4d335518d9fbe62e4088f0387648e29b
4. Get_Flag(4d335518d9fbe62e4088f0387648e29b) -> 63727970746f7b35306d335f703330706c335f64306e375f3768316e6b5f49565f31355f316d70307237346e375f3f7d
5. HEX TO STRING -> crypto{50m3_p30pl3_d0n7_7h1nk_IV_15_1mp0r74n7_?}