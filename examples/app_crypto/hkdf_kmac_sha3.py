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

print("HKDF-KMAC-SHA3-256")
print("#"*72)
print()

skmPre  = bytes.fromhex("01" * 16)
skm = hashlib.md5(skmPre).digest() + bytes.fromhex("00" * 16)
print('skm:  %s' % (skm.hex()))
salt = bytes.fromhex("02" * 32)
print('salt: %s' % (salt.hex()))
ctx = b""
print('ctx:  %s' % (ctx.hex()))
print()

okm1 = hkdf(16, skm, salt, ctx)
print("hkdf(16, skm, salt, ctx):")
print('      %s' % (okm1.hex()))
okm2 = hkdf(32, skm, salt, ctx)
print("hkdf(32, skm, salt, ctx):")
print('      %s' % (okm2.hex()))
okm3 = hkdf(64, skm, salt, ctx)
print("hkdf(64, skm, salt, ctx):")
print('      %s\\' % (okm3[:32].hex()))
print('      %s' % (okm3[32:].hex()))

