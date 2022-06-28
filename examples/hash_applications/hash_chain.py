#!/usr/bin/env python3

import hashlib

xStr = '00112233445566778899aabbccddeeff'
x0 = bytes.fromhex(xStr)

md5 = hashlib.md5()
md5.update(x0)
x1 = md5.digest()

md5 = hashlib.md5()
md5.update(x1)
x2 = md5.digest()

md5 = hashlib.md5()
md5.update(x2)
x3 = md5.digest()

md5 = hashlib.md5()
md5.update(x3)
x4 = md5.digest()

md5 = hashlib.md5()
md5.update(x4)
x5 = md5.digest()

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
