#!/usr/bin/env python3

import hashlib
import hmac

print("HMAC-MD5")
print("#"*72)
print()

# Set up key and message
preKey = bytes.fromhex(''.join('13' for i in range(16)))
md5 = hashlib.md5(); md5.update(preKey)
key = md5.digest()
print('key: %s' % (key.hex()))

msg = bytes.fromhex(''.join('42' for i in range(32)))
print('msg: %s' % (msg.hex()))
print()

# Pad key
padding = md5.block_size-len(key)
zeroPad = bytes.fromhex(''.join('00' for i in range(padding)))
keyPrime = key + zeroPad

# Derive inner and outer keys
ipad = bytes.fromhex(''.join('36' for i in range(md5.block_size)))
opad = bytes.fromhex(''.join('5c' for i in range(md5.block_size)))
key1 = bytes([a^b for (a,b) in zip(keyPrime, ipad)])
key2 = bytes([a^b for (a,b) in zip(keyPrime, opad)])

# Compute value
md5 = hashlib.md5(); md5.update(key1); md5.update(msg)
tmp = md5.digest()
md5 = hashlib.md5(); md5.update(key2); md5.update(tmp)
t = md5.digest()
print('tag: %s' % (t.hex()))
print()

# Correct value
hmac_md5 = hmac.new(key, digestmod=hashlib.md5)
hmac_md5.update(msg)
ret = hmac_md5.digest()

assert t == ret # Valid hmac
print('Valid tag')
