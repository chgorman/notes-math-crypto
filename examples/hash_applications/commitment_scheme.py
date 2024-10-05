#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

print("Commitment Scheme using MD5")
print("#"*72)
print()

rPreStr = '00'*16
rPre = bytes.fromhex(rPreStr)
r = hash(rPre)
print('randomization: %s' % (r.hex()))

mStr = '01'
m = bytes.fromhex(mStr)
print('message:       %s' % (m.hex()))

c = hash(r + m)
print('commitment:    %s' % (c.hex()))
print()
print('%s = md5(%s||%s)' % (c.hex(), r.hex(), m.hex()))
