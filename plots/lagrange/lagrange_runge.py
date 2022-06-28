#!/usr/bin/env python3

import scipy as sp
from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 16})

N = 10000
xStart = -1
xStop = 1
yStart = -1
yStop = 2

# Interpolation Points
xN = 21
xInterp = np.linspace(xStart,xStop,xN)
yInterp = 1.0/(1.0 + 25.0*xInterp**2)

# Function points
xFunc = np.linspace(xStart,xStop,N)
yFunc = 1.0/(1.0 + 25.0*xFunc**2)

# Points and Data
poly = sp.interpolate.lagrange(xInterp,yInterp)
xNew = np.linspace(xStart, xStop, N)
yNew = np.polynomial.polynomial.Polynomial(poly.coef[::-1])(xNew)

# Plot Setup
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot the data
plt.title('Runge\'s Phenomenon')
plt.scatter(xInterp, yInterp, linewidth=3.0, color='red', zorder=1)
plt.plot(xFunc, yFunc, linewidth=3.0, color='blue', zorder=-1)
plt.plot(xNew, yNew, linewidth=3.0, color='gold', zorder=0)

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'lagrange_runge'
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()
