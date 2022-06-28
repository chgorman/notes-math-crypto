#!/usr/bin/env python3

import hashlib

root = bytes.fromhex('74c2208dee857014164825cfbc045371')

# Set up data and proof
x3 = bytes.fromhex('33333333333333333333333333333333')
y4 = bytes.fromhex('629f0b541d8ebec86267b948c0381de5')
y5 = bytes.fromhex('7536b40f7385c138406ae2cd703e2bad')

# Merkle Proof
md5 = hashlib.md5(); md5.update(x3);    yHat3 = md5.digest()
# 28bfcf057ec5a48f18c3154c1f2bd324
md5 = hashlib.md5(); md5.update(yHat3); md5.update(y4)
yHat6 = md5.digest()
# cfa3bb502293d3b8acaa608628ca06fb
md5 = hashlib.md5(); md5.update(y5);    md5.update(yHat6)
yHat7 = md5.digest()
# 74c2208dee857014164825cfbc045371

assert yHat7 == root # Valid
