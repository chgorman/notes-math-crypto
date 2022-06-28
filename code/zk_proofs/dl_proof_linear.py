#!/usr/bin/env python3
import hashlib
num_bytes = 5
r = 12; q = 2**32 + 15; p = r*q + 1
h1 = 7; g1 = pow(h1, r, p) # g1: 13841287201
h2 = 6; g2 = pow(h2, r, p) # g2:  2176782336

x1PreStr = '00'*16; x1Pre = bytes.fromhex(x1PreStr)
md5 = hashlib.md5(); md5.update(x1Pre)
x1 = int(md5.hexdigest(), 16) % q
x2PreStr = 'ff'*16; x2Pre = bytes.fromhex(x2PreStr)
md5 = hashlib.md5(); md5.update(x2Pre)      # y1:  34063925739
x2 = int(md5.hexdigest(), 16) % q           # y2:   6808289188
y1 = pow(g1, x1, p); y2 = pow(g2, x2, p)    # a1: 521; a2: 523
a1 = 521; a2 = 523; b = (a1*x1 + a2*x2) % q # b:    4030483429
a2Inv = pow(a2, q-2, q); assert (a2Inv * a2) % q == 1

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
c  = int(md5.hexdigest(), 16) % q # c:  1236818951
r1 = (v1 - c*x1) % q              # r1: 1952959998
r2 = (v2 - c*x2) % q              # r2: 3581019185

t1Prime = (pow(g1, r1, p) * pow(y1, c, p)) % p
t2Prime = (pow(g2, r2, p) * pow(y2, c, p)) % p
t1Prime_bytes = t1Prime.to_bytes(num_bytes, 'big')
t2Prime_bytes = t2Prime.to_bytes(num_bytes, 'big')
md5 = hashlib.md5()
md5.update(g1_bytes); md5.update(y1_bytes); md5.update(g2_bytes)
md5.update(y2_bytes); md5.update(a1_bytes); md5.update(a2_bytes)
md5.update(b_bytes);
md5.update(t1Prime_bytes); md5.update(t2Prime_bytes)
cPrime = int(md5.hexdigest(), 16) % q
assert c == cPrime
assert ((a1*r1 + a2*r2) % q) == ((-c*b) % q) # Valid
