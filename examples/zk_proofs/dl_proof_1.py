#!/usr/bin/env python3

import hashlib
num_bytes = 5
r = 12; q = 2**32 + 15; p = r*q + 1
h = 7;  g = pow(h, r, p)

print("Knowledge of Discrete Logarithm 1")
print("#"*72)
print()
print("Base Prime:  p = %11d" % p)
print("Prime Order: q = %11d" % q)
print("Base Point:  g = %11d" % g)
print()


xPreStr = '00'*16; xPre = bytes.fromhex(xPreStr)
md5 = hashlib.md5(); md5.update(xPre)
x = int(md5.hexdigest(), 16) % q
y = pow(g, x, p)
print("Knowledge:")
print("x  = %11d" % x)
print("y  = g**x mod p")
print("   = %11d" % y)
print()

vPreStr = '11'*16; vPre = bytes.fromhex(vPreStr)
md5 = hashlib.md5(); md5.update(vPre)
v = int(md5.hexdigest(), 16) % q
t = pow(g, v, p)
print("Setup:")
print("v  = %11d" % v)
print("t  = g**v mod p")
print("   = %11d" % t)
print()

t_bytes = t.to_bytes(num_bytes, 'big')
g_bytes = g.to_bytes(num_bytes, 'big')
y_bytes = y.to_bytes(num_bytes, 'big')

md5 = hashlib.md5()
md5.update(g_bytes); md5.update(y_bytes); md5.update(t_bytes);
c = int(md5.hexdigest(), 16) % q
r = (v - c*x) % q
print("Challenge-Response:")
print("c  = md5(g||y||t) mod q")
print("   = %11d" % c)
print("r  = (v - c*x) mod q")
print("   = %11d" % r)
print()

tPrime = (pow(g, r, p) * pow(y, c, p)) % p
tPrime_bytes = tPrime.to_bytes(num_bytes, 'big')
md5 = hashlib.md5()
md5.update(g_bytes); md5.update(y_bytes); md5.update(tPrime_bytes);
cPrime = int(md5.hexdigest(), 16) % q
print("Zero-Knowledge Proof:")
print("t' = g**r * y**c mod p")
print("   = %11d" % tPrime)
print("c' = md5(g||y||t') mod q")
print("   = %11d" % cPrime)
print()

assert c == cPrime
print("Valid Zero-Knowledge Proof")
