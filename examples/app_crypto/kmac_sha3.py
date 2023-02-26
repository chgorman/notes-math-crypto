#!/usr/bin/env python3

import hashlib

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

# Pad key
padding = sha3.block_size-len(key)
zeroPad = bytes.fromhex(''.join('00' for i in range(padding)))
keyPrime = key + zeroPad

# Compute value
sha3 = hashlib.sha3_256(); sha3.update(keyPrime); sha3.update(msg)
t = sha3.digest()
print('tag: %s' % (t.hex()))
