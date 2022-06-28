#!/usr/bin/env python3

p = 73

x = [1, 4, 7]
y = [2, 1, 8]

# Plot Setup: Points and Data

c2 = 41
c1 = 38
c0 = 69

def poly(x: int):
    return (c2*x**2 + c1*x + c0) % p

print("Lagrange Interpolation over the Finite Field 1")
print("#"*72)
print()
print("Data")
print('{(%d,%d), (%d,%d), (%d,%d)}' % (x[0],y[0], x[1],y[1], x[2],y[2]))
print()
print("Lagrange Polynomial")
print('L(x) = %2d*x**2 + %2d*x + %2d' % (c2, c1, c0))
print()
print("Lagrange Values")
for k in range(len(x)):
    print('L(%2d) = %2d' % (x[k], poly(x[k])))

