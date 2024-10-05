#!/usr/bin/env python3

import hashlib
import math

def hash_md5(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

def hash_sha2(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()

def hmac_sha2(key: bytes, msg: bytes) -> bytes:
    block_size = hashlib.sha256().block_size

    # Pad key
    if len(key) > block_size:
        key = hash_md5(key)
    pad = block_size-len(key)
    z_pad = bytes.fromhex(''.join('00' for i in range(pad)))
    key_prime = key + z_pad

    # Derive inner and outer keys
    ipad = bytes.fromhex(''.join('36' for i in range(block_size)))
    opad = bytes.fromhex(''.join('5c' for i in range(block_size)))
    key1 = bytes([a^b for (a,b) in zip(key_prime, ipad)])
    key2 = bytes([a^b for (a,b) in zip(key_prime, opad)])

    # Compute value
    tmp  = hash_sha2(key1 + msg)
    return hash_sha2(key2 + tmp)

def hkdf(length: int, skm, salt: bytes = b"", ctx: bytes = b""):
    hash_len= hashlib.sha256().digest_size
    if len(salt) == 0:
        salt = bytes([0] * hash_len)
    prk = hmac_sha2(salt, skm)
    t = b""
    okm = b""
    for i in range(math.ceil(length / hash_len)):
        t = hmac_sha2(prk, t + ctx + bytes([i + 1]))
        okm += t
    return okm[:length]

print("HKDF-HMAC-SHA2-256")
print("#"*72)
print()

skm_pre  = bytes.fromhex("01" * 16)
skm = hash_md5(skm_pre) + bytes.fromhex("00" * 16)
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
