import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the Employee class."""

	def setUp(self):
		"""Create an employee for use in all methods."""
		self.worker = Employee('John', 'Smith', 30_000)

	def test_give_default_raise(self):
		"""
		Test whether a raise can be increased by the default amount of $5000.
		"""
		self.worker.give_raise()
		self.assertEqual(self.worker.get_salary(), 35_000)

	def test_give_custom_raise(self):
		"""
		Test if a custom raise amount can be given.
		"""
		self.worker.give_raise(1_000)
		self.assertEqual(self.worker.get_salary(), 31_000)


if __name__ == '__main__':
	unittest.main()