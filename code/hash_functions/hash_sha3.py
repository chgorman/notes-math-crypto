#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()

# Example SHA-3 hashes

# Hash [] (the empty byte array)
string_data = ''
data = bytes.fromhex(string_data)
hash(data)
# a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a

# Hash 'The quick brown fox jumps over the lazy dog'
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
hash(data)
# 69070dda01975c8c120c3aada1b282394e7f032fa9cf32f4cb2259a0897dfc04

# Hash 'The quick brown fox jumps over the lazy dog.'
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
hash(data)
# a80f839cd4f83f6c3dafc87feae470045e4eb0d366397d5c6ce34ba1739f734d
