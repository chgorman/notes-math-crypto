#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

num_b = 5
r = 12; q = 2**32 + 15; p = r*q + 1
h1 = 7; g1 = pow(h1, r, p)
h2 = 6; g2 = pow(h2, r, p)

print("Knowledge of Discrete Logarithm Linear")
print("#"*72)
print()
print("Base Prime:  p  = %11d" % p)
print("Prime Order: q  = %11d" % q)
print("Base Point:  g1 = %11d" % g1)
print("Base Point:  g2 = %11d" % g2)
print()

x1ps = '00'*16; x1p = bytes.fromhex(x1ps)
res = hash(x1p)
x1 = int(res.hex(), 16) % q
x2ps = 'ff'*16; x2p = bytes.fromhex(x2ps)
res = hash(x2p)
x2 = int(res.hex(), 16) % q
y1 = pow(g1, x1, p); y2 = pow(g2, x2, p)
a1 = 521; a2 = 523; b = (a1*x1 + a2*x2) % q
a2Inv = pow(a2, q-2, q); assert (a2Inv * a2) % q == 1

print("Knowledge:")
print("x1  = %11d" % x1)
print("x2  = %11d" % x2)
print("y1  = g1**x mod p")
print("    = %11d" % y1)
print("y2  = g2**x mod p")
print("    = %11d" % y2)
print()
print("a1*x1 + a2*x2 == b mod q")
print()
print("a1  = %11d" % a1)
print("a2  = %11d" % a2)
print("b   = %11d" % b)
print()

v1bps = '11'*16; v1bp = bytes.fromhex(v1bps)
res = hash(v1bp)
v1b = int(res.hex(), 16) % q
v1 = v1b
v2bps = '11'*16; v2bp = bytes.fromhex(v2bps)
res = hash(v2bp)
v2b = int(res.hex(), 16) % q
alpha = (a1*v1b + a2*v2b) % q
v2 = (v2b - a2Inv*alpha) % q
assert (a1*v1 + a2*v2) % q == 0, "Invalid (v1,v2)"

t1 = pow(g1, v1, p); t2 = pow(g2, v2, p)

print("Setup:")
print("v1  = %11d" % v1)
print("v2  = %11d" % v2)
print("t1  = g1**v1 mod p")
print("    = %11d" % t1)
print("t2  = g2**v2 mod p")
print("    = %11d" % t2)
print()

t1_b = t1.to_bytes(num_b, 'big')
t2_b = t2.to_bytes(num_b, 'big')
g1_b = g1.to_bytes(num_b, 'big')
g2_b = g2.to_bytes(num_b, 'big')
y1_b = y1.to_bytes(num_b, 'big')
y2_b = y2.to_bytes(num_b, 'big')
a1_b = a1.to_bytes(num_b, 'big')
a2_b = a2.to_bytes(num_b, 'big')
b_b  = b.to_bytes(num_b, 'big')

res = hash(g1_b + y1_b + g2_b + y2_b + a1_b + a2_b + b_b + t1_b + t2_b)
c  = int(res.hex(), 16) % q
r1 = (v1 - c*x1) % q
r2 = (v2 - c*x2) % q

print("Challenge-Response:")
print("c   = md5(g1||y1||g2||y2||a1||a2||b||t1||t2) mod q")
print("    = %11d" % c)
print("r1  = (v1 - c*x1) mod q")
print("    = %11d" % r1)
print("r2  = (v2 - c*x2) mod q")
print("    = %11d" % r2)
print()

t1p = (pow(g1, r1, p) * pow(y1, c, p)) % p
t2p = (pow(g2, r2, p) * pow(y2, c, p)) % p
t1p_b = t1p.to_bytes(num_b, 'big')
t2p_b = t2p.to_bytes(num_b, 'big')
res = hash(g1_b + y1_b + g2_b + y2_b + a1_b + a2_b + b_b + t1p_b + t2p_b)
cp = int(res.hex(), 16) % q

print("Zero-Knowledge Proof:")
print("t1' = g1**r1 * y1**c mod p")
print("    = %11d" % t1p)
print("t2' = g2**r2 * y2**c mod p")
print("    = %11d" % t2p)
print("c'  = md5(g1||y1||g2||y2||a1||a2||b||t1'||t2') mod q")
print("    = %11d" % cp)
print()
print("a1*r1 + a2*r2 mod q = %11d" % ((a1*r1 + a2*r2) % q))
print("          -cb mod q = %11d" % ((-c*b) % q))
print()

assert c == cp
assert ((a1*r1 + a2*r2) % q) == ((-c*b) % q)
print("Valid Zero-Knowledge Proof")
