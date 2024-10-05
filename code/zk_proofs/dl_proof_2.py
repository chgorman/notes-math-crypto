#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

num_b = 5
r = 12; q = 2**32 + 15; p = r*q + 1
h1 = 7; g1 = pow(h1, r, p) # g1: 13841287201
h2 = 6; g2 = pow(h2, r, p) # g2:  2176782336

x_pre_str = '00'*16; x_pre = bytes.fromhex(x_pre_str)
res = hash(x_pre)
x = int(res.hex(), 16) % q
y1 = pow(g1, x, p); y2 = pow(g2, x, p)
# y1: 34063925739; y2: 42077908773

v_pre_str = '11'*16; v_pre = bytes.fromhex(v_pre_str)
res = hash(v_pre)
v = int(res.hex(), 16) % q;
t1 = pow(g1, v, p); t2 = pow(g2, v, p)

t1_b = t1.to_bytes(num_b, 'big'); t2_b = t2.to_bytes(num_b, 'big')
g1_b = g1.to_bytes(num_b, 'big'); g2_b = g2.to_bytes(num_b, 'big')
y1_b = y1.to_bytes(num_b, 'big'); y2_b = y2.to_bytes(num_b, 'big')

res = hash(g1_b + y1_b + g2_b + y2_b + t1_b + t2_b)
c = int(res.hex(), 16) % q # c:  820804763
r = (v - c*x) % q          # r: 1837574845

t1p = (pow(g1, r, p) * pow(y1, c, p)) % p
t2p = (pow(g2, r, p) * pow(y2, c, p)) % p
t1p_b = t1p.to_bytes(num_b, 'big')
t2p_b = t2p.to_bytes(num_b, 'big')
res = hash(g1_b + y1_b + g2_b + y2_b + t1p_b + t2p_b)
cp = int(res.hex(), 16) % q
assert c == cp # Valid
