#!/usr/bin/env python3

import hashlib

# Example SHA-1 hashes

# Hash [] (the empty byte array)
sha1 = hashlib.sha1()
string_data = ''
data = bytes.fromhex(string_data)
sha1.update(data)
sha1.hexdigest()
# da39a3ee5e6b4b0d3255bfef95601890afd80709

# Hash 'The quick brown fox jumps over the lazy dog'
sha1 = hashlib.sha1()
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
sha1.update(data)
sha1.hexdigest()
# 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12

# Hash 'The quick brown fox jumps over the lazy dog.'
sha1 = hashlib.sha1()
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
sha1.update(data)
sha1.hexdigest()
# 408d94384216f890ff7a0c3528e8bed1e0b01621
