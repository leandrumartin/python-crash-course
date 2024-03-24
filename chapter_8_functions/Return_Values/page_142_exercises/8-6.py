def city_country(city_name, country):
	city_and_country = f"{city_name.title()}, {country.title()}"
	return city_and_country

print(city_country("santiago", "chile"))
print(city_country('Los Angeles', 'United States'))
print(city_country('London', 'united kingdom'))