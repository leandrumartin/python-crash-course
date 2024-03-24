responses = {}

polling_active = True

while polling_active:
	name = input("What's your name? ")
	response = input('Where would your dream vacation be? ')
	responses[name] = response

	continue_poll = input('Is there someone else to poll? (yes/no) ').lower()
	if continue_poll == 'no':
		polling_active = False

	print('\n')

for name, response in responses.items():
	print(f"{name.title()}'s dream vacation is in {response.title()}.")