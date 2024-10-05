#!/usr/bin/env python3

import hashlib
import math

def xof_shake128(data: bytes, length: int):
    return hashlib.shake_128(data).digest(length)

def expand_msg_xof(msg: bytes, dst: bytes, length: int):
    dst_prime = dst + len(dst).to_bytes(1, "big")
    lib = length.to_bytes(2, "big")
    msg_prime = msg + lib + dst_prime
    uniform_bytes = xof_shake128(msg_prime, length)
    return uniform_bytes

msg = b""
dst = b"QUUX-V01-CS02-with-expander-SHAKE128"
length = 32

uniform_bytes = expand_msg_xof(msg, dst, length)
# 86518c9cd86581486e9485aa74ab35ba150d1c75c88e26b7043e44e2acd735a2
