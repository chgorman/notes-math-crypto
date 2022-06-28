#!/usr/bin/env python3

import matplotlib.pyplot as plt

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


xAll = []
yAll = []

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
        xAll.append(xVal)
        yAll.append(sr)
    else:
        xAll.append(xVal)
        yAll.append(sr)
        xAll.append(xVal)
        yAll.append(p-sr)

xStart = 0
xStop = p
yStart = 0
yStop = p

initialPoint = ([0,1], [1,2], [4,12], [6,4], [7,28], [10, 13])
assert a == 2
assert b == 1

# Loop through 
for item in initialPoint:
    P = Point(item[0] % p, item[1] % p)
    Q = Point(item[0] % p, item[1] % p)

    # Plot Setup
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # plot the functions
    plt.title(r'$y^2 = x^3 + 2x + 1$ over $\mathbb{{F}}_{{{0}}}$; $\langle({1},{2})\rangle$'.format(p, P.x, P.y))
    plt.scatter(xAll, yAll, linewidths=5.0, alpha=1, color='blue', zorder=1)
    plt.scatter(P.x, P.y, linewidths=5.0, alpha=1, color='magenta', zorder=3)

    # plot subgroup
    x = []
    y = []

    x.append(P.x)
    y.append(P.y)

    count = 1
    assert valid(P)
    while True:
        count += 1
        R = ec_add(P,Q)
        if is_origin(R):
            break
        Q = Point(R.x, R.y)
        x.append(Q.x)
        y.append(Q.y)

    plt.scatter(x, y, linewidths=5.0, alpha=1, color='orange', zorder=2)


    plt.xlim([xStart, xStop])
    plt.ylim([yStart, yStop])

    # show the plot
    figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_subgroup_' + str(P.x) + '_' + str(P.y)
    figBase = figBase.replace('-','n')
    figName = figBase+'.pdf'
    plt.savefig(figName, bbox_inches='tight')
    plt.close()
