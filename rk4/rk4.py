#
# RK4 integrator class
#
# Author: Ivo Filot
#

class RK4:
	"""
	Fixed step-size Fourth-order Runge-Kutta Integrator
	"""
	def __init__(self, _x, _y, _fptr, _h):
		"""
		Default constructor

		Defines the starting conditions x and y, sets a pointer to the
		function that sets the derivatives and sets a fixed step-size
		"""
		self.h = _h
		self.x = _x
		self.y = _y
		self.fptr = _fptr
	def iterate(self):
		"""
		Perform a single iterations and prints the result
		"""
		k1 = self.h * self.fptr(self.x, self.y)
		k2 = self.h * self.fptr(self.x + 0.5 * self.h, self.y + 0.5 * k1)
		k3 = self.h * self.fptr(self.x + 0.5 * self.h, self.y + 0.5 * k2)
		k4 = self.h * self.fptr(self.x + self.h, self.y + k3)
		self.y += (1.0/6.0) * k1 + (1.0/3.0) * k2 + \
		          (1.0/3.0) * k3 + (1.0/6.0) * k4
		self.x += self.h
		print "%f\t%f\t%f" % (self.x, self.y[0], self.y[1])