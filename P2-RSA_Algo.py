from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")

pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")

privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

msg = b'Ismile Academy' 
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)

print("Encrypted:", binascii.hexlify(encrypted).decode('ascii'))
