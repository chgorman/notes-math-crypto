#!/usr/bin/env python3

import hashlib

print("Example SHA-2 hashes")
print("#"*72)
print()

# Hash [] (the empty byte array)
sha2 = hashlib.sha256()
string_data = ''
data = bytes.fromhex(string_data)
sha2.update(data)
print('sha2(\'%s\')' % string_data)
print(sha2.hexdigest())
print()

# Hash 'The quick brown fox jumps over the lazy dog'
sha2 = hashlib.sha256()
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
sha2.update(data)
print('sha2(\'%s\')' % string_data)
print(sha2.hexdigest())
print()

# Hash 'The quick brown fox jumps over the lazy dog.'
sha2 = hashlib.sha256()
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
sha2.update(data)
print('sha2(\'%s\')' % string_data)
print(sha2.hexdigest())
