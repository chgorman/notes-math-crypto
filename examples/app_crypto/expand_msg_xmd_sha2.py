#!/usr/bin/env python3

import hashlib
import math

print("expand_msg_xmd using SHA2-256")
print("#"*72)
print()

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
        b_im1 = output_array[i-2]
        b_tmp = bytes_xor(b_0, b_im1)
        b_i = hash_sha2(b_tmp + i.to_bytes(1, "big") + dst_prime)
        output_array += [b_i]
    uniform_bytes = b"".join(v for v in output_array)
    return uniform_bytes[:length]

msg = b""
print('msg: %s' % (msg.hex()))
dst = b"QUUX-V01-CS02-with-expander-SHA256-128"
print('dst: %s' % (dst.hex()))
print()
length = 32
uniform_bytes = expand_msg_xmd(msg, dst, length)

uniform_bytes_true = bytes.fromhex("68a985b87eb6b46952128911f2a4412bbc302a9d759667f87f7a21d803f07235")
assert uniform_bytes == uniform_bytes_true, "invalid bytes 32"
print("length: %s" % length)
print("bytes:  %s" % uniform_bytes.hex())
print()

length = 128
uniform_bytes = expand_msg_xmd(msg, dst, length)

uniform_bytes_true = bytes.fromhex("af84c27ccfd45d41914fdff5df25293e221afc53d8ad2ac06d5e3e29485dadbee0d121587713a3e0dd4d5e69e93eb7cd4f5df4cd103e188cf60cb02edc3edf18eda8576c412b18ffb658e3dd6ec849469b979d444cf7b26911a08e63cf31f9dcc541708d3491184472c2c29bb749d4286b004ceb5ee6b9a7fa5b646c993f0ced")
assert uniform_bytes == uniform_bytes_true, "invalid bytes 128"
print("length: %s" % length)
print("bytes:  %s" % uniform_bytes.hex())
