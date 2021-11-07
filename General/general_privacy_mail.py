from Crypto.PublicKey import RSA

pathToMail = 'General/privacy_enhanced_mail.pem'
file = open(pathToMail, 'r').read()

input = RSA.importKey(file)
output = input.d

print(output)