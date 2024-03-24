cities = {
	'new york': {
		'state': 'new york',
		'mayor': 'bill de blasio',
		'population': '8,800,000',
		},
	'san francisco': {
		'state': 'california',
		'mayor': 'london breed',
		'population': '873,965',
		},
	'seattle': {
		'state': 'washington',
		'mayor': 'jenny durkan',
		'population': '737,015',
		},
	}

for city, city_info in cities.items():
	print(f"{city.title()}")
	for info_type, info in city_info.items():
		print(f"\t{info_type}: {info.title()}")