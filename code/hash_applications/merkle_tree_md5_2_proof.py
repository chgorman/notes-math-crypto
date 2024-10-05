#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

root = bytes.fromhex('40c0b71ca488d334d266beecac02a16c')

# Set up data and proof
x2 = bytes.fromhex('22222222222222222222222222222222')
y3 = bytes.fromhex('28bfcf057ec5a48f18c3154c1f2bd324')
y4 = bytes.fromhex('b05df6fba6c1c53e8ddb98ffd386ffc8')


# Merkle Proof
yHat2 = hash(x2)
# fbc3cf71d993ca7bec2664357ccdac2b
yHat5 = hash(yHat2 + y3   )
# 8f7a2a2dcd297872689e177953270f37
yHat6 = hash(y4    + yHat5)
# 40c0b71ca488d334d266beecac02a16c

assert yHat6 == root # Valid
