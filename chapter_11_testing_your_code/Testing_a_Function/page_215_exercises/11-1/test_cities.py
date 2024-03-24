import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
	"""Tests for '11-1-city_functions.py'."""

	def test1_city_country(self):
		self.assertEqual(get_formatted_city('santiago', 'chile'),
						 'Santiago, Chile')

if __name__ == '__main__':
	unittest.main()