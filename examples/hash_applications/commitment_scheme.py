#!/usr/bin/env python3

import hashlib

print("Commitment Scheme using MD5")
print("#"*72)
print()

rPreStr = '00'*16
rPre = bytes.fromhex(rPreStr)
md5 = hashlib.md5()
md5.update(rPre)
r = md5.digest()
print('randomization: %s' % (r.hex()))

mStr = '01'
m = bytes.fromhex(mStr)
print('message:       %s' % (m.hex()))

md5 = hashlib.md5()
md5.update(r)
md5.update(m)
c = md5.digest()
print('commitment:    %s' % (c.hex()))
print()
print('%s = md5(%s||%s)' % (c.hex(), r.hex(), m.hex()))
