#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

# Set up data
x0 = bytes.fromhex(''.join('00' for i in range(16)))
x1 = bytes.fromhex(''.join('01' for i in range(16)))
x2 = bytes.fromhex(''.join('02' for i in range(16)))
x3 = bytes.fromhex(''.join('03' for i in range(16)))
x4 = bytes.fromhex(''.join('04' for i in range(16)))
x5 = bytes.fromhex(''.join('05' for i in range(16)))
x6 = bytes.fromhex(''.join('06' for i in range(16)))
x7 = bytes.fromhex(''.join('07' for i in range(16)))

# Make Merkle Tree
y0 = hash(x0)
y1 = hash(x1)
y2 = hash(x2)
y3 = hash(x3)
y4 = hash(x4)
y5 = hash(x5)
y6 = hash(x6)
y7 = hash(x7)

y8  = hash(y0  + y1 )
y9  = hash(y2  + y3 )
y10 = hash(y4  + y5 )
y11 = hash(y6  + y7 )

y12 = hash(y8  + y9 )
y13 = hash(y10 + y11)

y14 = hash(y12 + y13)
# 18446692e822581d02b096e1b77c9fff
