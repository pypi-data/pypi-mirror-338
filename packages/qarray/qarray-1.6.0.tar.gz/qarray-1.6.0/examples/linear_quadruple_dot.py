"""
Quadruple dot example
"""
import time
from functools import partial

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from qarray import (DotArray, GateVoltageComposer, charge_state_changes)

# setting up the constant capacitance model for a linear quadruple dot
# the plunger gates couple to their repsective dots with capacitance 1. and to the next dot with capacitance 0.2
# and the next dot with capacitance 0.05 and finally the furthest dot with strength 0.01.
# the interdot capacitance between neighbouring dots are 0.3
# the interdot capacitance between next nerest neighbours are 0.05
# the interdot capacitance between the furthest dots are 0.01

cdd_non_maxwell = [
    [0., 0.3, 0.05, 0.01],
    [0.3, 0., 0.3, 0.05],
    [0.05, 0.3, 0., 0.3],
    [0.01, 0.05, 0.3, 0]
]
cgd_non_maxwell = [
    [1., 0.2, 0.05, 0.01],
    [0.2, 1., 0.2, 0.05],
    [0.05, 0.2, 1., 0.2],
    [0.01, 0.05, 0.2, 1]
]

model = DotArray(
    Cdd=cdd_non_maxwell,
    Cgd=cgd_non_maxwell,
)

# creating the dot voltage composer, which helps us to create the dot voltage array
# for sweeping in 1d and 2d
voltage_composer = GateVoltageComposer(n_gate=model.n_gate)

# defining the functions to compute the ground state for the different cases
ground_state_funcs = [
    model.ground_state_open,
    partial(model.ground_state_closed, n_charges=1),
    partial(model.ground_state_closed, n_charges=2),
    partial(model.ground_state_closed, n_charges=3)
]

# defining the min and max values for the dot voltage sweep

vx_min, vx_max = -10, 10
vy_min, vy_max = -10, 10
# using the dot voltage composer to create the dot voltage array for the 2d sweep
vg = voltage_composer.do2d(1, vy_min, vx_max, 200, 4, vy_min, vy_max, 200)

# creating the figure and axes
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
fig.set_size_inches(3, 3)
c = np.linspace(0.9, 1.1, 4)

# looping over the functions and axes, computing the ground state and plot the results
for (func, ax) in zip(ground_state_funcs, axes.flatten()):
    t0 = time.time()
    n = func(vg)  # computing the ground state by calling the function
    t1 = time.time()
    print(f'{t1 - t0:.3f} seconds')
    # passing the ground state to the dot occupation changes function to compute when
    # the dot occupation changes
    z = charge_state_changes(n)
    # plotting the result
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white", "black"])
    ax.imshow(z, extent=[vx_min, vx_max, vy_min, vy_max], origin='lower',
              aspect='auto', cmap=cmap,
              interpolation='antialiased')
    ax.set_aspect('equal')
fig.tight_layout()

# setting the labels and titles
axes[0, 0].set_ylabel(r'$V_y$')
axes[1, 0].set_ylabel(r'$V_y$')
axes[1, 0].set_xlabel(r'$V_x$')
axes[1, 1].set_xlabel(r'$V_x$')

axes[0, 0].set_title(r'Open')
axes[0, 1].set_title(r'$n_{charge} = 1$')
axes[1, 0].set_title(r'$n_{charge} = 2$')
axes[1, 1].set_title(r'$n_{charge} = 3$')

plt.savefig('quadruple_dot.pdf', bbox_inches='tight')

if __name__ == '__main__':
    plt.show()
