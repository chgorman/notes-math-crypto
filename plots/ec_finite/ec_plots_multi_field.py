#!/usr/bin/env python3

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

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

a = 1
b = 3
assert a == 1
assert b > 0

pList = (19, 43, 139, 151, 227, 311)

for item in pList:
    p = item

    xStart = 0
    xStop = p
    yStart = 0
    yStop = p

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
    plotTitle = r'$y^2 = x^3 + x + {0}$ over $\mathbb{{F}}_{{{1}}}$'.format(b, p)
    plt.title(plotTitle)
    plt.scatter(x, y, linewidths=5.0, alpha=1, color='blue')

    plt.xlim([xStart, xStop])
    plt.ylim([yStart, yStop])

    # show the plot
    figBase = 'ec_finite_F_' + str(p) + '_' + str(a) + '_' + str(b)
    figBase = figBase.replace('-','n')
    figName = figBase+'.pdf'
    plt.savefig(figName, bbox_inches='tight')
    plt.close()

