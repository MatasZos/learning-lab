import unittest
from PartA import Artist, Album, Song, Playlist

class TestMusicClasses(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Taylor Swift", "1989-12-13", "USA")
        self.album = Album("Fearless", "Taylor Swift", 2008)
        self.song = Song("Love Story", "Taylor Swift", 2008)
        self.playlist = Playlist("My Playlist")

    """unit test for if an object is an instance of a class"""
    def test_artist_instance(self):
        self.assertIsInstance(self.artist, Artist)

    def test_album_instance(self):
        self.assertIsInstance(self.album, Album)

    def test_song_instance(self):
        self.assertIsInstance(self.song, Song)

    def test_playlist_instance(self):
        self.assertIsInstance(self.playlist, Playlist)

    """unit test for if an object is not an instance of a class"""
    
    def testartistnotsong(self):
        self.assertNotIsInstance(self.artist, Song)

    def testalbumnotplaylist(self):
        self.assertNotIsInstance(self.album, Playlist)

    def testsongnotartist(self):
        self.assertNotIsInstance(self.song, Artist)

    def testplaylistnotalbum(self):
        self.assertNotIsInstance(self.playlist, Album)

    """unit test for if 2 obhjects are idential, 1 for identical, 1 for not"""
    
    def test_identical_objects(self):
        a = self.song
        b = self.song
        self.assertIs(a, b)

    def test_similar_objects(self):
        a = Song("Love Story", "Taylor Swift", 2008)
        b = Song("Love Story", "Taylor Swift", 2008)
        self.assertIsNot(a, b)
        
    
    
    """unit test for if all methods work"""
    
    def test_add_song_to_album(self):
        self.album.songs.append(self.song)
        self.assertIn(self.song, self.album.songs)

    def test_add_song_to_artist(self):
        self.artist.add_song(self.song)
        self.assertIn(self.song, self.artist.songs)

    def test_add_album_to_artist(self):
        self.artist.add_album(self.album)
        self.assertIn(self.album, self.artist.albums)

    def test_add_song_to_playlist(self):
        self.playlist.add_song(self.song)
        self.assertIn(self.song, self.playlist.songs)
        
    """unit test for if sorting annd shuffle methoid works"""
    
    def test_sort_playlist_ascending(self):
        s1 = Song("B", "Taylor Swift", 2008)
        s2 = Song("A", "Taylor Swift", 2008)
        self.playlist.add_song(s1)
        self.playlist.add_song(s2)

        self.playlist.sort_playlist("ASC")
        self.assertEqual(self.playlist.songs[0].title, "A")

    def test_sort_playlist_descending(self):
        s1 = Song("A", "Taylor Swift", 2008)
        s2 = Song("B", "Taylor Swift", 2008)
        self.playlist.add_song(s1)
        self.playlist.add_song(s2)

        self.playlist.sort_playlist("DES")
        self.assertEqual(self.playlist.songs[0].title, "B")
        
    def test_shuffle_playlist(self):
        s1 = Song("A", "Taylor Swift", 2008)
        s2 = Song("B", "Taylor Swift", 2008)
        s3 = Song("C", "Taylor Swift", 2008)

        self.playlist.add_song(s1)
        self.playlist.add_song(s2)
        self.playlist.add_song(s3)

        before = self.playlist.songs.copy()
        self.playlist.shuffle_playlist()
        after = self.playlist.songs
        self.assertNotEqual(before, after)

if __name__ == "__main__":
    unittest.main()
