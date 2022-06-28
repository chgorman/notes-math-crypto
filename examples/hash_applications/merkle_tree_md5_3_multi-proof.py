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

print("3-Layer MD5 Merkle Multi-Proof")
print("#"*72)
print()
print("Merkle Root")
print('     %s' % (root.hex()))
print()

print("Data and Proof")
print()
print('x2  = %s' % (x2.hex()))
print('x4  = %s' % (x4.hex()))
print('x7  = %s' % (x7.hex()))
print('y1  = %s' % (y1.hex()))
print('y3  = %s' % (y3.hex()))
print('y8  = %s' % (y8.hex()))
print('y11 = %s' % (y11.hex()))
print()
print()

print("Merkle Proof")
print()

print('yHat2  = md5(x2)')
print('       = %s' % (yHat2.hex()))
print('yHat4  = md5(x4)')
print('       = %s' % (yHat4.hex()))
print('yHat7  = md5(x7)')
print('       = %s' % (yHat7.hex()))
print('yHat9  = md5(y1    ||yHat2 )')
print('       = %s' % (yHat9.hex()))
print('yHat10 = md5(y3    ||yHat4 )')
print('       = %s' % (yHat10.hex()))
print('yHat12 = md5(yHat7 ||y8    )')
print('       = %s' % (yHat12.hex()))
print('yHat13 = md5(yHat9 ||yHat10)')
print('       = %s' % (yHat13.hex()))
print('yHat14 = md5(y11   ||yHat12)')
print('       = %s' % (yHat14.hex()))
print('yHat15 = md5(yHat13||yHat14)')
print('       = %s' % (yHat15.hex()))
print()

assert yHat15 == root # Valid
print('Valid Proof')
