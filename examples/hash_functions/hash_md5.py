#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

print("Example MD5 hashes")
print("#"*72)
print()

# Hash [] (the empty byte array)
string_data = ''
data = bytes.fromhex(string_data)
res  = hash(data)
print('md5(\'%s\')' % string_data)
print(res.hex())
print()

# Hash 'The quick brown fox jumps over the lazy dog'
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
res  = hash(data)
print('md5(\'%s\')' % string_data)
print(res.hex())
print()

# Hash 'The quick brown fox jumps over the lazy dog.'
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
res  = hash(data)
print('md5(\'%s\')' % string_data)
print(res.hex())
