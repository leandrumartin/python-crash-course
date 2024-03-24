# This program shows how to make dictionaries in a list.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

print('\n')

# Let's see a more realistic example with more than 3 aliens, with code that automatically generates them. Let's make a fleet of 30 aliens.

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Now, even though all of the aliens have the same properties, they are all separate objects in Python.
# Let's use this fact to say the aliens will change color. Let's change the color of the first three aliens.
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")