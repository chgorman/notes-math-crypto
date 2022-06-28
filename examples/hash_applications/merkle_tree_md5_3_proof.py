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
md5 = hashlib.md5(); md5.update(yHat5);  md5.update(y6)
yHat11 = md5.digest()
md5 = hashlib.md5(); md5.update(yHat11); md5.update(y12)
yHat14 = md5.digest()
md5 = hashlib.md5(); md5.update(y13);    md5.update(yHat14)
yHat15 = md5.digest()

print("3-Layer MD5 Merkle Proof")
print("#"*72)
print()
print("Merkle Root")
print('     %s' % (root.hex()))
print()

print("Data and Proof")
print()
print('x5  = %s' % (x5.hex()))
print('y6  = %s' % (y6.hex()))
print('y12 = %s' % (y12.hex()))
print('y13 = %s' % (y13.hex()))
print()
print()


print("Merkle Proof")
print()

print('yHat5  = md5(x5)')
print('       = %s' % (yHat5.hex()))
print('yHat11 = md5(yHat5 ||y6    )')
print('       = %s' % (yHat11.hex()))
print('yHat14 = md5(yHat11||y12   )')
print('       = %s' % (yHat14.hex()))
print('yHat15 = md5(y13   ||yHat14)')
print('       = %s' % (yHat15.hex()))
print()

assert yHat15 == root # Valid
print('Valid Proof')
