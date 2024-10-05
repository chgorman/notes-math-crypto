#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

num_b = 5
r = 12; q = 2**32 + 15; p = r*q + 1
h1 = 7; g1 = pow(h1, r, p)
h2 = 6; g2 = pow(h2, r, p)

print("Knowledge of Discrete Logarithm 2")
print("#"*72)
print()
print("Base Prime:  p  = %11d" % p)
print("Prime Order: q  = %11d" % q)
print("Base Point:  g1 = %11d" % g1)
print("Base Point:  g2 = %11d" % g2)
print()

x_pre_str = '00'*16; x_pre = bytes.fromhex(x_pre_str)
res = hash(x_pre)
x = int(res.hex(), 16) % q
y1 = pow(g1, x, p); y2 = pow(g2, x, p)

print("Knowledge:")
print("x   = %11d" % x)
print("y1  = g1**x mod p")
print("    = %11d" % y1)
print("y2  = g2**x mod p")
print("    = %11d" % y2)
print()

v_pre_str = '11'*16; v_pre = bytes.fromhex(v_pre_str)
res = hash(v_pre)
v = int(res.hex(), 16) % q;
t1 = pow(g1, v, p); t2 = pow(g2, v, p)

print("Setup:")
print("v   = %11d" % v)
print("t1  = g1**v mod p")
print("    = %11d" % t1)
print("t2  = g2**v mod p")
print("    = %11d" % t2)
print()

t1_b = t1.to_bytes(num_b, 'big')
t2_b = t2.to_bytes(num_b, 'big')
g1_b = g1.to_bytes(num_b, 'big')
g2_b = g2.to_bytes(num_b, 'big')
y1_b = y1.to_bytes(num_b, 'big')
y2_b = y2.to_bytes(num_b, 'big')

res = hash(g1_b + y1_b + g2_b + y2_b + t1_b + t2_b)
c = int(res.hex(), 16) % q
r = (v - c*x) % q

print("Challenge-Response:")
print("c   = md5(g1||y1||g2||y2||t1||t2) mod q")
print("    = %11d" % c)
print("r   = (v - c*x) mod q")
print("    = %11d" % r)
print()

t1p = (pow(g1, r, p) * pow(y1, c, p)) % p
t2p = (pow(g2, r, p) * pow(y2, c, p)) % p
t1p_b = t1p.to_bytes(num_b, 'big')
t2p_b = t2p.to_bytes(num_b, 'big')
res = hash(g1_b + y1_b + g2_b + y2_b + t1p_b + t2p_b)
cp = int(res.hex(), 16) % q

print("Zero-Knowledge Proof:")
print("t1' = g1**r * y1**c mod p")
print("    = %11d" % t1p)
print("t2' = g2**r * y2**c mod p")
print("    = %11d" % t2p)
print("c'  = md5(g1||y1||g2||y2||t1'||t2') mod q")
print("    = %11d" % cp)
print()

assert c == cp
print("Valid Zero-Knowledge Proof")
