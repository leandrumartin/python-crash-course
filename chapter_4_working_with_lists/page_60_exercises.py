wanted_exercise = input('Which exercise would you like to run? Choose a number from 4.3-4.9.')

if wanted_exercise == 4.3:
	for number in range(1, 21):
		print(number)

elif wanted_exercise == 4.4:
	numbers = []
	for number in range(1, 1_000_001):
		numbers.append(number)
		print(number)

elif wanted_exercise == 4.5:
	numbers = []
	for number in range(1, 1000001):
		numbers.append(number)
	print(min(numbers))
	print(max(numbers))
	print(sum(numbers))

elif wanted_exercise == 4.6:
	for odd in range(1, 21, 2):
		print(odd)

elif wanted_exercise == 4.7:
	for multiple_of_three in range(3, 31, 3):
		print (multiple_of_three)

elif wanted_exercise == 4.8:
	cubes = []
	for value in range(1, 11):
		cubes.append(value**3)
		print(cubes[-1])

elif wanted_exercise == 4.9:
	cubes = [value**3 for value in range(1, 11)]
	print(cubes)