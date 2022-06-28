#!/usr/bin/env python3

import numpy as np
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

q = 7919

secret_poly = np.array([1770, 6540, 2889], dtype=int)
master_secret = secret_poly[0]

# Setup
print("Shamir Secret Sharing 2:")
print("#"*72)
print("Alice, Bob, Charlie, and Dave share a secret")
print()
print("Secret Setup:")
print("q = %4d" % q)
print("secret_poly(x) = %4d + %4dx + %4dx^2" % (secret_poly[0],
    secret_poly[1], secret_poly[2]))
print()

alice_val   = int(round(np.polynomial.Polynomial(secret_poly).__call__(1))) % q
alice_idx   = 1
bob_val     = int(round(np.polynomial.Polynomial(secret_poly).__call__(2))) % q
bob_idx     = 2
charlie_val = int(round(np.polynomial.Polynomial(secret_poly).__call__(3))) % q
charlie_idx = 3
dave_val    = int(round(np.polynomial.Polynomial(secret_poly).__call__(4))) % q
dave_idx    = 4

print("Secrets:")
print("Alice:   (%4d,%4d)" % (alice_idx, alice_val))
print("Bob:     (%4d,%4d)" % (bob_idx, bob_val))
print("Charlie: (%4d,%4d)" % (charlie_idx, charlie_val))
print("Dave:    (%4d,%4d)" % (dave_idx, dave_val))
print()

print("Secret Recover:")
print()

s1 = alice_val
s2 = bob_val
s4 = dave_val
R1 = (8 * mod_inverse(3, q)) % q
R2 = (-2) % q
R4 = mod_inverse(3, q)
s  = (s1*R1 + s2*R2 + s4*R4) % q
assert s == master_secret

print("Alice, Bob, and Dave:")
print("s1 = %4d" % s1)
print("s2 = %4d" % s2)
print("s4 = %4d" % s4)
print("R1 = %4d" % R1)
print("R2 = %4d" % R2)
print("R4 = %4d" % R4)
print()
print("s = s1*R1 + s2*R2 + s4*R4 mod q")
print("  = %4d" % s)
print()


s1 = alice_val
s3 = charlie_val
s4 = dave_val
R1 = 2
R3 = (-2) % q
R4 = 1
s  = (s1*R1 + s3*R3 + s4*R4) % q
assert s == master_secret

print("Alice, Charlie, and Dave:")
print("s1 = %4d" % s1)
print("s3 = %4d" % s3)
print("s4 = %4d" % s4)
print("R1 = %4d" % R1)
print("R3 = %4d" % R3)
print("R4 = %4d" % R4)
print()
print("s = s1*R1 + s3*R3 + s4*R4 mod q")
print("  = %4d" % s)
