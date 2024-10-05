#!/usr/bin/env python3

import hashlib

def hash_md5(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

def hash_sha1(data: bytes) -> bytes:
    return hashlib.sha1(data).digest()

print("Example MD5 Collision")
print("#"*72)
print()

# Hash of message1.bin
string_data_1 = '\
4dc968ff 0ee35c20 9572d477 7b721587\n\
d36fa7b2 1bdc56b7 4a3dc078 3e7b9518\n\
afbfa200 a8284bf3 6e8e4b55 b35f4275\n\
93d84967 6da0d155 5d8360fb 5f07fea2\n'
data_1 = bytes.fromhex(string_data_1)
res_md5_1 = hash_md5(data_1)
hash_md5_1 = res_md5_1.hex()
m1 = "message1"
print("%s = " % m1)
print("%s" % string_data_1)
print('md5(\'%s\')' % m1)
print(hash_md5_1)
print()

res_sha1_1 = hash_sha1(data_1)
hash_sha1_1 = res_sha1_1.hex()
print('sha1(\'%s\')' % m1)
print(hash_sha1_1)
print()
print()

# Hash of message2.bin
string_data_2 = '\
4dc968ff 0ee35c20 9572d477 7b721587\n\
d36fa7b2 1bdc56b7 4a3dc078 3e7b9518\n\
afbfa202 a8284bf3 6e8e4b55 b35f4275\n\
93d84967 6da0d1d5 5d8360fb 5f07fea2\n'
data_2 = bytes.fromhex(string_data_2)
res_md5_2 = hash_md5(data_2)
hash_md5_2 = res_md5_2.hex()
m2 = "message2"
print("%s = " % m2)
print("%s" % string_data_2)
print('md5(\'%s\')' % m2)
print(hash_md5_2)
print()

res_sha1_2 = hash_sha1(data_2)
hash_sha1_2 = res_sha1_2.hex()
print('sha1(\'%s\')' % m2)
print(hash_sha1_2)
print()
print()

assert hash_md5_1  == hash_md5_2  # Passes
print("md5  hash values: equal")
assert hash_sha1_1 != hash_sha1_2 # Passes
print("sha1 hash values: different")
