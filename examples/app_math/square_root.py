#!/usr/bin/env python3

print("Computing the Square Roots by Exponentiation")
print("#"*72)
print()

values = range(1,20)

square_roots = []

p = 7919
assert p % 4 == 3
for k in values:
    leg = pow(k, (p-1)//2, p)
    res = pow(k, (p+1)//4, p)
    square_roots.append(res)
    if leg == 1:
        print("%4d^((p+1)/4) == %4d mod %4d" % (k, res, p))
    if leg == (-1) % p:
        print("%4d^((p+1)/4) == %4d mod %4d; %4d does not have a square root" % (k, res, p, k))

print()
print()

for k, sqrt in zip(values,square_roots):
    squared = pow(sqrt, 2, p)
    if squared == k:
        print("%4d^2 mod %4d == %4d" % (sqrt, p, k))
    else:
        print("%4d^2 mod %4d != %4d;   %4d^2 mod %4d == %4d" % (
            sqrt, p, k, sqrt, p, squared))
