#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()

print("Example SHA-3 hashes")
print("#"*72)
print()

# Hash [] (the empty byte array)
string_data = ''
data = bytes.fromhex(string_data)
res = hash(data)
print('sha3(\'%s\')' % string_data)
print(res.hex())
print()

# Hash 'The quick brown fox jumps over the lazy dog'
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
res = hash(data)
print('sha3(\'%s\')' % string_data)
print(res.hex())
print()

# Hash 'The quick brown fox jumps over the lazy dog.'
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
res = hash(data)
print('sha3(\'%s\')' % string_data)
print(res.hex())
