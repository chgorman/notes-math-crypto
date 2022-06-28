#!/usr/bin/env python3

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 16,
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

#  y^2 == x^3 + 8 (has zero at -2)
#
# Plot (-5,5) x (-5,5)

N = 20000
xStart = -5
xStop = 5
yStart = -5
yStop = 5

bC = 1
abList = ([-3,bC], [-2,bC], [-1,bC], [0,bC], [1,bC], [2,bC])
#aC = 1
#abList = ([aC,-10], [aC,-5], [aC,-1], [aC,0], [aC,5], [aC,10])

for item in abList:
    a = item[0]
    b = item[1]
    x = np.linspace(xStart, xStop, N)
    yPos =  np.sqrt(x**3 + a*x + b)
    yNeg = -np.sqrt(x**3 + a*x + b)


    # Plot Setup
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # plot the functions
    if a == 1:
        if b > 0:
            plt.title(r'$y^2 = x^3 + x + {0}$ over $\mathbb{{R}}$'.format(b))
        elif b < 0:
            plt.title(r'$y^2 = x^3 + x - {0}$ over $\mathbb{{R}}$'.format(-b))
        else:
            plt.title(r'$y^2 = x^3 + x$ over $\mathbb{{R}}$') # b == 0
    elif a == -1:
        if b > 0:
            plt.title(r'$y^2 = x^3 - x + {0}$ over $\mathbb{{R}}$'.format(b))
        elif b < 0:
            plt.title(r'$y^2 = x^3 - x - {0}$ over $\mathbb{{R}}$'.format(-b))
        else:
            plt.title(r'$y^2 = x^3 - x$ over $\mathbb{{R}}$') # b == 0
    elif a == 0:
        if b > 0:
            plt.title(r'$y^2 = x^3 + {0}$ over $\mathbb{{R}}$'.format(b))
        elif b < 0:
            plt.title(r'$y^2 = x^3 - {0}$ over $\mathbb{{R}}$'.format(-b))
        else:
            plt.title(r'$y^2 = x^3$ over $\mathbb{{R}}$') # b == 0
    elif (a > 1):
        if b > 0:
            plt.title(r'$y^2 = x^3 + {0}x + {1}$ over $\mathbb{{R}}$'.format(a, b))
        elif b < 0:
            plt.title(r'$y^2 = x^3 + {0}x - {1}$ over $\mathbb{{R}}$'.format(a, -b))
        else:
            plt.title(r'$y^2 = x^3 + {0}x$ over $\mathbb{{R}}$'.format(a)) # b == 0
    else:
        if b > 0:
            plt.title(r'$y^2 = x^3 - {0}x + {1}$ over $\mathbb{{R}}$'.format(-a, b))
        elif b < 0:
            plt.title(r'$y^2 = x^3 - {0}x - {1}$ over $\mathbb{{R}}$'.format(-a, -b))
        else:
            plt.title(r'$y^2 = x^3 - {0}x$ over $\mathbb{{R}}$'.format(-a)) # b == 0

    plt.plot(x, yPos, linewidth=3.0, color='blue', zorder=-1)
    plt.plot(x, yNeg, linewidth=3.0, color='blue', zorder=-1)

    plt.xlim([xStart, xStop])
    plt.ylim([yStart, yStop])

    # show the plot
    figBase = 'ec_reals_' + str(a) + '_' + str(b)
    figBase = figBase.replace('-','n')
    figName = figBase+'.pdf'
    plt.savefig(figName, bbox_inches='tight')
    plt.close()
