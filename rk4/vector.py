#
# Vector class
#
# Author: Ivo Filot
#

import copy # for deepcopy

class Vector:
	""" 
	Vector class

	Provides mathematical operations between vectors, and between
	vectors and floats, which are not possible using simple lists.
	"""
	def __init__(self, _v):
		"""
		Default constructor

		Takes a list as an argument. Automatically calculates the length
		of the vector.
		"""
		self.v = copy.deepcopy(_v)
		self.n = len(self.v)
	def __len__(self):
		"""
		Returns the length of the vector
		"""
		return self.n
	def __getitem__(self, i):
		"""
		Get the value at the position i. This function enables the direct
		use of [] on the class variable.
		"""
		if i < self.n:
			return self.v[i]
	def __setitem__(self, i, val):
		"""
		Set the value at the position i. This function enables the direct
		use of [] on the class variable.
		"""
		if i < self.n:
			self.v[i] = val
	def __add__(self, _v):
		"""
		Add two vectors. An automatic check is performed that the two vectors
		have the same size. A deepcopy has to be used because of the behaviour
		of the copy constructor of Python
		"""
		if len(self) == len(_v):
			ans = copy.deepcopy(self)
			for i in range(0, self.n):
				ans[i] += _v[i]
			return ans
	def __mul__(self, _scalar):
		"""
		Multiply a vector by a scalar
		"""
		ans = copy.deepcopy(self)
		for i in range(0, self.n):
				ans[i] *= _scalar
		return ans
	def __rmul__(self, _scalar):
		"""
		Multiply a vector by a scalar when the Vector class is the rhs
		of the multiplication.
		"""
		return self * _scalar
	def __div__(self, _scalar):
		"""
		Divide a vector by a scalar
		"""
		ans = copy.deepcopy(self)
		for i in range(0, self.n):
				ans[i] /= _scalar
		return ans
	def __rdiv__(self, _scalar):
		"""
		Divide a vector by a scalar when the Vector class is the rhs
		of the multiplication.
		"""
		return self / _scalar
	def __str__(self):
		return str(self.v)