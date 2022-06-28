#!/usr/bin/env python3

import hashlib

# Example SHA-2 hashes

# Hash [] (the empty byte array)
sha2 = hashlib.sha256()
string_data = ''
data = bytes.fromhex(string_data)
sha2.update(data)
sha2.hexdigest()
# e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

# Hash 'The quick brown fox jumps over the lazy dog'
sha2 = hashlib.sha256()
string_data = 'The quick brown fox jumps over the lazy dog'
data = str.encode(string_data)
sha2.update(data)
sha2.hexdigest()
# d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592

# Hash 'The quick brown fox jumps over the lazy dog.'
sha2 = hashlib.sha256()
string_data = 'The quick brown fox jumps over the lazy dog.'
data = str.encode(string_data)
sha2.update(data)
sha2.hexdigest()
# ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c
