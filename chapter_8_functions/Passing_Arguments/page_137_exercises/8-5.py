def describe_city(city_name, country='australia'):
	"""Say what country a city is in."""
	print(f"{city_name.title()} is in {country.title()}.")

describe_city('canberra')
describe_city('reykjavik', country='iceland')
describe_city('sydney')