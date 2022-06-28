#!/usr/bin/env python3

import hashlib

print("Example SHA-3 hashes")
print("#"*72)
print()

# Hash [] (the empty byte array)
sha3 = hashlib.sha3_256()
string_data = ''
data = bytes.fromhex(string_data)
sha3.update(data)
print('sha3(\'%s\')' % string_data)
print(sha3.hexdigest())
print()

# Hash 'The quick brown fox jumps over the lazy dog'
sha3 = hashlib.sha3_256()
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
sha3.update(data)
print('sha3(\'%s\')' % string_data)
print(sha3.hexdigest())
print()

# Hash 'The quick brown fox jumps over the lazy dog.'
sha3 = hashlib.sha3_256()
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
sha3.update(data)
print('sha3(\'%s\')' % string_data)
print(sha3.hexdigest())
