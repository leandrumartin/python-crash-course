def make_album(artist, title, songs_number=None):
	album = {'artist': artist.title(), 'title': title.title()}
	if songs_number:
		album['number of songs'] = songs_number
	return album

print(make_album('bob jimbo', 'epic sauce'))
print(make_album('cool jim', 'orangeee', 10))