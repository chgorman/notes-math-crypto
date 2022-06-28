#!/usr/bin/env python3

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 16,
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

N = 20000
xStart = -5
xStop = 5
yStart = -5
yStop = 5

a = 4
b = 3
x = np.linspace(xStart, xStop, N)
yPos =  b*np.sqrt(1 - x**2/a**2)
yNeg = -b*np.sqrt(1 - x**2/a**2)


# Plot Setup
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot the functions
plt.title(r'$(x/{0})^2 + (y/{1})^2 = 1$ over $\mathbb{{R}}$'.format(a, b))
plt.plot(x, yPos, linewidth=3.0, color='blue', zorder=-1)
plt.plot(x, yNeg, linewidth=3.0, color='blue', zorder=-1)

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ellipse_reals_' + str(a) + '_' + str(b)
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()
