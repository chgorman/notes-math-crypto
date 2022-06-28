#!/usr/bin/env python3

# Standard definitions
p = 7919
g = 7

# Alice and Bob definitions
a = 1347
A = pow(g, a, p)
b = 4862
B = pow(g, b, p)

k_alice = pow(B, a, p)
k_bob = pow(A, b, p)

print("Diffie-Hellman Key Exchange 2")
print("#"*72)
print()
print("Prime:      p = %4d" % p)
print("Base Point: g = %4d" % g)
print()

print("Alice")
print("a = %4d" % a)
print("A = %d**(%4d) mod %4d" % (g, a, p))
print("  = %4d" % A)
print()

print("Bob")
print("b = %4d" % b)
print("B = %d**(%4d) mod %4d" % (g, b, p))
print("  = %4d" % B)
print()

print("Alice computes:")
print("k = %4d**(%4d) mod %4d" % (B, a, p))
print("  = %4d" % k_alice)
print()

print("Bob computes:")
print("k = %4d**(%4d) mod %4d" % (A, b, p))
print("  = %4d" % k_bob)
print()


assert k_alice == k_bob
print("Computed shared secret")
