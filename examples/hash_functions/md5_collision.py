#!/usr/bin/env python3

import hashlib

print("Example MD5 Collision")
print("#"*72)
print()

# Hash of message1.bin
md5 = hashlib.md5()
string_data = '\
4dc968ff 0ee35c20 9572d477 7b721587\n\
d36fa7b2 1bdc56b7 4a3dc078 3e7b9518\n\
afbfa200 a8284bf3 6e8e4b55 b35f4275\n\
93d84967 6da0d155 5d8360fb 5f07fea2\n'
data = bytes.fromhex(string_data)
md5.update(data)
hash_md5_1 = md5.hexdigest()
m1 = "message1"
print("%s = " % m1)
print("%s" % string_data)
print('md5(\'%s\')' % m1)
print(hash_md5_1)
print()

sha1 = hashlib.sha1()
sha1.update(data)
hash_sha1_1 = sha1.hexdigest()
print('sha1(\'%s\')' % m1)
print(hash_sha1_1)
print()
print()

# Hash of message2.bin
md5 = hashlib.md5()
sha1 = hashlib.sha1()
string_data = '\
4dc968ff 0ee35c20 9572d477 7b721587\n\
d36fa7b2 1bdc56b7 4a3dc078 3e7b9518\n\
afbfa202 a8284bf3 6e8e4b55 b35f4275\n\
93d84967 6da0d1d5 5d8360fb 5f07fea2\n'
data = bytes.fromhex(string_data)
md5.update(data)
hash_md5_2 = md5.hexdigest()
m2 = "message2"
print("%s = " % m2)
print("%s" % string_data)
print('md5(\'%s\')' % m2)
print(hash_md5_2)
print()

sha1 = hashlib.sha1()
sha1.update(data)
hash_sha1_2 = sha1.hexdigest()
print('sha1(\'%s\')' % m2)
print(hash_sha1_2)
print()
print()

assert hash_md5_1 == hash_md5_2 # Passes
print("md5  hash values: equal")
assert hash_sha1_1 != hash_sha1_2 # Passes
print("sha1 hash values: different")
