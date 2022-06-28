#!/usr/bin/env python3

print("Computing the Legendre Symbols by Squaring")
print("#"*72)
print()

p = 13
for k in range(1,p):
    print("%2d^2 == %2d mod %2d" % (k, pow(k, 2, p), p))

print()
print()
print("Every number on the righthand side is a residue;")
print("the numbers not present are nonresidues.")
