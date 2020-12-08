import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Kanye West")

    def test_artist_has_name(self):
        self.assertEqual("Kanye West", self.artist.name)
