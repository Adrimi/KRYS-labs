from Crypto.PublicKey import RSA
import subprocess

filepath = 'General/bruce_rsa.pub'
result = subprocess.run(['ssh-keygen', '-f' , filepath, '-e', '-m', 'pem'], stdout=subprocess.PIPE)

modulo = RSA.importKey(result.stdout).n

print(modulo)