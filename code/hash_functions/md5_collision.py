#!/usr/bin/env python3

import hashlib

# Example of MD5 collision

# Hash of message 1
md5 = hashlib.md5()
string_1 = '4dc968ff 0ee35c20 9572d477 7b721587 \
            d36fa7b2 1bdc56b7 4a3dc078 3e7b9518 \
            afbfa200 a8284bf3 6e8e4b55 b35f4275 \
            93d84967 6da0d155 5d8360fb 5f07fea2'
data_1 = bytes.fromhex(string_1)
md5.update(data_1)
hash_md5_1 = md5.hexdigest()
# 008ee33a9d58b51cfeb425b0959121c9
sha1 = hashlib.sha1()
sha1.update(data_1)
hash_sha1_1 = sha1.hexdigest()
# c6b384c4968b28812b676b49d40c09f8af4ed4cc

# Hash of message 2
md5 = hashlib.md5()
sha1 = hashlib.sha1()
string_2 = '4dc968ff 0ee35c20 9572d477 7b721587 \
            d36fa7b2 1bdc56b7 4a3dc078 3e7b9518 \
            afbfa202 a8284bf3 6e8e4b55 b35f4275 \
            93d84967 6da0d1d5 5d8360fb 5f07fea2'
data_2 = bytes.fromhex(string_2)
md5.update(data_2)
hash_md5_2 = md5.hexdigest()
# 008ee33a9d58b51cfeb425b0959121c9
sha1 = hashlib.sha1()
sha1.update(data_2)
hash_sha1_2 = sha1.hexdigest()
# c728d8d93091e9c7b87b43d9e33829379231d7ca

assert hash_md5_1  == hash_md5_2  # Passes
assert hash_sha1_1 != hash_sha1_2 # Passes
