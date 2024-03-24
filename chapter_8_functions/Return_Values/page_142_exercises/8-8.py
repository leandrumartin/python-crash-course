def make_album(artist, title, songs_number=None):
	album = {'artist': artist.title(), 'title': title.title()}
	if songs_number:
		album['number of songs'] = songs_number
	return album

while True:
	print("\nLet's make an album!")
	print("(enter 'q' at any time to quit)")
	
	artist = input("Artist: ")
	if artist == 'q':
		break

	title = input('Title: ')
	if title == 'q':
		break
	
	songs_number = input('Number of songs (optional): ')
	if songs_number == 'q':
		break
	
	print(make_album(artist, title, songs_number))