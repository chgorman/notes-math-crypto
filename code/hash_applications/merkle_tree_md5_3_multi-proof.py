#!/usr/bin/env python3

import hashlib

root = bytes.fromhex('a9250f9b87b54a884997c41042029ed9')

# Set up data and proof
x2  = bytes.fromhex('02020202020202020202020202020202')
x4  = bytes.fromhex('04040404040404040404040404040404')
x7  = bytes.fromhex('07070707070707070707070707070707')
y1  = bytes.fromhex('24311d9abc4077123c2c9a167afbe754')
y3  = bytes.fromhex('b09931959951caa2ac110feebbd16750')
y8  = bytes.fromhex('01e8f7a7da1a35b3138845a7a2f18b46')
y11 = bytes.fromhex('406c1b079725e8d5f889b5450c72c4f9')

# Merkle Proof
md5 = hashlib.md5(); md5.update(x2);     yHat2 = md5.digest()
md5 = hashlib.md5(); md5.update(x4);     yHat4 = md5.digest()
md5 = hashlib.md5(); md5.update(x7);     yHat7 = md5.digest()

md5 = hashlib.md5(); md5.update(y1);     md5.update(yHat2)
yHat9 = md5.digest()
md5 = hashlib.md5(); md5.update(y3);     md5.update(yHat4)
yHat10 = md5.digest()
md5 = hashlib.md5(); md5.update(yHat7);  md5.update(y8)
yHat12 = md5.digest()

md5 = hashlib.md5(); md5.update(yHat9);  md5.update(yHat10)
yHat13 = md5.digest()
md5 = hashlib.md5(); md5.update(y11);    md5.update(yHat12)
yHat14 = md5.digest()

md5 = hashlib.md5(); md5.update(yHat13); md5.update(yHat14)
yHat15 = md5.digest()

assert yHat15 == root # Valid
