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

skmPre  = bytes.fromhex("01" * 16)
skm = hashlib.md5(skmPre).digest() + bytes.fromhex("00" * 16)
# 24311d9abc4077123c2c9a167afbe75400000000000000000000000000000000
salt = bytes.fromhex("02" * 32)
# 0202020202020202020202020202020202020202020202020202020202020202
ctx = b""

okm1 = hkdf(16, skm, salt, ctx)
# 209a24fb9c313a19d8ece110a922a75c
okm2 = hkdf(32, skm, salt, ctx)
# 209a24fb9c313a19d8ece110a922a75c7fdccb0ea20fff64eacf0bc621e688fe
okm3 = hkdf(64, skm, salt, ctx)
# 209a24fb9c313a19d8ece110a922a75c7fdccb0ea20fff64eacf0bc621e688fe\
# 9d905f252edb3b56a13609eaab6c13cd446a073ea08423c32b2fc009271d828c
