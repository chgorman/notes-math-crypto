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

# Signing definitions
x = 5654
y = pow(g, x, p)
k = 3331
HashM = 2689

res = extended_gcd(k, p-1)
gcd_value = res[2]
assert gcd_value == 1

k_inv = mod_inverse(k, p-1)

r = pow(g, k, p)
s = (k_inv*(HashM - x*r)) % (p-1)

print("Elgamal Signature Generation")
print("#"*72)
print()
print("Prime:      p = %4d" % p)
print("Base Point: g = %4d" % g)
print()

print("Alice")
print("x = %4d" % x)
print("y = %4d**(%4d) mod %4d" % (g, x, p))
print("  = %4d" % y)
print("k = %4d" % k)
print()
print("gcd(%4d,%4d) == %4d" % (k, p-1, gcd_value))
print()

print("Alice computes")
print("r     = %4d**(%4d) mod %4d" % (g, k, p))
print("      = %4d" % r)
print("H(m)  = %4d" % HashM)
print("k_inv = %4d" % k_inv)
print("s     = [%4d - (%4d)*(%4d)]*(%4d) mod %4d" % (HashM, x, r, k_inv, p))
print("      = %4d" % s)
print()
print("Alice sends (%4d,%4d) to Bob along with message m" % (r, s))
print()

lhs = pow(g, HashM, p)
rhs1 = pow(y, r, p)
rhs2 = pow(r, s, p)
rhs = rhs1*rhs2 % p

print("Bob computes")
print("H(m) = %4d" % HashM)
print("lhs  = %4d**(%4d) mod %4d" % (g, HashM, p))
print("     = %4d" % lhs)
print("rhs  = (%4d)**(%4d) * (%4d)**(%4d) mod %4d" % (y, r, r, s, p))
print("     = %4d" % rhs)
print()

assert lhs == rhs
print("Valid Elgamal signature")
