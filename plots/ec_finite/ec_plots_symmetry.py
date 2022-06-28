#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Create a simple Point class to represent the affine points.
from collections import namedtuple
Point = namedtuple("Point", "x y")

# The point at infinity (origin for the group law).
O = Point(0,0)

# Finite field: F_71
p = 71 # p == 3 mod 4
a = 2
b = 1

# Confirm valid point
def valid(P):
    if P == O:
        return True
    else:
        return (P.y**2 - (P.x**3 + a*P.x + b)) % p == 0 and (0 <= P.x < p) and (0 <= P.y < p)

# Check if origin
def is_origin(P):
    if P == O:
        return True
    else:
        return False

# modular inverse
def inv_mod_p(x):
    if x % p == 0:
        raise ZeroDivisionError("No inverse")
    return pow(x, p-2,p)

# Additive inverse of elliptic curve point
def ec_inv(P):
    if P == O:
        return P
    return Point(P.x, (-P.y)%p)

# Add elliptic curve points
def ec_add(P, Q):
    if not (valid(P) and valid(Q)):
        raise ValueError("Invalid points")
    if P == O:
        result = Q
    elif Q == O:
        result = P
    elif Q == ec_inv(P):
        result =  O
    else:
        if P == Q:
            dydx = (3 * P.x**2 + a) * inv_mod_p(2 * P.y)
        else:
            dydx = (Q.y - P.y) * inv_mod_p(Q.x - P.x)
        x = (dydx**2 - P.x - Q.x) % p
        y = (dydx * (P.x - x) - P.y) % p
        result = Point(x, y)

    # The above computations *should* have given us another point
    # on the curve.
    assert valid(result)
    return result

########################################################################

plt.rcParams.update({
    'font.size': 16,
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

def isSquare(a):
    ls = pow(a, (p-1)//2, p)
    if (ls == 0) or (ls == 1):
        return True
    else:
        return False

def sqrt(a):
    sr = pow(a, (p+1)//4, p)
    return sr


# Region 1: standard
# Region 2: standard negative (-)
# Region 3: negative (p-)
xAll1 = []
xAll2 = []
xAll3 = []
yAll1 = []
yAll2 = []
yAll3 = []

# First thing: find *all* valid points
#   Loop through all x values and check to see if valid.
#   From there, include conjugate.
#   Store list of everything and do a scatter plot of results.
for xVal in range(p):
    ySquared = (xVal**3 + a*xVal + b) % p
    if not isSquare(ySquared):
        continue
    sr = sqrt(ySquared)
    if sr == 0:
        xAll1.append(xVal)
        yAll1.append(sr)
    else:
        srMin = min(sr, p-sr)
        xAll1.append(xVal)
        yAll1.append(srMin)
        xAll2.append(xVal)
        yAll2.append(-srMin)
        xAll3.append(xVal)
        yAll3.append(p-srMin)

xStart = 0
xStop = p
yStart = -(p//2)-1
yStop = p

assert a == 2
assert b == 1

x_major_ticks = np.arange(0,71,20)
y_major_ticks = np.arange(-30,71,10)

fig, ax = plt.subplots()

# Symmetry Base
plt.title(r'$y^2 = x^3 + 2x + 1$ over $\mathbb{{F}}_{{{0}}}$; Symmetry'.format(p))
plt.scatter(xAll1, yAll1, linewidths=5.0, alpha=1, color='blue')
plt.scatter(xAll2, yAll2, linewidths=5.0, alpha=1, color='green')
plt.scatter(xAll3, yAll3, linewidths=5.0, alpha=1, color='green')
plt.scatter(1, 2, linewidths=5.0, alpha=1, color='magenta')
plt.scatter(1, -2, linewidths=5.0, alpha=1, color='orange')
plt.scatter(1, p-2, linewidths=5.0, alpha=1, color='orange')
ax.set_xticks(x_major_ticks)
ax.set_yticks(y_major_ticks)
ax.set_aspect(0.5)

ax.axhline(y=p/2, linewidth=3.0, color='black', linestyle='--')
ax.axhline(y=0, linewidth=3.0, color='black', linestyle='--')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_symmetry_base'
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()



fig, ax = plt.subplots()

# Symmetry 1
plt.title(r'$y^2 = x^3 + 2x + 1$ over $\mathbb{{F}}_{{{0}}}$; Sym 1'.format(p))
plt.scatter(xAll1, yAll1, linewidths=5.0, alpha=1, color='blue')
plt.scatter(xAll3, yAll3, linewidths=5.0, alpha=1, color='green')
plt.scatter(1, 2, linewidths=5.0, alpha=1, color='magenta')
plt.scatter(1, p-2, linewidths=5.0, alpha=1, color='orange')
ax.axhline(y=p/2, linewidth=3.0, color='black', linestyle='--')

xStart = 0
xStop = p
yStart = 0
yStop = p

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_symmetry_1'
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()



fig, ax = plt.subplots()

# Symmetry 2
plt.title(r'$y^2 = x^3 + 2x + 1$ over $\mathbb{{F}}_{{{0}}}$; Sym 2'.format(p))
plt.scatter(xAll1, yAll1, linewidths=5.0, alpha=1, color='blue')
plt.scatter(xAll2, yAll2, linewidths=5.0, alpha=1, color='green')
plt.scatter(1, 2, linewidths=5.0, alpha=1, color='magenta')
plt.scatter(1, -2, linewidths=5.0, alpha=1, color='orange')
ax.axhline(y=0, linewidth=3.0, color='black', linestyle='--')

xStart = 0
xStop = p
yStart = -(p//2)-2
yStop = p//2+1

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_symmetry_2'
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()
