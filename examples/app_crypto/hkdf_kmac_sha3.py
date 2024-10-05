#!/usr/bin/env python3

import hashlib
import math

def hash_sha3(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()

# This version of KMAC does not follow the NIST spec
def kmac_sha3(key: bytes, msg: bytes) -> bytes:
    block_size = hashlib.sha3_256().block_size
    r = len(key) % block_size
    pad = block_size-r
    z_pad = bytes.fromhex(''.join('00' for i in range(pad)))
    return hash_sha3(key + z_pad + msg)

def hkdf(length: int, skm, salt: bytes = b"", ctx: bytes = b""):
    hash_len = hashlib.sha3_256().digest_size
    if len(salt) == 0:
        salt = bytes([0] * hash_len)
    prk = kmac_sha3(salt, skm)
    t = b""
    okm = b""
    for i in range(math.ceil(length / hash_len)):
        t = kmac_sha3(prk, t + ctx + bytes([i + 1]))
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

