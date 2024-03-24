# building a list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print("\n")

# replacing a list item
motorcycles[0] = 'ducati'
print(motorcycles)

print("\n")

# resetting the list and inserting a list item
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

print("\n")

# resetting the list and deleting a list item
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

print("\n")

# resetting the list and using pop() method, which removes an item from a list and still allows you to access it
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print("\n")

# resetting the list and using pop() method for a specific list item
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycles)

print("\n")

# using the remove() method to remove an item, which lets you still work with it
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

# Use pop() when you know the index of the item. Use remove() when you only know the name of the item.
# remove() only removes the first item that matches that in the list.