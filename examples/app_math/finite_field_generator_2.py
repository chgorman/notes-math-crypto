#!/usr/bin/env python3

q = 2**32 + 15
r = 12
p = r*q + 1

print("Finite Field Generator")
print("#"*72)
print()
print("Prime p = r*q + 1")
print("        = %11d" % p)
print("      r = %11d" % r)
print("      q = %11d" % q)
print()
print()

p1 = 2
p2 = 3
p3 = 2**32 + 15

q1 = (p-1)//p1
q2 = (p-1)//p2
q3 = (p-1)//p3

print("Prime Factors of p-1:")
print("    p-1 = %11d" % (p-1))
print()
print("     p1 = %11d" % p1)
print("     p2 = %11d" % p2)
print("     p3 = %11d" % p3)
print()
print("g is generator of Fp* if")
print()
print("     g**qI mod p != 1")
print()
print("for all")
print()
print("     qI = (p-1)//pI")
print()
print("     q1 = %11d" % q1)
print("     q2 = %11d" % q2)
print("     q3 = %11d" % q3)
print()
print()

print("Loop through potential generators")
print("#"*72)
print()

for k in range(2,8):
    print("%4d" % k)
    is_generator = True
    for prime in [p1, p2, p3]:
        qPrime = (p-1)//prime
        computed_power = pow(k, qPrime, p)
        if computed_power == 1:
            is_generator = False
        print("%4d**(%11d) = %11d" % (k, qPrime, computed_power))
    if is_generator:
        print("%4d is a generator" % k)
    print()
