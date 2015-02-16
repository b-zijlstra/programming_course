#
# Calculate exp using a Taylor expansion
#
# Author: Ivo Filot <i.a.w.filot@tue.nl>
#

from math import exp
import sys

def factorial(i):
	"""
	Returns the factorial of i, i.e. i!
	"""
	if i < 1:
		return 1.0
	else:
		return i * factorial(i-1)

def pow(base, exp):
	"""
	Calculates the power of a base number
	"""
	return base**exp

def my_exp(x):
	"""
	Calculates the exponent using a Taylor expansion
	"""
	sum = 1.0
	term = 1.0 # temp value to hold term
	i = 1
	# keep iterating until the added term is less than the machine precision
	# alternatively, one could also use a fixed number of terms in the Taylor expansion,
	# however the number required to get sufficient accuracy depends on the value of x
	# and therefore a while loop is better
	while term > sys.float_info.epsilon:
		term = pow(x, i) / factorial(i)
		sum += term
		i += 1
	print "Required %i terms for convergence" % (i)
	return sum


error = 0	# collect total error
for i in range(0,10):
	my_val = my_exp(i)	# calculate exp using the Taylor expansion
	real_val = exp(i)	# calculate exp using the math library of Python
	error += abs(my_val - real_val)	# calculate the absolute difference
	print str(my_val) + " versus " + str(real_val)

print "The total error was %f" % (error)