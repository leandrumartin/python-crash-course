answer = input('Which exercise would you like to see? Type a number from 3.8-3.10')

if answer == '3.8':
	places_to_visit = ['North Korea', 'London', 'Madrid', 'Canada', 'Rome']

	print(places_to_visit)
	print(sorted(places_to_visit))

	print('\n')

	print(places_to_visit)
	print(sorted(places_to_visit, reverse=True))

	print('\n')

	print(places_to_visit)
	places_to_visit.reverse()
	print(places_to_visit)
	places_to_visit.reverse()
	print(places_to_visit)

	print('\n')

	print(places_to_visit)
	places_to_visit.sort()
	print(places_to_visit)
	places_to_visit.sort(reverse=True)
	print(places_to_visit)

elif answer == '3.9':
	invitees = ['your mom', 'martin luther king', 'obama']
	print(len(invitees))