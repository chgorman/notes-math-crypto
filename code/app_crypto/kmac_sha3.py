#!/usr/bin/env python3

import hashlib

# Set up key and message
preKey = bytes.fromhex(''.join('13' for i in range(32)))
sha3 = hashlib.sha3_256(); sha3.update(preKey)
key = sha3.digest()
# 0554a7d12c7a1bfcb47088e98851c036ca90c3e2d2b0ef6d88b341d86ec6bd4a
msg = bytes.fromhex(''.join('42' for i in range(32)))
# 4242424242424242424242424242424242424242424242424242424242424242

# Pad key
padding = sha3.block_size-len(key)
zeroPad = bytes.fromhex(''.join('00' for i in range(padding)))
keyPrime = key + zeroPad

# Compute value
sha3 = hashlib.sha3_256(); sha3.update(keyPrime); sha3.update(msg)
t = sha3.digest()
# b4033d41cef0553003b8e1b189fae0c44283a4b1870f59cdd8a8133a7d31c585
