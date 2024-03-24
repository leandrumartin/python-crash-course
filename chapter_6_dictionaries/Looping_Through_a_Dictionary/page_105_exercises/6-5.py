river_countries = {'nile': 'egypt', 'amazon': 'brazil', 'mississippi': 'america'}

# Don't forget to include the items() method as seen below!
for river, country in river_countries.items():
	print(f"The {river.title()} River runs in {country.title()}.")

for river in river_countries.keys():
	print(river)

for country in river_countries.values():
	print(country)