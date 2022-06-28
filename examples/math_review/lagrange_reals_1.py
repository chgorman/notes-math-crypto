#!/usr/bin/env python3

from scipy.interpolate import lagrange
import numpy as np

x = [1, 4, 7]
y = [2, 1, 8]

# Plot Setup: Points and Data
poly = lagrange(x,y)
xNew = np.array(x)
yNew = np.polynomial.polynomial.Polynomial(poly.coef[::-1])(xNew)

print("Lagrange Interpolation over the Reals 1")
print("#"*72)
print()
print("Data")
print('{(%d,%d), (%d,%d), (%d,%d)}' % (x[0],y[0], x[1],y[1], x[2],y[2]))
print()
print("Lagrange Polynomial")
print('L(x) = (%f)*x**2 + (%f)*x + (%f)' % (poly.coef[0], poly.coef[1], poly.coef[2]))
print()
print("Lagrange Values")
for k in range(len(xNew)):
    print('L(%f) = %f' % (xNew[k], yNew[k]))

