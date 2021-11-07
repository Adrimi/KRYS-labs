from Crypto.PublicKey import RSA

filepath1 = 'General/transparency.pem'
file1 = open(filepath1, 'r').read()

key1 = RSA.importKey(file1)

print(key1.export_key())

filepath2 = 'General/thetransparencyflagishere-cryptohack-org.pem'
file2 = open(filepath2, 'r').read()
key2 = RSA.import_key(file2)
kluczu = key2.export_key()

print(kluczu)
