#!/usr/bin/env python3

import scipy as sp
from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 16})

N = 10000
xStart = 0
xStop = 10
yStart = 0
yStop = 10

x = [1, 4, 5, 7]
y = [2, 1, 1, 8]


# Plot Setup: Points
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot the data
plt.title('Lagrange Reals 2: Points')
plt.scatter(x, y, linewidth=3.0, color='red', zorder=0)

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'lagrange_reals_points_2'
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')

# Plot Setup: Points and Data
poly = sp.interpolate.lagrange(x,y)
xNew = np.linspace(xStart, xStop, N)
yNew = np.polynomial.polynomial.Polynomial(poly.coef[::-1])(xNew)

# plot the data
plt.title('Lagrange Reals 2: Polynomial')
plt.plot(xNew, yNew, linewidth=3.0, color='blue', zorder=-1)

# show the plot
figBase = 'lagrange_reals_poly_2'
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()
