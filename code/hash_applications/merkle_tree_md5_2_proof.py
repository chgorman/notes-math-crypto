#!/usr/bin/env python3

import hashlib

root = bytes.fromhex('40c0b71ca488d334d266beecac02a16c')

# Set up data and proof
x2 = bytes.fromhex('22222222222222222222222222222222')
y3 = bytes.fromhex('28bfcf057ec5a48f18c3154c1f2bd324')
y4 = bytes.fromhex('b05df6fba6c1c53e8ddb98ffd386ffc8')


# Merkle Proof
md5 = hashlib.md5(); md5.update(x2);    yHat2 = md5.digest()
# fbc3cf71d993ca7bec2664357ccdac2b
md5 = hashlib.md5(); md5.update(yHat2); md5.update(y3)
yHat5 = md5.digest()
# 8f7a2a2dcd297872689e177953270f37
md5 = hashlib.md5(); md5.update(y4);    md5.update(yHat5)
yHat6 = md5.digest()
# 40c0b71ca488d334d266beecac02a16c

assert yHat6 == root # Valid
