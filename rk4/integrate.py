#
# Sample script how to integrate a 2nd order differential equation
# by integrating two simple ordinary differential equations. This
# script employs a Runge-Kutta Fourth Order ODE solver.
#
# Author: Ivo Filot
#

from vector import Vector
from rk4 import RK4
import copy

def func(x, y):
	"""
	Function to be parsed to the integrator class
	"""
	f = copy.deepcopy(y)
	f[0] = y[1]
	f[1] = -y[0]
	return f

integrator = RK4(0, Vector([0.0, 1.0]), func, 0.01) # construct integrator class
for i in range(0,500):							    # 500 iterations
	integrator.iterate()