#!/usr/bin/env python3

from Crypto.Hash import keccak
keccak256 = keccak.new(digest_bits=256)

from eth_keys import keys

pk_str = '01' + '00'*30 + '01'
private_key_bytes = bytes.fromhex(pk_str)
private_key = keys.PrivateKey(private_key_bytes)
public_key_bytes = bytes.fromhex(str(private_key.public_key)[2:])
public_key_str = public_key_bytes.hex()

keccak256.update(public_key_bytes)
output = keccak256.digest()
addr = output[12:]

true_addr = str(private_key.public_key.to_address())[2:]

print("Computing Ethereum Address")
print("#"*72)
print()
print("Private Key")
print(private_key_bytes.hex())
print()
print("Public Key")
print(public_key_str[0:64])
print(public_key_str[64:])
print()
print("Ethereum Address")
print(addr.hex())
print()
print()

assert addr.hex() == true_addr
print("Valid Address")
