#!/usr/bin/env python3
import hashlib
num_bytes = 5
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

x1PreStr = '00'*16; x1Pre = bytes.fromhex(x1PreStr)
md5 = hashlib.md5(); md5.update(x1Pre)
x1 = int(md5.hexdigest(), 16) % q
x2PreStr = 'ff'*16; x2Pre = bytes.fromhex(x2PreStr)
md5 = hashlib.md5(); md5.update(x2Pre)
x2 = int(md5.hexdigest(), 16) % q
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

v1BarPreStr = '11'*16; v1BarPre = bytes.fromhex(v1BarPreStr)
md5 = hashlib.md5(); md5.update(v1BarPre)
v1Bar = int(md5.hexdigest(), 16) % q
v1 = v1Bar
v2BarPreStr = '11'*16; v2BarPre = bytes.fromhex(v2BarPreStr)
md5 = hashlib.md5(); md5.update(v2BarPre)
v2Bar = int(md5.hexdigest(), 16) % q
alpha = (a1*v1Bar + a2*v2Bar) % q
v2 = (v2Bar - a2Inv*alpha) % q
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

t1_bytes = t1.to_bytes(num_bytes, 'big')
t2_bytes = t2.to_bytes(num_bytes, 'big')
g1_bytes = g1.to_bytes(num_bytes, 'big')
g2_bytes = g2.to_bytes(num_bytes, 'big')
y1_bytes = y1.to_bytes(num_bytes, 'big')
y2_bytes = y2.to_bytes(num_bytes, 'big')
a1_bytes = a1.to_bytes(num_bytes, 'big')
a2_bytes = a2.to_bytes(num_bytes, 'big')
b_bytes  = b.to_bytes(num_bytes, 'big')

md5 = hashlib.md5()
md5.update(g1_bytes); md5.update(y1_bytes); md5.update(g2_bytes)
md5.update(y2_bytes); md5.update(a1_bytes); md5.update(a2_bytes)
md5.update(b_bytes);  md5.update(t1_bytes); md5.update(t2_bytes)
c  = int(md5.hexdigest(), 16) % q
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

t1Prime = (pow(g1, r1, p) * pow(y1, c, p)) % p
t2Prime = (pow(g2, r2, p) * pow(y2, c, p)) % p
t1Prime_bytes = t1Prime.to_bytes(num_bytes, 'big')
t2Prime_bytes = t2Prime.to_bytes(num_bytes, 'big')
md5 = hashlib.md5()
md5.update(g1_bytes); md5.update(y1_bytes); md5.update(g2_bytes)
md5.update(y2_bytes); md5.update(a1_bytes); md5.update(a2_bytes)
md5.update(b_bytes)
md5.update(t1Prime_bytes); md5.update(t2Prime_bytes)
cPrime = int(md5.hexdigest(), 16) % q

print("Zero-Knowledge Proof:")
print("t1' = g1**r1 * y1**c mod p")
print("    = %11d" % t1Prime)
print("t2' = g2**r2 * y2**c mod p")
print("    = %11d" % t2Prime)
print("c'  = md5(g1||y1||g2||y2||a1||a2||b||t1'||t2') mod q")
print("    = %11d" % cPrime)
print()
print("a1*r1 + a2*r2 mod q = %11d" % ((a1*r1 + a2*r2) % q))
print("          -cb mod q = %11d" % ((-c*b) % q))
print()

assert c == cPrime
assert ((a1*r1 + a2*r2) % q) == ((-c*b) % q)
print("Valid Zero-Knowledge Proof")
