from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

def sign(key, msg):
    return PKCS1_v1_5.new(RSA.importKey(key)).sign(SHA256.new(msg.encode()))

def verify(key, msg, sign):
    return PKCS1_v1_5.new(RSA.importKey(key)).verify(SHA256.new(msg.encode()), sig)

key_pair = RSA.generate(2048, Random.new().read)
msg = "Hello, World!"
sig = sign(key_pair.export_key(), msg)

print("Generated Signature:", sig)
print("Signature Verification Result:", verify(key_pair.publickey().export_key(), msg, sig))
