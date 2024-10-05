#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

xStr = '00112233445566778899aabbccddeeff'
x0 = bytes.fromhex(xStr)

x1 = hash(x0)
x2 = hash(x1)
x3 = hash(x2)
x4 = hash(x3)
x5 = hash(x4)

print("MD5 Hash Chain")
print("#"*72)
print()
print('x0 = %s' % (x0.hex()))
print()
print("x1 = md5(x0)")
print('   = %s' % (x1.hex()))
print()
print("x2 = md5(x1)")
print('   = %s' % (x2.hex()))
print()
print("x3 = md5(x2)")
print('   = %s' % (x3.hex()))
print()
print("x4 = md5(x3)")
print('   = %s' % (x4.hex()))
print()
print("x5 = md5(x4)")
print('   = %s' % (x5.hex()))
