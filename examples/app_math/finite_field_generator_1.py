#!/usr/bin/env python3

p = 7919

print("Finite Field Generator")
print("#"*72)
print()
print("Prime p = %4d" % p)
print()
print()

p1 = 2
p2 = 37
p3 = 107

q1 = (p-1)//p1
q2 = (p-1)//p2
q3 = (p-1)//p3

print("Prime Factors of p-1:")
print("    p-1 = %4d" % (p-1))
print()
print("     p1 = %4d" % p1)
print("     p2 = %4d" % p2)
print("     p3 = %4d" % p3)
print()
print("g is generator of Fp* if")
print()
print("     g**qI mod p != 1")
print()
print("for all")
print()
print("     qI = (p-1)//pI")
print()
print("     q1 = %4d" % q1)
print("     q2 = %4d" % q2)
print("     q3 = %4d" % q3)
print()
print()

print("Loop through potential generators")
print("#"*72)
print()

for k in range(2,14):
    print("%4d" % k)
    is_generator = True
    for prime in [p1, p2, p3]:
        qPrime = (p-1)//prime
        computed_power = pow(k, qPrime, p)
        if computed_power == 1:
            is_generator = False
        print("%4d**(%4d) = %4d" % (k, qPrime, computed_power))
    if is_generator:
        print("%4d is a generator" % k)
    print()
