current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

# Let's use the 'continue' statment to go back to the beginning of a loop.
# In this case, we'll run through the numbers from 1 to 10 and only print the odd numbers.
print("\n")

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 ==0:
		continue

	print(current_number)

# This next loop will run forever!
# Press ctrl+C in your terminal window (or the output window of your editor) to stop it.

answer = input("Run infinite loop? ")
answer = answer.lower()
answer = answer.strip()

if answer == 'yes':
	x = 1
	while x <= 5:
		print(x)
