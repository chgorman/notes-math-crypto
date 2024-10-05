#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

xStr = '00112233445566778899aabbccddeeff'
x0 = bytes.fromhex(xStr)
# 00112233445566778899aabbccddeeff

x1 = hash(x0)
# 6e8311168ee16d6aa1aa48c64145003c

x2 = hash(x1)
# 7a69fffa917aafaa21e54379fa990232

x3 = hash(x2)
# 30367bcf47ed16e934dc13e4c270e869

x4 = hash(x3)
# 5aef06528360f7185f08110aacb45f5d

x5 = hash(x4)
# e94712ae81bf26d81b0e7475fbf6b3f8
