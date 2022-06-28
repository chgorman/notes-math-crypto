#!/usr/bin/env python3

import hashlib

# Set up data
x1 = bytes.fromhex(''.join('11' for i in range(16)))
x2 = bytes.fromhex(''.join('22' for i in range(16)))
x3 = bytes.fromhex(''.join('33' for i in range(16)))
x4 = bytes.fromhex(''.join('44' for i in range(16)))

# Make Merkle Tree
md5 = hashlib.md5(); md5.update(x1); y1 = md5.digest()
# 8057b6feaa62d90126274cf9ba31c642
md5 = hashlib.md5(); md5.update(x2); y2 = md5.digest()
# fbc3cf71d993ca7bec2664357ccdac2b
md5 = hashlib.md5(); md5.update(x3); y3 = md5.digest()
# 28bfcf057ec5a48f18c3154c1f2bd324
md5 = hashlib.md5(); md5.update(x4); y4 = md5.digest()
# 629f0b541d8ebec86267b948c0381de5

md5 = hashlib.md5(); md5.update(y1); md5.update(y2)
y5 = md5.digest()
# 7536b40f7385c138406ae2cd703e2bad
md5 = hashlib.md5(); md5.update(y3); md5.update(y4)
y6 = md5.digest()
# cfa3bb502293d3b8acaa608628ca06fb

md5 = hashlib.md5(); md5.update(y5); md5.update(y6)
y7 = md5.digest()
# 74c2208dee857014164825cfbc045371
