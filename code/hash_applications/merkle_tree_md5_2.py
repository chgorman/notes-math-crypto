#!/usr/bin/env python3

import hashlib

# Set up data
x0 = bytes.fromhex(''.join('00' for i in range(16)))
x1 = bytes.fromhex(''.join('11' for i in range(16)))
x2 = bytes.fromhex(''.join('22' for i in range(16)))
x3 = bytes.fromhex(''.join('33' for i in range(16)))

# Make Merkle Tree
md5 = hashlib.md5(); md5.update(x0); y0 = md5.digest()
# 4ae71336e44bf9bf79d2752e234818a5
md5 = hashlib.md5(); md5.update(x1); y1 = md5.digest()
# 8057b6feaa62d90126274cf9ba31c642
md5 = hashlib.md5(); md5.update(x2); y2 = md5.digest()
# fbc3cf71d993ca7bec2664357ccdac2b
md5 = hashlib.md5(); md5.update(x3); y3 = md5.digest()
# 28bfcf057ec5a48f18c3154c1f2bd324

md5 = hashlib.md5(); md5.update(y0); md5.update(y1)
y4 = md5.digest()
# b05df6fba6c1c53e8ddb98ffd386ffc8
md5 = hashlib.md5(); md5.update(y2); md5.update(y3)
y5 = md5.digest()
# 8f7a2a2dcd297872689e177953270f37

md5 = hashlib.md5(); md5.update(y4); md5.update(y5)
y6 = md5.digest()
# 40c0b71ca488d334d266beecac02a16c
