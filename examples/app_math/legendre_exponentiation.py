#!/usr/bin/env python3

print("Computing the Legendre Symbols by Exponentiation")
print("#"*72)
print()

p = 7919
for k in range(1,20):
    res = pow(k, (p-1)//2, p)
    if res == 1:
        print("%4d^((p-1)/2) == % d mod %4d" % (k, res, p))
    else:
        print("%4d^((p-1)/2) == % d mod %4d" % (k, -1,  p))

print()
print()
print("Residues == 1; Nonresidues == -1")
