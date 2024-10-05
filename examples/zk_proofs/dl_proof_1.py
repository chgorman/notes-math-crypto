#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

num_b = 5
r = 12; q = 2**32 + 15; p = r*q + 1
h = 7;  g = pow(h, r, p)

print("Knowledge of Discrete Logarithm 1")
print("#"*72)
print()
print("Base Prime:  p = %11d" % p)
print("Prime Order: q = %11d" % q)
print("Base Point:  g = %11d" % g)
print()

x_pre_str = '00'*16; x_pre = bytes.fromhex(x_pre_str)
res = hash(x_pre)
x = int(res.hex(), 16) % q
y = pow(g, x, p)
print("Knowledge:")
print("x  = %11d" % x)
print("y  = g**x mod p")
print("   = %11d" % y)
print()

v_pre_str = '11'*16; v_pre = bytes.fromhex(v_pre_str)
res = hash(v_pre)
v = int(res.hex(), 16) % q
t = pow(g, v, p)
print("Setup:")
print("v  = %11d" % v)
print("t  = g**v mod p")
print("   = %11d" % t)
print()

t_b = t.to_bytes(num_b, 'big')
g_b = g.to_bytes(num_b, 'big')
y_b = y.to_bytes(num_b, 'big')

res = hash(g_b + y_b + t_b)
c = int(res.hex(), 16) % q
r = (v - c*x) % q
print("Challenge-Response:")
print("c  = md5(g||y||t) mod q")
print("   = %11d" % c)
print("r  = (v - c*x) mod q")
print("   = %11d" % r)
print()

tp = (pow(g, r, p) * pow(y, c, p)) % p
tp_b = tp.to_bytes(num_b, 'big')
res = hash(g_b + y_b + tp_b)
cp = int(res.hex(), 16) % q
print("Zero-Knowledge Proof:")
print("t' = g**r * y**c mod p")
print("   = %11d" % tp)
print("c' = md5(g||y||t') mod q")
print("   = %11d" % cp)
print()

assert c == cp
print("Valid Zero-Knowledge Proof")
