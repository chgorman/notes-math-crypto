#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

# Example MD5 hashes

# Hash [] (the empty byte array)
string_data = ''
data = bytes.fromhex(string_data)
hash(data)
# d41d8cd98f00b204e9800998ecf8427e

# Hash 'The quick brown fox jumps over the lazy dog'
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
hash(data)
# 9e107d9d372bb6826bd81d3542a419d6

# Hash 'The quick brown fox jumps over the lazy dog.'
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
hash(data)
# e4d909c290d0fb1ca068ffaddf22cbd0
