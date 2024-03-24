class Employee():
	"""A respresentation of a company employee."""

	def __init__(self, first_name, last_name, salary):
		"""Store the employee's name and salary."""
		self._first_name = first_name
		self._last_name = last_name
		self._salary = salary

	def get_first_name(self):
		return self._first_name

	def get_last_name(self):
		return self._last_name

	def get_salary(self):
		return self._salary

	def give_raise(self, amount=5_000):
		"""Increase salary by the inputted amount."""
		self._salary += amount