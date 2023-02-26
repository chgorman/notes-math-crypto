#!/usr/bin/env python3

import hashlib
import math

# This version of KMAC does not follow the NIST spec
def kmac(key: bytes, msg: bytes):
    sha3 = hashlib.sha3_256()
    key_len = len(key)
    assert key_len < sha3.block_size
    padding = bytes.fromhex("00" * (sha3.block_size - key_len))
    sha3.update(key); sha3.update(padding); sha3.update(msg)
    return sha3.digest()

def hkdf(length: int, skm, salt: bytes = b"", ctx: bytes = b""):
    sha3 = hashlib.sha3_256()
    hash_len = sha3.digest_size
    if len(salt) == 0:
        salt = bytes([0] * hash_len)
    prk = kmac(salt, skm)
    t = b""
    okm = b""
    for i in range(math.ceil(length / hash_len)):
        t = kmac(prk, t + ctx + bytes([i + 1]))
        okm += t
    return okm[:length]

skmPre  = bytes.fromhex("01" * 16)
skm = hashlib.md5(skmPre).digest() + bytes.fromhex("00" * 16)
# 24311d9abc4077123c2c9a167afbe75400000000000000000000000000000000
salt = bytes.fromhex("02" * 32)
# 0202020202020202020202020202020202020202020202020202020202020202
ctx = b""

okm1 = hkdf(16, skm, salt, ctx)
# f9b8dbec9e6ba6c6862cc45cfc408e0b
okm2 = hkdf(32, skm, salt, ctx)
# f9b8dbec9e6ba6c6862cc45cfc408e0b33b125aecff2705650f191b7cb599b74
okm3 = hkdf(64, skm, salt, ctx)
# f9b8dbec9e6ba6c6862cc45cfc408e0b33b125aecff2705650f191b7cb599b74\
# 02c32a28defa349720c44c449319f9cff77b211fa5262de491334409115c712d
