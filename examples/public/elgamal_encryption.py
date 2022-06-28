#!/usr/bin/env python3

from copy import deepcopy

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

# Standard definitions
p = 7919
g = 7

# Alice and Bob definitions
m = 1234
y = 3185
b = 3119
B = pow(g, b, p)

c1 = pow(g, y, p)
s  = pow(B, y, p)
c2 = (m * s) % p

s_inv = mod_inverse(s, p)
m_bob = (c2 * s_inv) % p

print("Elgamal Encryption")
print("#"*72)
print()
print("Prime:      p = %4d" % p)
print("Base Point: g = %4d" % g)
print()

print("Alice")
print("m = %4d" % m)
print("y = %4d" % y)
print()

print("Bob")
print("b = %4d" % b)
print("B = %d**(%4d) mod %4d" % (g, b, p))
print("  = %4d" % B)
print()

print("Alice computes:")
print("c1 = %4d**(%4d) mod %4d" % (g, y, p))
print("   = %4d" % c1)
print("s  = %4d**(%4d) mod %4d" % (B, y, p))
print("   = %4d" % s)
print("c2 = %4d*%4d mod %4d" % (m, s, p))
print("   = %4d" % c2)
print()
print("Alice sends (%4d,%4d) to Bob" % (c1, c2))
print()

print("Bob computes:")
print("s     = %4d**(%4d) mod %4d" % (c1, b, p))
print("      = %4d" % s)
print("s_inv = %4d" % s_inv)
print("m     = %4d*%4d mod %4d" % (c2, s_inv, p))
print("      = %4d" % m_bob)
print()

assert m == m_bob
print("Valid Elgamal encryption")
