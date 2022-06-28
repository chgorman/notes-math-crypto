#!/usr/bin/env python3
import hashlib
num_bytes = 5
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

xPreStr = '00'*16; xPre = bytes.fromhex(xPreStr)
md5 = hashlib.md5(); md5.update(xPre)
x = int(md5.hexdigest(), 16) % q
y1 = pow(g1, x, p); y2 = pow(g2, x, p)

print("Knowledge:")
print("x   = %11d" % x)
print("y1  = g1**x mod p")
print("    = %11d" % y1)
print("y2  = g2**x mod p")
print("    = %11d" % y2)
print()

vPreStr = '11'*16; vPre = bytes.fromhex(vPreStr)
md5 = hashlib.md5(); md5.update(vPre)
v = int(md5.hexdigest(), 16) % q;
t1 = pow(g1, v, p); t2 = pow(g2, v, p)

print("Setup:")
print("v   = %11d" % v)
print("t1  = g1**v mod p")
print("    = %11d" % t1)
print("t2  = g2**v mod p")
print("    = %11d" % t2)
print()

t1_bytes = t1.to_bytes(num_bytes, 'big')
t2_bytes = t2.to_bytes(num_bytes, 'big')
g1_bytes = g1.to_bytes(num_bytes, 'big')
g2_bytes = g2.to_bytes(num_bytes, 'big')
y1_bytes = y1.to_bytes(num_bytes, 'big')
y2_bytes = y2.to_bytes(num_bytes, 'big')

md5 = hashlib.md5()
md5.update(g1_bytes); md5.update(y1_bytes); md5.update(g2_bytes);
md5.update(y2_bytes); md5.update(t1_bytes); md5.update(t2_bytes);
c = int(md5.hexdigest(), 16) % q
r = (v - c*x) % q

print("Challenge-Response:")
print("c   = md5(g1||y1||g2||y2||t1||t2) mod q")
print("    = %11d" % c)
print("r   = (v - c*x) mod q")
print("    = %11d" % r)
print()

t1Prime = (pow(g1, r, p) * pow(y1, c, p)) % p
t2Prime = (pow(g2, r, p) * pow(y2, c, p)) % p
t1Prime_bytes = t1Prime.to_bytes(num_bytes, 'big')
t2Prime_bytes = t2Prime.to_bytes(num_bytes, 'big')
md5 = hashlib.md5()
md5.update(g1_bytes);      md5.update(y1_bytes);
md5.update(g2_bytes);      md5.update(y2_bytes);
md5.update(t1Prime_bytes); md5.update(t2Prime_bytes)
cPrime = int(md5.hexdigest(), 16) % q

print("Zero-Knowledge Proof:")
print("t1' = g1**r * y1**c mod p")
print("    = %11d" % t1Prime)
print("t2' = g2**r * y2**c mod p")
print("    = %11d" % t2Prime)
print("c'  = md5(g1||y1||g2||y2||t1'||t2') mod q")
print("    = %11d" % cPrime)
print()

assert c == cPrime
print("Valid Zero-Knowledge Proof")
