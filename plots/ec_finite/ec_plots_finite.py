#!/usr/bin/env python3

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 16,
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

# Finite field: F_71
p = 71 # p == 3 mod 4

def isSquare(a):
    ls = pow(a, (p-1)//2, p)
    if (ls == 0) or (ls == 1):
        return True
    else:
        return False

def sqrt(a):
    sr = pow(a, (p+1)//4, p)
    return sr


xStart = 0
xStop = p
yStart = 0
yStop = p

bC = 1
abList = ([-3,bC], [-2,bC], [-1,bC], [0,bC], [1,bC], [2,bC])
#aC = 1
#abList = ([aC,-10], [aC,-5], [aC,-1], [aC,0], [aC,5], [aC,10])

for item in abList:
    a = item[0] % p
    b = item[1] % p

    # First thing: find *all* valid points
    #   Loop through all x values and check to see if valid.
    #   From there, include conjugate.
    #   Store list of everything and do a scatter plot of results.

    x = []
    y = []

    for xVal in range(p):
        ySquared = (xVal**3 + a*xVal + b) % p
        if not isSquare(ySquared):
            continue
        sr = sqrt(ySquared)
        if sr == 0:
            x.append(xVal)
            y.append(sr)
        else:
            x.append(xVal)
            y.append(sr)
            x.append(xVal)
            y.append(p-sr)

    # Plot Setup
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # plot the functions
    if a == 1:
        if b > 0:
            plt.title(r'$y^2 = x^3 + x + {0}$ over $\mathbb{{F}}_{{{1}}}$'.format(b,p))
        else:
            plt.title(r'$y^2 = x^3 + x$ over $\mathbb{{F}}_{{{0}}}$'.format(p)) # b == 0
    elif a == 0:
        if b > 0:
            plt.title(r'$y^2 = x^3 + {0}$ over $\mathbb{{F}}_{{{1}}}$'.format(b,p))
        else:
            plt.title(r'$y^2 = x^3$ over $\mathbb{{F}}_{{{0}}}$'.format(p)) # b == 0
    else:
        if b > 0:
            plt.title(r'$y^2 = x^3 + {0}x + {1}$ over $\mathbb{{F}}_{{{2}}}$'.format(a, b, p))
        else:
            plt.title(r'$y^2 = x^3 + {0}x$ over $\mathbb{{F}}_{{{1}}}$'.format(a,p)) # b == 0

    plt.scatter(x, y, linewidths=5.0, alpha=1, color='blue')

    plt.xlim([xStart, xStop])
    plt.ylim([yStart, yStop])

    # show the plot
    figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b)
    figBase = figBase.replace('-','n')
    figName = figBase+'.pdf'
    plt.savefig(figName, bbox_inches='tight')
    plt.close()

