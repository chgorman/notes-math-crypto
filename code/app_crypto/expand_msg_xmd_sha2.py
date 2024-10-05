#!/usr/bin/env python3

import hashlib
import math

def hash_sha2(data: bytes):
    return hashlib.sha256(data).digest()

def bytes_xor(a: bytes, b: bytes):
    assert len(a) == len(b), "unequal byte array lengths"
    return bytes(s ^ t for s, t in zip(a, b))

def expand_msg_xmd(msg: bytes, dst: bytes, length: int):
    b_in_bytes = hashlib.sha256().digest_size
    s_in_bytes = hashlib.sha256().block_size
    ell = math.ceil(length/b_in_bytes)
    dst_prime = dst + len(dst).to_bytes(1, "big")
    z_pad = bytes.fromhex("00" * s_in_bytes)
    lib = length.to_bytes(2, "big")
    msg_prime = z_pad + msg + lib + bytes.fromhex("00") + dst_prime
    b_0 = hash_sha2(msg_prime)
    b_1 = hash_sha2(b_0 + bytes.fromhex("01") + dst_prime)
    output_array = [b_1]
    for i in range(2, ell+1):
        b_im1 = output_bytes[i-2]
        b_tmp = bytes_xor(b_0, bim1)
        b_i = hash_sha2(b_tmp + i.to_bytes(1, "big") + dst_prime)
        output_array += [b_i]
    uniform_bytes = b"".join(v for v in output_array)
    return uniform_bytes[:length]

msg = b""
dst = b"QUUX-V01-CS02-with-expander-SHA256-128"
length = 32

uniform_bytes = expand_msg_xmd(msg, dst, length)
# 68a985b87eb6b46952128911f2a4412bbc302a9d759667f87f7a21d803f07235
