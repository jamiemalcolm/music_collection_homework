import pdb
from models.artist import Artist
import repositories.artist_repository as artist_repository
from models.album import Album
import repositories.album_repository as album_repository




artist_1 = Artist("Kanye West")
artist_repository.save(artist_1)

artist_2 = Artist("Jay-Z")
artist_repository.save(artist_2)

album_1 = Album("Graduation", "Hip-Hop", "Kanye West")
album_repository.save(album_1)

album_2 = Album("Graduation", "Hip-Hop", "Kanye East")
album_repository.save(album_2)

check_1 = album_repository.select(1)

# album_repository.delete_all()