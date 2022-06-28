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

ab_list = ((3,5), (15,5), (15,3), (1872,1080))

print("Computing the Greatest Common Divisor and Bezout Coefficients")
print("#"*72)
print()

print("Greatest Common Divisor:")
for ab_val in ab_list:
    a = ab_val[0]
    b = ab_val[1]
    res = extended_gcd(a, b)
    s = res[0]
    t = res[1]
    g = res[2]
    assert a*s + b*t == g
    print('    gcd(%4d,%4d) = %4d' % (a, b, g))

print()
print("Bezout Coefficients")
for ab_val in ab_list:
    a = ab_val[0]
    b = ab_val[1]
    res = extended_gcd(a, b)
    s = res[0]
    t = res[1]
    g = res[2]
    assert a*s + b*t == g
    print('    (%4d)*(%4d) + (%4d)*(%4d) = %4d' % (a, s, b, t, g))
