#!/usr/bin/env python3

import hashlib
import hmac

def hash_md5(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

def hmac_md5(key: bytes, msg: bytes) -> bytes:
    block_size = hashlib.md5().block_size

    # Pad key
    if len(key) > block_size:
        key = hash_md5(key)
    pad = block_size-len(key)
    z_pad = bytes.fromhex(''.join('00' for i in range(pad)))
    key_prime = key + z_pad

    # Derive inner and outer keys
    ipad = bytes.fromhex(''.join('36' for i in range(block_size)))
    opad = bytes.fromhex(''.join('5c' for i in range(block_size)))
    key1 = bytes([a^b for (a,b) in zip(key_prime, ipad)])
    key2 = bytes([a^b for (a,b) in zip(key_prime, opad)])

    # Compute value
    tmp  = hash_md5(key1 + msg)
    return hash_md5(key2 + tmp)

print("HMAC-MD5")
print("#"*72)
print()

# Set up key and message
pre_key = bytes.fromhex(''.join('13' for i in range(16)))
key = hash_md5(pre_key)
print('key: %s' % (key.hex()))

msg = bytes.fromhex(''.join('42' for i in range(32)))
print('msg: %s' % (msg.hex()))
print()

t = hmac_md5(key, msg)
print('tag: %s' % (t.hex()))
print()

# Correct value
hmac_md5_def = hmac.new(key, digestmod=hashlib.md5)
hmac_md5_def.update(msg)
ret = hmac_md5_def.digest()

assert t == ret # Valid hmac
print('Valid tag')
