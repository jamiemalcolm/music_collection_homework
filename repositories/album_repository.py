from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


# SAVE
def save(album):
    sql = 'INSERT INTO albums (title, genre, artist) VALUES (%s,%s,%s) RETURNING *'
    values = [album.title, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

#  select by id 
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        album = Album(result['title'], result['genre'], result['artist'], result['id'])
    return album


# select all 
def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['title'], row['genre'], row['artist'], row['id'])
        albums.append(album)
    return albums


# delete all   
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)