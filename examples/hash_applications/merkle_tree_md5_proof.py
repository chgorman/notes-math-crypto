#!/usr/bin/env python3

import hashlib

root = bytes.fromhex('74c2208dee857014164825cfbc045371')

# Set up data and proof
x3 = bytes.fromhex('33333333333333333333333333333333')
y4 = bytes.fromhex('629f0b541d8ebec86267b948c0381de5')
y5 = bytes.fromhex('7536b40f7385c138406ae2cd703e2bad')

# Merkle Proof
md5 = hashlib.md5(); md5.update(x3);    yHat3 = md5.digest()
md5 = hashlib.md5(); md5.update(yHat3); md5.update(y4)
yHat6 = md5.digest()
md5 = hashlib.md5(); md5.update(y5);    md5.update(yHat6)
yHat7 = md5.digest()

print("2-Layer MD5 Merkle Proof")
print("#"*72)
print()
print("Merkle Root")
print('     %s' % (root.hex()))
print()

print("Data and Proof")
print()
print('x3 = %s' % (x3.hex()))
print('y4 = %s' % (y4.hex()))
print('y5 = %s' % (y5.hex()))
print()
print()

print("Merkle Proof")
print()

print('yHat3 = md5(x3)')
print('      = %s' % (yHat3.hex()))
print('yHat6 = md5(yHat3||y4   )')
print('      = %s' % (yHat6.hex()))
print('yHat7 = md5(y5   ||yHat6)')
print('      = %s' % (yHat7.hex()))
print()

assert yHat7 == root # Valid
print('Valid Proof')
