#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

root = bytes.fromhex('18446692e822581d02b096e1b77c9fff')

# Set up data and proof
x   = bytes.fromhex('\
b40ebeba833c1c07e74d9e4c6ebb8230af52282db55243f4c147ba5d7fb1155a')
y11 = bytes.fromhex('70d0669eae8c7a5dce3b3ff4ccf4adbb')
y12 = bytes.fromhex('a3f21dba8fa8de359220c29c00467556')

# Merkle Proof
yHat   = hash(x)
# 524856d86cb1006e9e9e9149f36b2875
yHat13 = hash(yHat + y11   )
# da95d6882598892592ccd54bc89f7bdb
yHat14 = hash(y12  + yHat13)
# 18446692e822581d02b096e1b77c9fff

assert yHat14 == root # Valid
