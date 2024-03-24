players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

# it starts at the beginning and ends at the end if you remove one of the indices
print(players[:4])
print(players[2:])

# this prints the last three items
print(players[-3:])

# adding a third value will tell Python how many items to skip between items
print(players[0:5:2])

# you can still omit one or both of the first two indices if you add the third
print(players[::2])

print('\n')

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())