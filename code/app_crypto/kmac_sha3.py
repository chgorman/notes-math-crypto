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

# Set up key and message
pre_key = bytes.fromhex(''.join('13' for i in range(32)))
key = hash_sha3(pre_key)
# 0554a7d12c7a1bfcb47088e98851c036ca90c3e2d2b0ef6d88b341d86ec6bd4a
msg = bytes.fromhex(''.join('42' for i in range(32)))
# 4242424242424242424242424242424242424242424242424242424242424242

# Compute value
t = kmac_sha3(key, msg)
# b4033d41cef0553003b8e1b189fae0c44283a4b1870f59cdd8a8133a7d31c585
