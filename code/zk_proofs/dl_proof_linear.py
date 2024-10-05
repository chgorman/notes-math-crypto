#!/usr/bin/env python3
import hashlib
def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()
num_b = 5
r = 12; q = 2**32 + 15; p = r*q + 1
h1 = 7; g1 = pow(h1, r, p) # g1: 13841287201
h2 = 6; g2 = pow(h2, r, p) # g2:  2176782336

x1ps = '00'*16; x1p = bytes.fromhex(x1ps); res = hash(x1p)
x1 = int(res.hex(), 16) % q                 # y1:  34063925739
x2ps = 'ff'*16; x2p = bytes.fromhex(x2ps); res = hash(x2p)
x2 = int(res.hex(), 16) % q                 # y2:   6808289188
y1 = pow(g1, x1, p); y2 = pow(g2, x2, p)    # a1: 521; a2: 523
a1 = 521; a2 = 523; b = (a1*x1 + a2*x2) % q # b:    4030483429
a2Inv = pow(a2, q-2, q); assert (a2Inv * a2) % q == 1

v1bps = '11'*16; v1bp = bytes.fromhex(v1bps); res = hash(v1bp)
v1b = int(res.hex(), 16) % q;  v1 = v1b
v2bps = '11'*16; v2bp = bytes.fromhex(v2bps); res = hash(v2bp)
v2b = int(res.hex(), 16) % q
alpha = (a1*v1b + a2*v2b) % q; v2 = (v2b - a2Inv*alpha) % q
assert (a1*v1 + a2*v2) % q == 0, "Invalid (v1,v2)"

t1 = pow(g1,v1,p); t2 = pow(g2,v2,p); b_b=b.to_bytes(num_b, 'big')
t1_b = t1.to_bytes(num_b, 'big'); t2_b = t2.to_bytes(num_b, 'big')
g1_b = g1.to_bytes(num_b, 'big'); g2_b = g2.to_bytes(num_b, 'big')
y1_b = y1.to_bytes(num_b, 'big'); y2_b = y2.to_bytes(num_b, 'big')
a1_b = a1.to_bytes(num_b, 'big'); a2_b = a2.to_bytes(num_b, 'big')

res = hash(g1_b+y1_b+g2_b+y2_b+a1_b+a2_b+b_b+t1_b+t2_b)
c  = int(res.hex(), 16) % q # c:  1236818951    # r1: 1952959998
r1 = (v1 - c*x1) % q; r2 = (v2 - c*x2) % q      # r2: 3581019185

t1p = (pow(g1, r1, p) * pow(y1, c, p)) % p
t2p = (pow(g2, r2, p) * pow(y2, c, p)) % p
t1p_b =t1p.to_bytes(num_b,'big'); t2p_b =t2p.to_bytes(num_b,'big')
res = hash(g1_b+y1_b+g2_b+y2_b+a1_b+a2_b+b_b+t1p_b+t2p_b)
cp = int(res.hex(), 16) % q
assert c == cp
assert ((a1*r1 + a2*r2) % q) == ((-c*b) % q) # Valid
