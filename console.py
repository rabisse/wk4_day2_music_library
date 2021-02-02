import pdb

from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()


artist_1 = Artist("Alex")
artist_repository.save(artist_1)

artist_1.name = "John"
artist_repository.update(artist_1)

artist_2 = Artist("David")
artist_repository.save(artist_2)

# print(artist_repository.select(artist_1.id))
# print(artist_repository.select_all())

album_1 = Album("My Debut Album", "Hard Coding", artist_1)
album_repository.save(album_1)

album_1.title = "New Album Title"
album_repository.update(album_1)

print(artist_repository.select(artist_2.id).name)
artist_repository.delete(artist_2.id)


pdb.set_trace()
