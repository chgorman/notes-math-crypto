#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

# Set up data
x0 = bytes.fromhex(''.join('00' for i in range(16)))
x1 = bytes.fromhex(''.join('11' for i in range(16)))
x2 = bytes.fromhex(''.join('22' for i in range(16)))
x3 = bytes.fromhex(''.join('33' for i in range(16)))

# Make hashes
y0 = hash(x0)
y1 = hash(x1)
y2 = hash(x2)
y3 = hash(x3)

y4 = hash(y0 + y1)
y5 = hash(y2 + y3)

y6 = hash(y4 + y5)
print("2-Layer MD5 Merkle Tree")
print("#"*72)
print()
print("Data")
print()
print('x0 = %s' % (x0.hex()))
print('x1 = %s' % (x1.hex()))
print('x2 = %s' % (x2.hex()))
print('x3 = %s' % (x3.hex()))
print()
print()

print("Merkle Tree")
print()
print('y0 = md5(x0)')
print('   = %s' % (y0.hex()))
print('y1 = md5(x1)')
print('   = %s' % (y1.hex()))
print('y2 = md5(x2)')
print('   = %s' % (y2.hex()))
print('y3 = md5(x3)')
print('   = %s' % (y3.hex()))
print()

print('y4 = md5(y0||y1)')
print('   = %s' % (y4.hex()))
print('y5 = md5(y2||y3)')
print('   = %s' % (y5.hex()))
print()

print('y6 = md5(y4||y5)')
print('   = %s' % (y6.hex()))
