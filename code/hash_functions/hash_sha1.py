#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.sha1(data).digest()

# Example SHA-1 hashes

# Hash [] (the empty byte array)
string_data = ''
data = bytes.fromhex(string_data)
hash(data)
# da39a3ee5e6b4b0d3255bfef95601890afd80709

# Hash 'The quick brown fox jumps over the lazy dog'
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
hash(data)
# 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12

# Hash 'The quick brown fox jumps over the lazy dog.'
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
hash(data)
# 408d94384216f890ff7a0c3528e8bed1e0b01621
