height = input("How tall are you, in inches? ")
# This next line is necessary because by default, the input is a string, but we need to work with it as a numbwer.
height = int(height)

if height >= 48:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")