#!/usr/bin/env python3

import hashlib
import hmac
import math

def hkdf(length: int, skm, salt: bytes = b"", ctx: bytes = b""):
    sha2 = hashlib.sha256()
    hash_len = sha2.digest_size
    if len(salt) == 0:
        salt = bytes([0] * hash_len)
    prk = hmac.new(salt, skm, digestmod=hashlib.sha256).digest()
    t = b""
    okm = b""
    for i in range(math.ceil(length / hash_len)):
        t = hmac.new(prk,
                     t + ctx + bytes([i + 1]),
                     digestmod=hashlib.sha256).digest()
        okm += t
    return okm[:length]

print("HKDF-HMAC-SHA2-256")
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
