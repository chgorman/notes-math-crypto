#!/usr/bin/env python3

import hashlib

# Set up data
x1 = bytes.fromhex(''.join('01' for i in range(16)))
x2 = bytes.fromhex(''.join('02' for i in range(16)))
x3 = bytes.fromhex(''.join('03' for i in range(16)))
x4 = bytes.fromhex(''.join('04' for i in range(16)))
x5 = bytes.fromhex(''.join('05' for i in range(16)))
x6 = bytes.fromhex(''.join('06' for i in range(16)))
x7 = bytes.fromhex(''.join('07' for i in range(16)))
x8 = bytes.fromhex(''.join('08' for i in range(16)))

# Make Merkle Tree
md5 = hashlib.md5(); md5.update(x1);  y1 = md5.digest()
md5 = hashlib.md5(); md5.update(x2);  y2 = md5.digest()
md5 = hashlib.md5(); md5.update(x3);  y3 = md5.digest()
md5 = hashlib.md5(); md5.update(x4);  y4 = md5.digest()
md5 = hashlib.md5(); md5.update(x5);  y5 = md5.digest()
md5 = hashlib.md5(); md5.update(x6);  y6 = md5.digest()
md5 = hashlib.md5(); md5.update(x7);  y7 = md5.digest()
md5 = hashlib.md5(); md5.update(x8);  y8 = md5.digest()

md5 = hashlib.md5(); md5.update(y1);  md5.update(y2)
y9 = md5.digest()
md5 = hashlib.md5(); md5.update(y3);  md5.update(y4)
y10 = md5.digest()
md5 = hashlib.md5(); md5.update(y5);  md5.update(y6)
y11 = md5.digest()
md5 = hashlib.md5(); md5.update(y7);  md5.update(y8)
y12 = md5.digest()

md5 = hashlib.md5(); md5.update(y9);  md5.update(y10)
y13 = md5.digest()
md5 = hashlib.md5(); md5.update(y11); md5.update(y12)
y14 = md5.digest()

md5 = hashlib.md5(); md5.update(y13); md5.update(y14)
y15 = md5.digest()
# a9250f9b87b54a884997c41042029ed9
