prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# We need to first set "message" to an empty string so that the while loop after it can run the first time.
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)

# This first time, it prints the message "quit" when you say "quit." Let's fix this.

print("\nLet's do this again! This time, I won't say 'quit' when you tell me to quit.")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)

# Let's make a "flag," a variable that determines whether the program is active.
# This way, we can easily have multiple criteria determine whether to end the program.

print("\nSorry for not quitting just yet! I'm going to do something different behind the scenes this time.")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)