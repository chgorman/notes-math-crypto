#!/usr/bin/env python3

message = bytes.fromhex('00112233445566778899aabbccddeeff')
key =     bytes.fromhex('09fa37f922072f9cd36cfbc4936d5712')

ciphertext = bytes(a ^ b for a,b in zip(key, message))
# 09eb15ca665249eb5bf5517f5fb0b9ed

message_prime = bytes(a ^ b for a,b in zip(key, ciphertext))
# 00112233445566778899aabbccddeeff

assert message == message_prime # Valid
