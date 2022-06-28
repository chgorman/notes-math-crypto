#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 16,
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

# TODO: possibly annotate more in the future if questions arise.

N = 20000
xStart = -3
xStop = 3
yStart = -2
yStop = 9

x = np.linspace(xStart, xStop, N)
y = x**2


# Plot Setup
fig = plt.figure()

# plot the functions
plt.title(r'$f(x) = x^2$')
plt.xlabel('domain', fontsize=24)
plt.ylabel('codomain', fontsize=24)
plt.plot(x, y, linewidth=3.0, color='blue')
plt.xlim([xStart*1.05,xStop*1.05])
plt.ylim([yStart*1.20,yStop*1.05])

# show the plot
figBase = 'function_parabola'
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()
