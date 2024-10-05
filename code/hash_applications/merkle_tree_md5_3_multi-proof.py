#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

root = bytes.fromhex('18446692e822581d02b096e1b77c9fff')

# Set up data and proof
x1  = bytes.fromhex('01010101010101010101010101010101')
x3  = bytes.fromhex('03030303030303030303030303030303')
x6  = bytes.fromhex('06060606060606060606060606060606')
y0  = bytes.fromhex('4ae71336e44bf9bf79d2752e234818a5')
y2  = bytes.fromhex('437b25ad27df2f61eb14c6400ae98309')
y7  = bytes.fromhex('a4aa9a02aa65f31d17dce9f944a57ab2')
y10 = bytes.fromhex('524856d86cb1006e9e9e9149f36b2875')

# Merkle Proof
yHat1  = hash(x1)
yHat3  = hash(x3)
yHat6  = hash(x6)

yHat8  = hash(y0     + yHat1 )
yHat9  = hash(y2     + yHat3 )
yHat11 = hash(yHat6  + y7    )

yHat12 = hash(yHat8  + yHat9 )
yHat13 = hash(y10    + yHat11)

yHat14 = hash(yHat12 + yHat13)

assert yHat14 == root # Valid
