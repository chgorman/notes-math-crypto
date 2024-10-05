#!/usr/bin/env python3

import hashlib

def hash_sha3(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()

def kmac_sha3(key: bytes, msg: bytes) -> bytes:
    block_size = hashlib.sha3_256().block_size
    r = len(key) % block_size
    pad = block_size-r
    z_pad = bytes.fromhex(''.join('00' for i in range(pad)))
    return hash_sha3(key + z_pad + msg)

print("KMAC-SHA3")
print("#"*72)
print()

# Set up key and message
preKey = bytes.fromhex(''.join('13' for i in range(32)))
sha3 = hashlib.sha3_256(); sha3.update(preKey)
key = sha3.digest()
print('key: %s' % (key.hex()))

msg = bytes.fromhex(''.join('42' for i in range(32)))
print('msg: %s' % (msg.hex()))
print()

# Compute value
t = kmac_sha3(key, msg)
print('tag: %s' % (t.hex()))
