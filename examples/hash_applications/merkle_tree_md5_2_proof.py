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
yHat5 = hash(yHat2 + y3   )
yHat6 = hash(y4    + yHat5)

print("2-Layer MD5 Merkle Proof")
print("#"*72)
print()
print("Merkle Root")
print('     %s' % (root.hex()))
print()

print("Data and Proof")
print()
print('x2 = %s' % (x2.hex()))
print('y3 = %s' % (y3.hex()))
print('y4 = %s' % (y4.hex()))
print()
print()

print("Merkle Proof")
print()

print('yHat2 = md5(x2)')
print('      = %s' % (yHat2.hex()))
print('yHat5 = md5(yHat2||y3   )')
print('      = %s' % (yHat5.hex()))
print('yHat6 = md5(y4   ||yHat5)')
print('      = %s' % (yHat6.hex()))
print()

assert yHat6 == root # Valid
print('Valid Proof')
