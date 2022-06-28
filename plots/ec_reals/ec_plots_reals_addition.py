#!/usr/bin/env python3

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 16,
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

#  y^2 == x^3 - 4x + 1
#
# Plot (-3,3) x (-3,3)

N = 30000
xStart = -3
xStop = 3
yStart = -3
yStop = 3

a = -4
b = 1

x = np.linspace(xStart, xStop, N)
yPos =  np.sqrt(x**3 + a*x + b)
yNeg = -np.sqrt(x**3 + a*x + b)

# Red
x1 = 0
y1 = np.sqrt(x1**3 + a*x1 + b)
# Orange
x2 = 2
y2 = -np.sqrt(x2**3 + a*x2 + b)

s = (y2-y1)/(x2-x1)
# Green
x3 = s**2 - x1 - x2
y3 = s*(x1-x3) - y1

x_array = np.array([x1, x2, x3])
y_array = np.array([y1, y2, -y3])
argmin = x_array.argmin()
argmax = x_array.argmax()

x1_coord = x_array[argmin] - 0.5
x2_coord = x_array[argmax] + 0.5

# Line for P, Q, R'
x_line_1 = np.linspace(x1_coord, x2_coord, N)
y_line_1 = y1 + s*(x_line_1 - x1)

# Line for R and R'
x_line_2 = np.full(N, x3)
y_line_2 = np.linspace(y3-0.5, -y3+0.5, N)

# Plot Setup
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot the functions
assert a < 0
assert b > 0
plt.title(r'$y^2 = x^3 - {0}x + {1}$ over $\mathbb{{R}}$; Addition 1'.format(-a, b))
plt.plot(x, yPos, linewidth=3.0, color='blue', zorder=-1)
plt.plot(x, yNeg, linewidth=3.0, color='blue', zorder=-1)
plt.scatter(x1, y1, linewidths=5.0, alpha=1, color='red')
plt.scatter(x2, y2, linewidths=5.0, alpha=1, color='orange')
plt.scatter(x3, -y3, linewidths=5.0, alpha=0.5, color='green')
plt.scatter(x3, y3, linewidths=5.0, alpha=1, color='green')
plt.plot(x_line_1, y_line_1, linewidth=2.0, color='black', linestyle='--')
plt.plot(x_line_2, y_line_2, linewidth=2.0, color='black', linestyle=':')
plt.text(x1+0.15, y1+0.15, r'$P$', color='red')
plt.text(x2+0.15, y2+0.15, r'$Q$', color='orange')
plt.text(x3+0.15, y3-0.5, r'$R$', color='green')
plt.text(x3+0.15, -y3+0.15, r"$R^{\prime}$", color='green')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_reals_addition_1'
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()

# Another plot
x1_prime = -1.0
y1_prime = np.sqrt(x1_prime**3 + a*x1_prime + b)
s = (3*x1_prime**2 + a)/(2*y1_prime)
x3_prime = s**2 - 2*x1_prime
y3_prime = s*(x1_prime-x3_prime) - y1_prime

x_array_prime = np.array([x1_prime, x3_prime])
y_array_prime = np.array([y1_prime, -y3_prime])
argmin_prime = x_array_prime.argmin()
argmax_prime = x_array_prime.argmax()

x1_coord_prime = x_array_prime[argmin_prime] - 0.5
x2_coord_prime = x_array_prime[argmax_prime] + 0.5

# Line for P, Q, R'
x_line_1_prime = np.linspace(x1_coord_prime, x2_coord_prime, N)
y_line_1_prime = y1_prime + s*(x_line_1_prime - x1_prime)

# Line for R and R'
x_line_2_prime = np.full(N, x3_prime)
y_line_2_prime = np.linspace(y3_prime-0.5, -y3_prime+0.5, N)

# Plot Setup
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot the functions
plt.title(r'$y^2 = x^3 - {0}x + {1}$ over $\mathbb{{R}}$; Addition 2'.format(-a, b))
plt.plot(x, yPos, linewidth=3.0, color='blue', zorder=-1)
plt.plot(x, yNeg, linewidth=3.0, color='blue', zorder=-1)
plt.scatter(x1_prime, y1_prime, linewidths=5.0, alpha=1, color='red')
plt.scatter(x3_prime, -y3_prime, linewidths=5.0, alpha=0.5, color='green')
plt.scatter(x3_prime, y3_prime, linewidths=5.0, alpha=1, color='green')
plt.plot(x_line_1_prime, y_line_1_prime, linewidth=2.0, color='black', linestyle='--')
plt.plot(x_line_2_prime, y_line_2_prime, linewidth=2.0, color='black', linestyle=':')
plt.text(x1_prime+0.15, y1_prime+0.15, r'$P$', color='red')
plt.text(x3_prime+0.25, y3_prime-0.5, r'$R$', color='green')
plt.text(x3_prime+0.25, -y3_prime+0.15, r"$R^{\prime}$", color='green')

plt.xlim([xStart, xStop])
plt.ylim([yStart, yStop])

# show the plot
figBase = 'ec_reals_addition_2'
figBase = figBase.replace('-','n')
figName = figBase+'.pdf'
plt.savefig(figName, bbox_inches='tight')
plt.close()
