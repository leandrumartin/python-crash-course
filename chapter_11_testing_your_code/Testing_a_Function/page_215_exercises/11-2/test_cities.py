import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
	"""Tests for '11-1-city_functions.py'."""

	def test1_city_country(self):
		"""Test if 'Santiago, Chile' works."""
		self.assertEqual(get_formatted_city('santiago', 'chile'),
						 'Santiago, Chile')

	def test1_city_country_population(self):
		"""Test if 'Santiago, Chile, population 5000000' works."""
		self.assertEqual(get_formatted_city('santiago', 'chile', population = 5_000_000),
						 'Santiago, Chile, population 5000000')

if __name__ == '__main__':
	unittest.main()