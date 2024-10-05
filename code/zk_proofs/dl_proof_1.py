#!/usr/bin/env python3

import hashlib

def hash(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

num_b = 5
r = 12; q = 2**32 + 15; p = r*q + 1
h = 7;  g = pow(h, r, p)
# g: 13841287201

x_pre_str = '00'*16; x_pre = bytes.fromhex(x_pre_str)
res = hash(x_pre)
x = int(res.hex(), 16) % q
y = pow(g, x, p)
# y: 34063925739

v_pre_str = '11'*16; v_pre = bytes.fromhex(v_pre_str)
res = hash(v_pre)
v = int(res.hex(), 16) % q
t = pow(g, v, p)

t_b = t.to_bytes(num_b, 'big')
g_b = g.to_bytes(num_b, 'big')
y_b = y.to_bytes(num_b, 'big')

res = hash(g_b + y_b + t_b)
c = int(res.hex(), 16) % q # c: 2451489814
r = (v - c*x) % q          # r: 3624355949

tp = (pow(g, r, p) * pow(y, c, p)) % p
tp_b = tp.to_bytes(num_b, 'big')
res = hash(g_b + y_b + tp_b)
cp = int(res.hex(), 16) % q
assert c == cp # Valid
