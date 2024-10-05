#!/usr/bin/env python3

def bytes_xor(a: bytes, b: bytes):
    assert len(a) == len(b), "unequal byte array lengths"
    return bytes(s ^ t for s, t in zip(a, b))

message = bytes.fromhex('00112233445566778899aabbccddeeff')
key =     bytes.fromhex('aa31553ea3fd3f015c4bffac26447514')

ciphertext = bytes_xor(key, message)
# aa20770de7a85976d4d25517ea999beb

message_prime = bytes_xor(key, ciphertext)
# 00112233445566778899aabbccddeeff

assert message == message_prime # Valid
