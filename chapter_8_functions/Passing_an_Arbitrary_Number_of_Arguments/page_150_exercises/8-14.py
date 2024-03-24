def car_details(manufacturer, model, **car_details):
	car_details['manufacturer'] = manufacturer.title()
	car_details['model'] = model.title()
	print(car_details)

car_details('Subaru', 'outback',
			color='black',
			sunroof=True)
car_details('buick', 'enclave',
			color='white',
			sunroof=False)