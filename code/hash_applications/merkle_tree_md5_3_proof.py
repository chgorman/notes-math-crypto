#!/usr/bin/env python3

import hashlib

root = bytes.fromhex('a9250f9b87b54a884997c41042029ed9')

# Set up data and proof
x5  = bytes.fromhex('05050505050505050505050505050505')
y6  = bytes.fromhex('e5f636381c9702b63aa666ef2a6f8e20')
y12 = bytes.fromhex('6b169c5ae04d0da8360ec5475c16983a')
y13 = bytes.fromhex('4ed351819fee1c3b3ecfe7620bed7a5c')

# Merkle Proof
md5 = hashlib.md5(); md5.update(x5);     yHat5 = md5.digest()
# af52282db55243f4c147ba5d7fb1155a
md5 = hashlib.md5(); md5.update(yHat5);  md5.update(y6)
yHat11 = md5.digest()
# 406c1b079725e8d5f889b5450c72c4f9
md5 = hashlib.md5(); md5.update(yHat11); md5.update(y12)
yHat14 = md5.digest()
# f63aee7a89333c34333544fb87ac424c
md5 = hashlib.md5(); md5.update(y13);    md5.update(yHat14)
yHat15 = md5.digest()
# a9250f9b87b54a884997c41042029ed9

assert yHat15 == root # Valid
