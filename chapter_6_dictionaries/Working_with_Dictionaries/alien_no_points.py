# Let's see what happens when we ask for a value that doesn't exist.
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

# This is the same thing, but uses the get() method to set a default value to be returned if the requested key doesn't exist.
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# If there's any chance that the key you're asking for might not exist, use the get() method instead of the square bracket notation.