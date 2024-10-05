#!/usr/bin/env python3

def bytes_xor(a: bytes, b: bytes):
    assert len(a) == len(b), "unequal byte array lengths"
    return bytes(s ^ t for s, t in zip(a, b))

message = bytes.fromhex('00112233445566778899aabbccddeeff')
key =     bytes.fromhex('09fa37f922072f9cd36cfbc4936d5712')

ciphertext = bytes_xor(key, message)
# 09eb15ca665249eb5bf5517f5fb0b9ed

message_prime = bytes_xor(key, ciphertext)
# 00112233445566778899aabbccddeeff

assert message == message_prime # Valid
