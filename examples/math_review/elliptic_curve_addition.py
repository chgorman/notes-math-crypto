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

########################################################################

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

print('Elliptic Curve: y**2 == x**3 + %d*x + %d over F_%d; Addition' % (a, b, p))
print("#"*72)
print()
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q1.x, Q1.y, R1.x, R1.y))
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q2.x, Q2.y, R2.x, R2.y))
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q3.x, Q3.y, R3.x, R3.y))
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q4.x, Q4.y, R4.x, R4.y))
print('(%2d,%2d) + (%2d,%2d) = (%2d,%2d)' % (P.x, P.y, Q5.x, Q5.y, R5.x, R5.y))
