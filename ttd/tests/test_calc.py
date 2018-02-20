import unittest
from app.calculator import Calculator

class test_calculator(unittest.TestCase):
	def setUp(self):
		self.calc = Calculator()

	def test_add_method(self):
		result = self.calc.add(2, 2)
		self.assertEqual(result, 4, msg='Add method failed')

	def test_add_fails_if_not_numbers(self):
		self.assertRaises(ValueError, self.calc.add, 'jj', 2)

	

if __name__ == '__main__':
    unittest.main()

