#!/usr/bin/env python3
import hashlib
num_bytes = 5
r = 12; q = 2**32 + 15; p = r*q + 1
h1 = 7; g1 = pow(h1, r, p) # g1: 13841287201
h2 = 6; g2 = pow(h2, r, p) # g2:  2176782336

xPreStr = '00'*16; xPre = bytes.fromhex(xPreStr)
md5 = hashlib.md5(); md5.update(xPre)
x = int(md5.hexdigest(), 16) % q
y1 = pow(g1, x, p); y2 = pow(g2, x, p)
# y1: 34063925739; y2: 42077908773

vPreStr = '11'*16; vPre = bytes.fromhex(vPreStr)
md5 = hashlib.md5(); md5.update(vPre)
v = int(md5.hexdigest(), 16) % q;
t1 = pow(g1, v, p); t2 = pow(g2, v, p)

t1_bytes = t1.to_bytes(num_bytes, 'big')
t2_bytes = t2.to_bytes(num_bytes, 'big')
g1_bytes = g1.to_bytes(num_bytes, 'big')
g2_bytes = g2.to_bytes(num_bytes, 'big')
y1_bytes = y1.to_bytes(num_bytes, 'big')
y2_bytes = y2.to_bytes(num_bytes, 'big')

md5 = hashlib.md5()
md5.update(g1_bytes); md5.update(y1_bytes); md5.update(g2_bytes)
md5.update(y2_bytes); md5.update(t1_bytes); md5.update(t2_bytes)
c = int(md5.hexdigest(), 16) % q # c:  820804763
r = (v - c*x) % q                # r: 1837574845

t1Prime = (pow(g1, r, p) * pow(y1, c, p)) % p
t2Prime = (pow(g2, r, p) * pow(y2, c, p)) % p
t1Prime_bytes = t1Prime.to_bytes(num_bytes, 'big')
t2Prime_bytes = t2Prime.to_bytes(num_bytes, 'big')
md5 = hashlib.md5()
md5.update(g1_bytes);      md5.update(y1_bytes)
md5.update(g2_bytes);      md5.update(y2_bytes)
md5.update(t1Prime_bytes); md5.update(t2Prime_bytes)
cPrime = int(md5.hexdigest(), 16) % q
assert c == cPrime # Valid
