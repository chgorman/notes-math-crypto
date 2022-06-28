#!/usr/bin/env python3

p = 73

x = [1, 4, 5, 7]
y = [2, 1, 1, 8]

# Plot Setup: Points and Data

c3 = 60
c2 = 51
c1 = 42
c0 = 68

def poly(x: int):
    return (c3*x**3 + c2*x**2 + c1*x + c0) % p

print("Lagrange Interpolation over the Finite Field 2")
print("#"*72)
print()
print("Data")
print('{(%d,%d), (%d,%d), (%d,%d), (%d,%d)}' % (x[0],y[0], x[1],y[1], x[2],y[2], x[3],y[3]))
print()
print("Lagrange Polynomial")
print('L(x) = %2d*x**3 + %2d*x**2 + %2d*x + %2d' % (c3, c2, c1, c0))
print()
print("Lagrange Values")
for k in range(len(x)):
    print('L(%2d) = %2d' % (x[k], poly(x[k])))

