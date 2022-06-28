#!/usr/bin/env python3

from mnemonic import Mnemonic
import hashlib

num_bytes = 20
num_bits = num_bytes*8
checksum_bits = num_bits//32
num_words = checksum_bits*3

# Short version

sha1 = hashlib.sha1()

mnemo = Mnemonic("english")

dataPre = bytes.fromhex('00'*num_bytes)
sha1.update(dataPre)
data = sha1.digest()
words = mnemo.to_mnemonic(data)
seed = Mnemonic.to_seed(words)

print("BIP-39 Mnemonic Seed Phrase; 160-bit entropy, sha1(zeros)")
print("#"*72)
print()
print("Data (hex)")
print(data.hex())
print()


# Long version

sha2 = hashlib.sha256()
sha2.update(data)
sha2digest = sha2.digest()
print("sha256(Data) (hex)")
print(sha2digest.hex())
print()
binary_string = "{:0256b}".format(int(sha2digest.hex(),16))
checksum_str = binary_string[:checksum_bits]
print("Checksum (bits)")
print(checksum_str)

print()
total_bits = "{:0160b}".format(int(data.hex(),16)) + checksum_str
print("Data with checksum (bits)")
print(total_bits)

delim = 11
bit_words = [total_bits[i:i+delim] for i in range(0, len(total_bits), delim)]

print()
print("bit words:")
for bit_word in bit_words:
    print(bit_word, int(bit_word, 2))


print()
print()
print("data: ", data.hex())
print("words:", words)
print("seed: ", seed.hex())
