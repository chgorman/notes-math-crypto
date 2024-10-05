#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

root = bytes.fromhex('18446692e822581d02b096e1b77c9fff')

# Set up data and proof
x4  = bytes.fromhex('04040404040404040404040404040404')
y5  = bytes.fromhex('af52282db55243f4c147ba5d7fb1155a')
y11 = bytes.fromhex('70d0669eae8c7a5dce3b3ff4ccf4adbb')
y12 = bytes.fromhex('a3f21dba8fa8de359220c29c00467556')

# Merkle Proof
yHat4  = hash(x4)
yHat10 = hash(yHat4  + y5    )
yHat13 = hash(yHat10 + y11   )
yHat14 = hash(y12    + yHat13)

print("3-Layer MD5 Merkle Proof")
print("#"*72)
print()
print("Merkle Root")
print('     %s' % (root.hex()))
print()

print("Data and Proof")
print()
print('x4  = %s' % (x4.hex()))
print('y5  = %s' % (y5.hex()))
print('y11 = %s' % (y11.hex()))
print('y12 = %s' % (y12.hex()))
print()
print()


print("Merkle Proof")
print()

print('yHat4  = md5(x4)')
print('       = %s' % (yHat4.hex()))
print('yHat10 = md5(yHat4 ||y5    )')
print('       = %s' % (yHat10.hex()))
print('yHat13 = md5(yHat10||y11   )')
print('       = %s' % (yHat13.hex()))
print('yHat14 = md5(y12   ||yHat13)')
print('       = %s' % (yHat14.hex()))
print()

assert yHat14 == root # Valid
print('Valid Proof')
