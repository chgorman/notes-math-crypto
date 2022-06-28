#!/usr/bin/env python3

import hashlib
from copy import deepcopy

########################################################################
# Functions
def extended_gcd(a, b):
    old_r = deepcopy(a)
    r = deepcopy(b)

    old_s = 1
    s = 0

    old_t = 0
    t = 1

    while (r != 0):
        q = old_r // r

        #(old_r, r) := (r, old_r − quotient × r)
        prov = r
        r = old_r - q*prov
        old_r = prov

        #(old_s, s) := (s, old_s − quotient × s)
        prov = s
        s = old_s - q*prov
        old_s = prov

        #(old_t, t) := (t, old_t − quotient × t)
        prov = t
        t = old_t - q*prov
        old_t = prov

    return (old_s, old_t, old_r)

def mod_inverse(a, m):
    res = extended_gcd(a, m)
    s = res[0]
    t = res[1]
    g = res[2]
    if (g != 1):
        raise Exception('modular inverse does not exist')
    else:
        res = s % m
        assert a * res % m == 1
        return res
########################################################################

num_bytes = 5
R = 12; q = 2**32 + 15; p = R*q + 1
h = 7;  g = pow(h, R, p)
# g: 13841287201

print("DSA Signature Generation")
print("#"*72)
print()
print("Base Prime:  p = %11d" % p)
print("Prime Order: q = %11d" % q)
print("Base Point:  g = %11d" % g)
print()

x = 3713319676
y = pow(g, x, p)

m = bytes.fromhex('00010203')

print("Alice")
print("x = %11d" % x)
print("y = %11d**(%11d) mod %4d" % (g, x, p))
print("  = %11d" % y)
print("m = %s (hex)" % m.hex())
print()

k = 2073840447
r = pow(g, k, p) % q

k_inv = mod_inverse(k, q)

md5 = hashlib.md5(); md5.update(m); HashM_bytes = md5.digest()
HashM = int(HashM_bytes.hex(), 16) % q
s = (k_inv*(HashM + x*r)) % q

print("Alice computes")
print("k     = %11d" % k)
print("r     = [%11d**(%11d) mod %11d] mod %11d" % (g, k, p, q))
print("      = %11d" % r)
print("k_inv = %11d" % k_inv)
print("H(m)  = md5(%s) mod %11d" % (m.hex(), q))
print("      = %11d (int)" % HashM)
print("s = (%11d)*[%11d + (%11d)*(%11d)] mod %11d" % (k_inv, HashM, x, r, q))
print("  =  %11d" % s)
print()
print("Alice sends (%11d,%11d) to Bob" % (r,s))
print()

w  = mod_inverse(s, q)
u1 = (HashM * w) % q
u2 = (r * w) % q
v  = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

print("Bob computes")
print("w  =  (%11d)^(-1) mod %11d" % (s, q))
print("   =   %11d" % w)
print("u1 =  (%11d)*(%11d) mod %11d" % (HashM, w, q))
print("   =   %11d" % u1)
print("u2 =  (%11d)*(%11d) mod %11d" % (r, w, q))
print("   =   %11d" % u2)
print("v  =  (g**u1 * y**u2 mod p) mod q")
print("   =   %11d" % v)
print()

assert r == v
print("Valid DSA signature")
