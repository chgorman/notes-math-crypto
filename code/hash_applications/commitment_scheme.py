#!/usr/bin/env python3

import hashlib

rPreStr = '00'*16
rPre = bytes.fromhex(rPreStr)
md5 = hashlib.md5()
md5.update(rPre)
r = md5.digest()
# 4ae71336e44bf9bf79d2752e234818a5

mStr = '01'
m = bytes.fromhex(mStr)
# 01

md5 = hashlib.md5()
md5.update(r)
md5.update(m)
c = md5.digest()
# ff95213ae708e6443c5f0ae2d8f5fe41
