#!/usr/bin/env python3

message = bytes.fromhex('00112233445566778899aabbccddeeff')
key =     bytes.fromhex('aa31553ea3fd3f015c4bffac26447514')

ciphertext = bytes(a ^ b for a,b in zip(key, message))
# aa20770de7a85976d4d25517ea999beb

message_prime = bytes(a ^ b for a,b in zip(key, ciphertext))
# 00112233445566778899aabbccddeeff

assert message == message_prime # Valid
