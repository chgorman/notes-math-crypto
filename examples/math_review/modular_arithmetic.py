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

print("Modular Arithmetic Operations")
print("#"*72)
print()

a = 27
b = 241
n = 256

c = (a + b) % n
d = (a * b) % n

print('%4d + %4d == %4d mod %4d' % (a, b, c, n))
print('%4d * %4d == %4d mod %4d' % (a, b, d, n))

res_na = extended_gcd(a, n)
gcd_na = res_na[2]
assert gcd_na == 1
print()
print('gcd(%4d,%4d) = %4d' % (a, n, gcd_na))

res_nb = extended_gcd(b, n)
gcd_nb = res_nb[2]
assert gcd_nb == 1
print('gcd(%4d,%4d) = %4d' % (b, n, gcd_nb))

a_inv = mod_inverse(a, n)
b_inv = mod_inverse(b, n)

a_res = (a * a_inv) % n
assert a_res == 1
b_res = (b * b_inv) % n
assert b_res == 1

print()
print('%4d * %4d == %4d mod %4d' % (a, a_inv, a_res, n))
print('%4d * %4d == %4d mod %4d' % (b, b_inv, b_res, n))
