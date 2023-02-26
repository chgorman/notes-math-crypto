#!/usr/bin/env python3

import hashlib

root = bytes.fromhex('18446692e822581d02b096e1b77c9fff')

# Set up data and proof
x   = bytes.fromhex('\
b40ebeba833c1c07e74d9e4c6ebb8230af52282db55243f4c147ba5d7fb1155a')
y11 = bytes.fromhex('70d0669eae8c7a5dce3b3ff4ccf4adbb')
y12 = bytes.fromhex('a3f21dba8fa8de359220c29c00467556')

# Merkle Proof
md5 = hashlib.md5(); md5.update(x);    yHat = md5.digest()
yHat10 = md5.digest()
md5 = hashlib.md5(); md5.update(yHat); md5.update(y11)
yHat13 = md5.digest()
md5 = hashlib.md5(); md5.update(y12);  md5.update(yHat13)
yHat14 = md5.digest()

print("3-Layer MD5 Merkle \"Proof\"")
print("#"*72)
print()
print("Merkle Root")
print('     %s' % (root.hex()))
print()

print("Data and \"Proof\"")
print()
print('x   = %s' % (x.hex()))
print('y11 = %s' % (y11.hex()))
print('y12 = %s' % (y12.hex()))
print()
print()


print("Merkle \"Proof\"")
print()

print('yHat   = md5(x)')
print('       = %s' % (yHat.hex()))
print('yHat13 = md5(yHat||y11   )')
print('       = %s' % (yHat13.hex()))
print('yHat14 = md5(y12 ||yHat13)')
print('       = %s' % (yHat14.hex()))
print()

assert yHat14 == root # Valid
print('Valid Proof')
