#!/usr/bin/env python3

import hashlib

# Example of SHA-1 collision

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

file1 = "../../figures/hash_functions/shattered-1.pdf"
file2 = "../../figures/hash_functions/shattered-2.pdf"

# File 1
hash_md5_1  = md5(file1)
# ee4aa52b139d925f8d8884402b0a750c
hash_sha1_1 = sha1(file1)
# 38762cf7f55934b34d179ae6a4c80cadccbb7f0a

# File 2
hash_md5_2  = md5(file2)
# 5bd9d8cabc46041579a311230539b8d1
hash_sha1_2 = sha1(file2)
# 38762cf7f55934b34d179ae6a4c80cadccbb7f0a

assert hash_md5_1  != hash_md5_2  # Passes
assert hash_sha1_1 == hash_sha1_2 # Passes
