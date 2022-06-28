#!/usr/bin/env python3

import hashlib

print("Example SHA-1 hashes")
print("#"*72)
print()

# Hash [] (the empty byte array)
sha1 = hashlib.sha1()
string_data = ''
data = bytes.fromhex(string_data)
sha1.update(data)
print('sha1(\'%s\')' % string_data)
print(sha1.hexdigest())
print()

# Hash 'The quick brown fox jumps over the lazy dog'
sha1 = hashlib.sha1()
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
sha1.update(data)
print('sha1(\'%s\')' % string_data)
print(sha1.hexdigest())
print()

# Hash 'The quick brown fox jumps over the lazy dog.'
sha1 = hashlib.sha1()
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
sha1.update(data)
print('sha1(\'%s\')' % string_data)
print(sha1.hexdigest())
