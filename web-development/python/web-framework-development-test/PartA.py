
import random


class Artist:
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        self.albums = []    
        self.songs = []
        
    def display_info(self):
        print("Artist name is:", self.name)
        print("Date of birth is:", self.dob)
        print("Country:", self.country)
        print("Albums made:")
        for album in self.albums:
            print(" , ", album.title)
        print("Songs made:")
        for song in self.songs:
            print(" , ", song.title)
        print("-"*40)
    
    def add_album(self,album):
        self.albums.append(album)
    
    def add_song(self,song):
        self.songs.append(song)
        



class Album:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year
        self.songs = [] 
        
    def add_song(self,title,year):
        new_song=Song(title,self.artist_name,year)
        self.songs.append(new_song)
        return new_song
    
    
    def display_info(self):
        print("Title of album:", self.title)
        print("Artist that made it:", self.artist_name)
        print("Year it was released:", self.year)
        print("Songs in the album:")
        for song in self.songs:
            print("  -", song.title, "(", song.year, ")")
        print("_" * 40)

    
class Song:
    def __init__(self, title,artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year
        
    def display_info(self):
        print("Title of song:", self.title)
        print("Artist that made it:", self.artist_name)
        print("Year it was released:", self.year)
        print("_" * 40)



class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = [] 
        
    def add_song(self, song):
        self.songs.append(song)
        
    
    def print_all_songs(self):
        print("Name of Playlisy:", self.title)
        if not self.songs:
            print("No songs found")
        else:
            """index list"""
            for i, song in enumerate(self.songs, start=1):
                print(f"{i}.{song.title}-{song.artist_name}({song.year})")
        print("_" * 40)
    
    def shuffle_playlist(self):
        random.shuffle(self.songs)



    def sort_playlist(self, order="ASC"):
        self.songs.sort(key=lambda s: s.title)
        if order == "DES":
            self.songs.reverse()
            
            
if __name__ == "__main__":
    taylor = Artist("Taylor Swift", "1989-12-13", "USA")
    
    fearlessalbum = Album("Fearless", taylor.name, 2008)
    album1989 = Album("1989", taylor.name, 2014)
    
    lovestorysong = Song("Love Story", taylor.name, 2008)
    youbelongsong = Song("You Belong With Me", taylor.name, 2008)
    spaceblanksong = Song("Blank Space", taylor.name, 2014)
    stylesong = Song("Style", taylor.name, 2014)
    
    taylor.add_album(fearlessalbum)
    taylor.add_album(album1989)

    taylor.add_song(lovestorysong)
    taylor.add_song(youbelongsong)
    taylor.add_song(spaceblanksong)
    taylor.add_song(stylesong)
    fearlessalbum.songs.append(lovestorysong)
    fearlessalbum.songs.append(youbelongsong)

    album1989.songs.append(spaceblanksong)
    album1989.songs.append(stylesong)
    taylor.display_info()
    fearlessalbum.display_info()
    album1989.display_info()
    lovestorysong.display_info()
    
    playlist = Playlist("Taylor Swift Albums and Songs")
    for s in fearlessalbum.songs:
        playlist.add_song(s)
    for s in album1989.songs:
        playlist.add_song(s)
        
    print("Songs in playlist:")
    playlist.print_all_songs()

    playlist.sort_playlist(order="ASC")
    print("Playlist sorted in ascending order:")
    playlist.print_all_songs()
    
    
    playlist.sort_playlist(order="DES")
    print("Playlist sorted in descending order")
    playlist.print_all_songs()



    playlist.shuffle_playlist()
    print("Playlist after shuffling:")
    playlist.print_all_songs()


