#!/usr/bin/env python3
import hashlib
num_bytes = 5
r = 12; q = 2**32 + 15; p = r*q + 1
h = 7;  g = pow(h, r, p)
# g: 13841287201

xPreStr = '00'*16; xPre = bytes.fromhex(xPreStr)
md5 = hashlib.md5(); md5.update(xPre)
x = int(md5.hexdigest(), 16) % q
y = pow(g, x, p)
# y: 34063925739

vPreStr = '11'*16; vPre = bytes.fromhex(vPreStr)
md5 = hashlib.md5(); md5.update(vPre)
v = int(md5.hexdigest(), 16) % q
t = pow(g, v, p)

t_bytes = t.to_bytes(num_bytes, 'big')
g_bytes = g.to_bytes(num_bytes, 'big')
y_bytes = y.to_bytes(num_bytes, 'big')

md5 = hashlib.md5()
md5.update(g_bytes); md5.update(y_bytes); md5.update(t_bytes)
c = int(md5.hexdigest(), 16) % q # c: 2451489814
r = (v - c*x) % q                # r: 3624355949

tPrime = (pow(g, r, p) * pow(y, c, p)) % p
tPrime_bytes = tPrime.to_bytes(num_bytes, 'big')
md5 = hashlib.md5()
md5.update(g_bytes); md5.update(y_bytes); md5.update(tPrime_bytes)
cPrime = int(md5.hexdigest(), 16) % q
assert c == cPrime # Valid
