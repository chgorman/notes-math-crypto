#!/usr/bin/env python3

import hashlib

xStr = '00112233445566778899aabbccddeeff'
x0 = bytes.fromhex(xStr)
# 00112233445566778899aabbccddeeff

md5 = hashlib.md5()
md5.update(x0)
x1 = md5.digest()
# 6e8311168ee16d6aa1aa48c64145003c

md5 = hashlib.md5()
md5.update(x1)
x2 = md5.digest()
# 7a69fffa917aafaa21e54379fa990232

md5 = hashlib.md5()
md5.update(x2)
x3 = md5.digest()
# 30367bcf47ed16e934dc13e4c270e869

md5 = hashlib.md5()
md5.update(x3)
x4 = md5.digest()
# 5aef06528360f7185f08110aacb45f5d

md5 = hashlib.md5()
md5.update(x4)
x5 = md5.digest()
# e94712ae81bf26d81b0e7475fbf6b3f8
