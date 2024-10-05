#!/usr/bin/env python3

import hashlib
import math

print("expand_msg_xof using SHAKE128")
print("#"*72)
print()

def xof_shake128(data: bytes, length: int):
    return hashlib.shake_128(data).digest(length)

def expand_msg_xof(msg: bytes, dst: bytes, length: int):
    dst_prime = dst + len(dst).to_bytes(1, "big")
    lib = length.to_bytes(2, "big")
    msg_prime = msg + lib + dst_prime
    uniform_bytes = xof_shake128(msg_prime, length)
    return uniform_bytes

msg = b""
print('msg: %s' % (msg.hex()))
dst = b"QUUX-V01-CS02-with-expander-SHAKE128"
print('dst: %s' % (dst.hex()))
print()
length = 32
uniform_bytes = expand_msg_xof(msg, dst, length)

uniform_bytes_true = bytes.fromhex("86518c9cd86581486e9485aa74ab35ba150d1c75c88e26b7043e44e2acd735a2")
assert uniform_bytes == uniform_bytes_true, "invalid bytes 32"
print("length: %s" % length)
print("bytes:  %s" % uniform_bytes.hex())
print()

length = 128
uniform_bytes = expand_msg_xof(msg, dst, length)

uniform_bytes_true = bytes.fromhex("7314ff1a155a2fb99a0171dc71b89ab6e3b2b7d59e38e64419b8b6294d03ffee42491f11370261f436220ef787f8f76f5b26bdcd850071920ce023f3ac46847744f4612b8714db8f5db83205b2e625d95afd7d7b4d3094d3bdde815f52850bb41ead9822e08f22cf41d615a303b0d9dde73263c049a7b9898208003a739a2e57")
assert uniform_bytes == uniform_bytes_true, "invalid bytes 32"
print("length: %s" % length)
print("bytes:  %s" % uniform_bytes.hex())
print()
