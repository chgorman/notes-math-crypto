#!/usr/bin/env python3

import scipy as sp
from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 16})

p = 73

xStart = 0
xStop = p-1
yStart = 0
yStop = p-1

x = [1, 4, 5, 7]
y = [2, 1, 1, 8]

# Plot Setup: Points
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot the data
plt.title('Lagrange Finite 2: Points')
plt.scatter(x, y, linewidth=3.0, color='red', zorder=0)

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'lagrange_finite_points_2'
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')

# Plot Setup: Points and Data
xNew = np.arange(xStart, xStop, 1)
yNew = (60*xNew**3 + 51*xNew**2 + 42*xNew + 68) % p
# Poly: 1/72*(13*x^3 - 124*x^2 + 323*x - 68)
# For p = 73, the equivalent form is
#           60*x^3 + 51*x^2 + 42*x + 68

# plot the data
plt.title('Lagrange Finite 2: Polynomial')
plt.scatter(xNew, yNew, linewidth=3.0, color='blue', zorder=-1)

# show the plot
figBase = 'lagrange_finite_poly_2'
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()
