#!/usr/bin/env python3

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

print('Elliptic Curve: y**2 == x**3 + %d*x + %d over F_%d; Double-and-Add' % (a, b, p))
print("#"*72)
print()

P = Point(0,1)
k = 29

R = double_and_add(P, k)
print('%2d*(%2d,%2d) = (%2d,%2d)' % (k, P.x, P.y, R.x, R.y))

print()
P = Point(0, 1)
Q = Point(0, 1)
R = ec_add(P,Q)
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q.x, Q.y, R.x, R.y))

P = Point(1, 69)
Q = Point(1, 69)
R = ec_add(P,Q)
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q.x, Q.y, R.x, R.y))

P = Point(4, 59)
Q = Point(4, 59)
R = ec_add(P,Q)
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q.x, Q.y, R.x, R.y))

P = Point(56, 2)
Q = Point(56, 2)
R = ec_add(P,Q)
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q.x, Q.y, R.x, R.y))

print()
P = Point(56, 2)
Q = Point(67, 0)
R = ec_add(P,Q)
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q.x, Q.y, R.x, R.y))

P = Point(4, 59)
Q = Point(56, 69)
R = ec_add(P,Q)
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q.x, Q.y, R.x, R.y))

P = Point(0, 1)
Q = Point(4, 12)
R = ec_add(P,Q)
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q.x, Q.y, R.x, R.y))
