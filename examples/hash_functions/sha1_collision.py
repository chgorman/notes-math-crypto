#!/usr/bin/env python3

import hashlib

print("Example SHA-1 Collision")
print("#"*72)
print()

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha1(fname):
    hash_sha1 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha1.update(chunk)
    return hash_sha1.hexdigest()

file1 = "shattered-1.pdf"
file2 = "shattered-2.pdf"

# File 1
hash_md5_1  = md5(file1)
print("md5(%s)  = %s" % (file1, hash_md5_1))
hash_sha1_1 = sha1(file1)
print("sha1(%s) = %s" % (file1, hash_sha1_1))
print()

# File 2
hash_md5_2  = md5(file2)
print("md5(%s)  = %s" % (file2, hash_md5_2))
hash_sha1_2 = sha1(file2)
print("sha1(%s) = %s" % (file2, hash_sha1_2))
print()
print()

assert hash_md5_1  != hash_md5_2  # Passes
print("md5  hash values: different")
assert hash_sha1_1 == hash_sha1_2 # Passes
print("sha1 hash values: equal")

