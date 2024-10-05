#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

r_pre_str = '00'*16
r_pre = bytes.fromhex(r_pre_str)
r = hash(r_pre)
# 4ae71336e44bf9bf79d2752e234818a5

m_str = '01'
m = bytes.fromhex(m_str)
# 01

c = hash(r + m)
# ff95213ae708e6443c5f0ae2d8f5fe41
