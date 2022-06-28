#!/usr/bin/env python3

import hashlib

print("Example MD5 hashes")
print("#"*72)
print()

# Hash [] (the empty byte array)
md5 = hashlib.md5()
string_data = ''
data = bytes.fromhex(string_data)
md5.update(data)
print('md5(\'%s\')' % string_data)
print(md5.hexdigest())
print()

# Hash 'The quick brown fox jumps over the lazy dog'
md5 = hashlib.md5()
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
md5.update(data)
print('md5(\'%s\')' % string_data)
print(md5.hexdigest())
print()

# Hash 'The quick brown fox jumps over the lazy dog.'
md5 = hashlib.md5()
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
md5.update(data)
print('md5(\'%s\')' % string_data)
print(md5.hexdigest())
