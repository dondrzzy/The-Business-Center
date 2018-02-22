class Calculator(object):
	"""docstring for Calculator"""
	def __init__(self, arg = 0):
		self.arg = arg

	def add(self, x, y):
		number_types = (int,  float, complex)
		if isinstance(x, number_types) and isinstance(y, number_types):
			return x + y
		else:
			raise ValueError


		