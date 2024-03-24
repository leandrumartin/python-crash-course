prompt = "\nHow old is each person receiving a movie ticket?"
prompt += "\nType 'quit' when you are done naming the age of everyone in your party. "

answer = ""
while answer != 'quit':
	answer = input(prompt)
	
	if answer != 'quit':
		if int(answer) < 3:
			print("Your ticket is free!")
		elif int(answer) <= 12:
			print("Your ticket costs $10.")
		elif int(answer) > 12:
			print("Your ticket costs $15.")