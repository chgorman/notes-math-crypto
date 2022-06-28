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

P = Point(17,7)

Q1 = Point(20,35)
Q2 = Point(21,28)
Q3 = Point(22,16)
Q4 = Point(23,12)
Q5 = Point(29,33)

R1 = ec_add(P,Q1)
R2 = ec_add(P,Q2)
R3 = ec_add(P,Q3)
R4 = ec_add(P,Q4)
R5 = ec_add(P,Q5)

assert a == 2
assert b == 1


# Base
plt.title(r'$y^2 = x^3 + 2x + 1$ over $\mathbb{{F}}_{{{0}}}$'.format(p))
plt.scatter(xAll, yAll, linewidths=5.0, alpha=1, color='blue')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_addition_base'
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()



# P + Q1
plt.title(r'$y^2 = x^3 + 2x + 1; ({0},{1})+({2},{3})$'.format(P.x, P.y, Q1.x, Q1.y))
plt.scatter(xAll, yAll, linewidths=3.0, alpha=0.1, color='blue')
plt.scatter([P.x], [P.y], linewidths=5.0, alpha=1, color='red')
plt.scatter([Q1.x], [Q1.y], linewidths=5.0, alpha=1, color='orange')
plt.scatter([R1.x], [R1.y], linewidths=5.0, alpha=1, color='green')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_addition_' + str(Q1.x) + '_' + str(Q1.y)
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()


# P + Q2
plt.title(r'$y^2 = x^3 + 2x + 1; ({0},{1})+({2},{3})$'.format(P.x, P.y, Q2.x, Q2.y))
plt.scatter(xAll, yAll, linewidths=3.0, alpha=0.1, color='blue')
plt.scatter([P.x], [P.y], linewidths=5.0, alpha=1, color='red')
plt.scatter([Q2.x], [Q2.y], linewidths=5.0, alpha=1, color='orange')
plt.scatter([R2.x], [R2.y], linewidths=5.0, alpha=1, color='green')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_addition_' + str(Q2.x) + '_' + str(Q2.y)
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()


# P + Q3
plt.title(r'$y^2 = x^3 + 2x + 1; ({0},{1})+({2},{3})$'.format(P.x, P.y, Q3.x, Q3.y))
plt.scatter(xAll, yAll, linewidths=3.0, alpha=0.1, color='blue')
plt.scatter([P.x], [P.y], linewidths=5.0, alpha=1, color='red')
plt.scatter([Q3.x], [Q3.y], linewidths=5.0, alpha=1, color='orange')
plt.scatter([R3.x], [R3.y], linewidths=5.0, alpha=1, color='green')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_addition_' + str(Q3.x) + '_' + str(Q3.y)
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()


# P + Q4
plt.title(r'$y^2 = x^3 + 2x + 1; ({0},{1})+({2},{3})$'.format(P.x, P.y, Q4.x, Q4.y))
plt.scatter(xAll, yAll, linewidths=3.0, alpha=0.1, color='blue')
plt.scatter([P.x], [P.y], linewidths=5.0, alpha=1, color='red')
plt.scatter([Q4.x], [Q4.y], linewidths=5.0, alpha=1, color='orange')
plt.scatter([R4.x], [R4.y], linewidths=5.0, alpha=1, color='green')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_addition_' + str(Q4.x) + '_' + str(Q4.y)
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()


# P + Q5
plt.title(r'$y^2 = x^3 + 2x + 1; ({0},{1})+({2},{3})$'.format(P.x, P.y, Q5.x, Q5.y))
plt.scatter(xAll, yAll, linewidths=3.0, alpha=0.1, color='blue')
plt.scatter([P.x], [P.y], linewidths=5.0, alpha=1, color='red')
plt.scatter([Q5.x], [Q5.y], linewidths=5.0, alpha=1, color='orange')
plt.scatter([R5.x], [R5.y], linewidths=5.0, alpha=1, color='green')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_addition_' + str(Q5.x) + '_' + str(Q5.y)
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()
