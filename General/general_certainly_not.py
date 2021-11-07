from Crypto.PublicKey import RSA
from ssl import DER_cert_to_PEM_cert

filepath = 'General/2048b-rsa-example-cert.der'
der = open(filepath, 'rb').read()

pem = DER_cert_to_PEM_cert(der)

key = RSA.importKey(pem).n

print(key)