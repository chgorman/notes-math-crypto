#!/usr/bin/env python3

from copy import deepcopy

########################################################################
# Functions
def euclidean_division(a: int, b: int):
    q = a//b
    r = a - q*b
    return (q, r)
########################################################################

print("Euclidean Algorithm")
print("#"*72)
print()

a = 1080
b = 1872
print("Compute gcd(%4d,%4d)" % (a, b))
print()

if a > b:
    rkm1 = deepcopy(a)
    rk = deepcopy(b)
else:
    rkm1 = deepcopy(b)
    rk = deepcopy(a)
rkp1 = 1

print("r0   = %4d" % rkm1)
print("r1   = %4d" % rk)
print()

k = 1
while rkp1 != 0:
    res = euclidean_division(rkm1, rk)
    qk   = res[0]
    rkp1 = res[1]
    print("%4d = %4d*%4d + %4d" % (rkm1, qk, rk, rkp1))
    print("q%d   = %4d" % (k,   qk))
    print("r%d   = %4d" % (k+1, rkp1))
    print()
    if rkp1 == 0:
        g = rk
        break
    rkm1 = deepcopy(rk)
    rk   = deepcopy(rkp1)
    k += 1
print("gcd(%4d,%4d) = %4d" % (a, b, g))
