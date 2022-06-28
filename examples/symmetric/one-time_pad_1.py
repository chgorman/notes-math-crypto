#!/usr/bin/env python3

message = bytes.fromhex('00112233445566778899aabbccddeeff')
key =     bytes.fromhex('aa31553ea3fd3f015c4bffac26447514')

print("One-Time Pad 1")
print("#"*72)
print()
print("message:    %s" % message.hex())
print("key:        %s" % key.hex())

ciphertext = bytes(a ^ b for a,b in zip(key, message))
print()
print("Encryption")
print("ciphertext: %s" % ciphertext.hex())
print()

message_prime = bytes(a ^ b for a,b in zip(key, ciphertext))
print("Decryption")
print("message:    %s" % message_prime.hex())
print()

assert message == message_prime # Valid
print("Valid encryption and decryption")
