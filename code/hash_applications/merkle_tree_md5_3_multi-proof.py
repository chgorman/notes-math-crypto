#!/usr/bin/env python3

import hashlib

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
md5 = hashlib.md5(); md5.update(x1);     yHat1 = md5.digest()
md5 = hashlib.md5(); md5.update(x3);     yHat3 = md5.digest()
md5 = hashlib.md5(); md5.update(x6);     yHat6 = md5.digest()

md5 = hashlib.md5(); md5.update(y0);     md5.update(yHat1)
yHat8  = md5.digest()
md5 = hashlib.md5(); md5.update(y2);     md5.update(yHat3)
yHat9  = md5.digest()
md5 = hashlib.md5(); md5.update(yHat6);  md5.update(y7)
yHat11 = md5.digest()

md5 = hashlib.md5(); md5.update(yHat8);  md5.update(yHat9)
yHat12 = md5.digest()
md5 = hashlib.md5(); md5.update(y10);    md5.update(yHat11)
yHat13 = md5.digest()

md5 = hashlib.md5(); md5.update(yHat12); md5.update(yHat13)
yHat14 = md5.digest()

assert yHat14 == root # Valid
