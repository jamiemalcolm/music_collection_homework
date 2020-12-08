import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album("Graduation", "Hip-Hop", "Kanye West")

    def test_album_has_title(self):
        self.assertEqual("Graduation", self.album.title)
    
    def test_album_has_genre(self):
        self.assertEqual("Hip-Hop", self.album.genre)
    

    def test_album_has_artist(self):
        self.assertEqual("Kanye West", self.album.artist)