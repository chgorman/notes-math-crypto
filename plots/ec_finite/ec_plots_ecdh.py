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

def double_and_add(P: Point, k: int):
    if k == 0:
        return Point(0,0)
    elif k == 1:
        return Point(P.x,P.y)
    elif k % 2 == 0:
        return double_and_add(ec_add(P,P), k//2)
    else:
        return ec_add(double_and_add(ec_add(P,P), (k-1)//2), P)
########################################################################

plt.rcParams.update({
    'font.size': 16,
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

xStart = 0
xStop = p
yStart = 0
yStop = p

P = Point(0,1) # base point
Q = Point(0,1)

x_subgroup = []
y_subgroup = []

x_subgroup.append(P.x)
y_subgroup.append(P.y)

while not is_origin(Q):
    Q = ec_add(P, Q)
    x_subgroup.append(Q.x)
    y_subgroup.append(Q.y)

# ECDH 1
alice = 29
A = double_and_add(P, alice)
bob = 14
B = double_and_add(P, bob)
k_Alice = double_and_add(B, alice)
k_Bob = double_and_add(A, bob)
assert k_Alice == k_Bob
K = Point(k_Alice.x, k_Alice.y)

# Plot Setup
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

assert a > 1
assert b > 0

# plot the functions
plt.title(r'$y^2 = x^3 + {0}x + {1}$ over $\mathbb{{F}}_{{{2}}}$; ECDH 1'.format(a,b,p))
plt.scatter(x_subgroup, y_subgroup, linewidths=3.0, alpha=0.1, color='green', zorder=1)
plt.scatter(A.x, A.y, linewidths=5.0, alpha=1, color='magenta', zorder=3)
plt.scatter(B.x, B.y, linewidths=5.0, alpha=1, color='blue', zorder=3)
plt.scatter(K.x, K.y, linewidths=5.0, alpha=1, color='purple', zorder=3)
plt.text(A.x + 2, A.y - 1.5, "Alice", color='magenta')
plt.text(B.x + 2, B.y - 1.5, "Bob",   color='blue')
plt.text(K.x + 2, K.y - 1.5, "Secret",color='purple')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_ecdh_1'
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()

# ECDH 2
alice = 17
A = double_and_add(P, alice)
bob = 27
B = double_and_add(P, bob)
k_Alice = double_and_add(B, alice)
k_Bob = double_and_add(A, bob)
assert k_Alice == k_Bob
K = Point(k_Alice.x, k_Alice.y)

# Plot Setup
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot the functions
plt.title(r'$y^2 = x^3 + {0}x + {1}$ over $\mathbb{{F}}_{{{2}}}$; ECDH 2'.format(a,b,p))
plt.scatter(x_subgroup, y_subgroup, linewidths=3.0, alpha=0.1, color='green', zorder=1)
plt.scatter(A.x, A.y, linewidths=5.0, alpha=1, color='magenta', zorder=3)
plt.scatter(B.x, B.y, linewidths=5.0, alpha=1, color='blue', zorder=3)
plt.scatter(K.x, K.y, linewidths=5.0, alpha=1, color='purple', zorder=3)
plt.text(A.x + 2, A.y - 1.5, "Alice", color='magenta')
plt.text(B.x + 2, B.y - 1.5, "Bob",   color='blue')
plt.text(K.x + 2, K.y - 1.5, "Secret",color='purple')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b) + '_ecdh_2'
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()
