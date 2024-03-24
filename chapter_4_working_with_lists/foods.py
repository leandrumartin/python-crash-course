# How to copy a list into another one
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# showing that they are two different lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print('\n\n')

# The following does NOT work for copying a list--one will change with the other and they are not really separate
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Therefore, to copy one list into another, use a slice!