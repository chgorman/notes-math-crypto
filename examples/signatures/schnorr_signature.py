#!/usr/bin/env python3
import hashlib
num_bytes = 5
R = 12; q = 2**32 + 15; p = R*q + 1
h = 7;  g = pow(h, R, p)
# g: 13841287201

print("Schnorr Signature Generation")
print("#"*72)
print()
print("Base Prime:  p = %11d" % p)
print("Prime Order: q = %11d" % q)
print("Base Point:  g = %11d" % g)
print()


x = 2981464014
y = pow(g, x, p)

m = bytes.fromhex('00010203')

print("Alice")
print("x = %11d" % x)
print("y = %11d**(%11d) mod %11d" % (g, x, p))
print("  = %11d" % y)
print("m = %s (hex)" % m.hex())
print()

k = 458074281
r = pow(g, k, p)
r_bytes = r.to_bytes(num_bytes, 'big')

md5 = hashlib.md5(); md5.update(r_bytes); md5.update(m)
e_bytes = md5.digest()
e = int(e_bytes.hex(), 16) % q
s = (k - x*e) % q

print("Alice computes")
print("k = %11d" % k)
print("r = %11d**(%11d) mod %11d" % (g, k, p))
print("  = %11d" % r)
print("e = md5(%s||%s) (hex)" % (r_bytes.hex(), m.hex()))
print("  = %s (hex)" % e_bytes.hex())
print("  = %11d (int)" % e)
print("s = [%11d - (%11d)*(%11d)] mod %11d" % (k, x, e, p))
print("  =  %11d" % s)
print()
print("Alice sends (%11d,%11d) to Bob" % (s,e))
print()

rv = (pow(g, s, p) * pow(y, e, p)) % p
rv_bytes = r.to_bytes(num_bytes, 'big')
md5 = hashlib.md5(); md5.update(rv_bytes); md5.update(m)
ev_bytes = md5.digest()
ev = int(ev_bytes.hex(), 16) % q

print("Bob computes")
print("rv = (%11d)**(%11d) * (%11d)**(%11d) mod %11d" % (g, s, y, e, p))
print("   =  %11d" % rv)
print("ev = md5(%s||%s) (hex)" % (rv_bytes.hex(), m.hex()))
print("   = %s (hex)" % ev_bytes.hex())
print("   = %11d (int)" % ev)
print()

assert e == ev
print("Valid Schnorr signature")
