#!/usr/bin/env python3

from copy import deepcopy

########################################################################
# Functions
def euclidean_division(a: int, b: int):
    q = a//b
    r = a - q*b
    return (q, r)
########################################################################

print("Extended Euclidean Algorithm")
print("#"*72)
print()

a = 1080
b = 1872
print("Compute")
print("    %4dx + %4dy = gcd(%4d,%4d)" % (a, b, a, b))
print()

if a > b:
    rkm1 = deepcopy(a)
    rk = deepcopy(b)
else:
    rkm1 = deepcopy(b)
    rk = deepcopy(a)
rkp1 = 1

skm1 = 1
sk   = 0
skp1 = 0
tkm1 = 0
tk   = 1
tkp1 = 0

print("r0   = %4d" % rkm1)
print("s0   = %4d" % skm1)
print("t0   = %4d" % tkm1)
print("r1   = %4d" % rk)
print("s1   = %4d" % sk)
print("t1   = %4d" % tk)
print()

k = 1
while rkp1 != 0:
    res = euclidean_division(rkm1, rk)
    qk   = res[0]
    rkp1 = res[1]
    skp1 = skm1 - qk*sk
    tkp1 = tkm1 - qk*tk
    print("%4d = %4d*%4d + %4d" % (rkm1, qk, rk, rkp1))
    print("q%d   = %4d" % (k,   qk))
    print("r%d   = %4d" % (k+1, rkp1))
    print("s%d   = %4d" % (k+1, skp1))
    print("t%d   = %4d" % (k+1, tkp1))
    print()
    if rkp1 == 0:
        g = rk
        x = sk
        y = tk
        break
    rkm1 = deepcopy(rk)
    rk   = deepcopy(rkp1)
    skm1 = deepcopy(sk)
    sk   = deepcopy(skp1)
    tkm1 = deepcopy(tk)
    tk   = deepcopy(tkp1)
    k += 1
print()
if b >= a:
    x, y = y, x
assert a*x + b*y == g
print("    (%4d)*(%4d) + (%4d)*(%4d) = %4d" % (a, x, b, y, g))
