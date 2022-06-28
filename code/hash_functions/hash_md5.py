#!/usr/bin/env python3

import hashlib

# Example MD5 hashes

# Hash [] (the empty byte array)
md5 = hashlib.md5()
string_data = ''
data = bytes.fromhex(string_data)
md5.update(data)
md5.hexdigest()
# d41d8cd98f00b204e9800998ecf8427e

# Hash 'The quick brown fox jumps over the lazy dog'
md5 = hashlib.md5()
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
md5.update(data)
md5.hexdigest()
# 9e107d9d372bb6826bd81d3542a419d6

# Hash 'The quick brown fox jumps over the lazy dog.'
md5 = hashlib.md5()
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
md5.update(data)
md5.hexdigest()
# e4d909c290d0fb1ca068ffaddf22cbd0
