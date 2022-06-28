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

alice   = np.array([5853, 2695, 4447], dtype=int)
bob     = np.array([87,   1150, 7782], dtype=int)
charlie = np.array([6991, 3631, 5061], dtype=int)
dave    = np.array([5304, 2184, 2803], dtype=int)

master_secret_key = (alice[0] + bob[0] + charlie[0] + dave[0]) % q

print("Alice, Bob, Charlie, and Dave distribute a key")
print("#"*72)
print("master secret key = %4d" % master_secret_key)
print()
print()

print("Secrets and Shares")
print("#"*72)
print()

# Alice shares
print("Alice:")
print("secret_poly(x) = %4d + %4dx + %4dx^2" % (alice[0], alice[1], alice[2]))
print()
s1to1 = int(round(np.polynomial.Polynomial(alice).__call__(1))) % q
s1to2 = int(round(np.polynomial.Polynomial(alice).__call__(2))) % q
s1to3 = int(round(np.polynomial.Polynomial(alice).__call__(3))) % q
s1to4 = int(round(np.polynomial.Polynomial(alice).__call__(4))) % q
print("Alice->Alice   = %4d" % s1to1)
print("Alice->Bob     = %4d" % s1to2)
print("Alice->Charlie = %4d" % s1to3)
print("Alice->Dave    = %4d" % s1to4)
print()
print()

# Bob shares
print("Bob:")
print("secret_poly(x) = %4d + %4dx + %4dx^2" % (bob[0], bob[1], bob[2]))
s2to1 = int(round(np.polynomial.Polynomial(bob).__call__(1))) % q
s2to2 = int(round(np.polynomial.Polynomial(bob).__call__(2))) % q
s2to3 = int(round(np.polynomial.Polynomial(bob).__call__(3))) % q
s2to4 = int(round(np.polynomial.Polynomial(bob).__call__(4))) % q
print("Bob->Alice   = %4d" % s2to1)
print("Bob->Bob     = %4d" % s2to2)
print("Bob->Charlie = %4d" % s2to3)
print("Bob->Dave    = %4d" % s2to4)
print()
print()

# Charlie shares
print("Charlie:")
print("secret_poly(x) = %4d + %4dx + %4dx^2"%(charlie[0],charlie[1],charlie[2]))
s3to1 = int(round(np.polynomial.Polynomial(charlie).__call__(1))) % q
s3to2 = int(round(np.polynomial.Polynomial(charlie).__call__(2))) % q
s3to3 = int(round(np.polynomial.Polynomial(charlie).__call__(3))) % q
s3to4 = int(round(np.polynomial.Polynomial(charlie).__call__(4))) % q
print("Charlie->Alice   = %4d" % s3to1)
print("Charlie->Bob     = %4d" % s3to2)
print("Charlie->Charlie = %4d" % s3to3)
print("Charlie->Dave    = %4d" % s3to4)
print()
print()

# Dave shares
print("Dave:")
print("secret_poly(x) = %4d + %4dx + %4dx^2" % (dave[0], dave[1], dave[2]))
s4to1 = int(round(np.polynomial.Polynomial(dave).__call__(1))) % q
s4to2 = int(round(np.polynomial.Polynomial(dave).__call__(2))) % q
s4to3 = int(round(np.polynomial.Polynomial(dave).__call__(3))) % q
s4to4 = int(round(np.polynomial.Polynomial(dave).__call__(4))) % q
print("Dave->Alice   = %4d" % s4to1)
print("Dave->Bob     = %4d" % s4to2)
print("Dave->Charlie = %4d" % s4to3)
print("Dave->Dave    = %4d" % s4to4)
print()
print()

print("Group Secret Key")
print("#"*72)
print()

gsk1 = (s1to1 + s2to1 + s3to1 + s4to1) % q
print("Alice:")
print("gsk1 = %4d" % gsk1)
print()

gsk2 = (s1to2 + s2to2 + s3to2 + s4to2) % q
print("Bob:")
print("gsk2 = %4d" % gsk2)
print()

gsk3 = (s1to3 + s2to3 + s3to3 + s4to3) % q
print("Charlie:")
print("gsk3 = %4d" % gsk3)
print()

gsk4 = (s1to4 + s2to4 + s3to4 + s4to4) % q
print("Dave:")
print("gsk4 = %4d" % gsk4)
print()
print()

print("Deriving the Master Secret Key")
print("#"*72)
print()

# Proving msk derivation:
r11 = (8 * mod_inverse(3, q)) % q
r12 = (-2) % q
r14 = mod_inverse(3, q)

msk1 = (gsk1*r11 + gsk2*r12 + gsk4*r14) % q
assert msk1 == master_secret_key
print("Alice, Bob, and Dave:")
print()
print("gsk1 = %4d" % gsk1)
print("gsk2 = %4d" % gsk2)
print("gsk4 = %4d" % gsk4)
print("R1   = %4d" % r11)
print("R2   = %4d" % r12)
print("R4   = %4d" % r14)
print()
print("msk = gsk1*R1 + gsk2*R2 + gsk4*R4")
print("    = %4d" % msk1)
print()
print()

r21 = 2
r23 = (-2) % q
r24 = 1

msk2 = (gsk1*r21 + gsk3*r23 + gsk4*r24) % q
assert msk2 == master_secret_key
print("Alice, Charlie, and Dave:")
print()
print("gsk1 = %4d" % gsk1)
print("gsk3 = %4d" % gsk3)
print("gsk4 = %4d" % gsk4)
print("R1   = %4d" % r21)
print("R3   = %4d" % r23)
print("R4   = %4d" % r24)
print()
print("msk = gsk1*R1 + gsk3*R3 + gsk4*R4")
print("    = %4d" % msk2)





