print('Aghisna Baihaqi\n210511034\nT121A(R1)\n')

class Song:
    def __init__(self, *song):
        self.song = song[0]

    def display(self):
        print(self.song)

class Album:
    def __init__(self, *idol_album):
        self.idol_album = idol_album[0]
        self.songs = []

    def add(self, lagu):
        self.songs.append(lagu)

    def remove(self, lagu):
        self.songs.remove(lagu)

    def display(self):
        print(f"="*50,'\n',self.idol_album)
        print("="*50)
        for lagu in self.songs:
            lagu.display()

if __name__ == "__main__":
    idol = Album("\t\t\tEXO\t\t\t")
    album = Album("Album\t: Don't Fight The Feeling")
    song1 = Song(" Songs\t: Don't Fight The Feeling")
    song2 = Song("\t  Paradise")
    song3 = Song("\t  No Matter")
    song4 = Song("\t  Runaway")
    song5 = Song("\t  Just As Usual\n")
    album2 = Album("Album\t: Love Shot")
    song1_album2 = Song(" Songs\t: Love Shot")
    song2_album2 = Song("\t  Love Shot (Chinese Version)")
    song3_album2 = Song("\t  Trauma")
    song4_album2 = Song("\t  Wait\n")

    album.add(song1)
    album.add(song2)
    album.add(song3)
    album.add(song4)
    album.add(song5)
    album2.add(song1_album2)
    album2.add(song2_album2)
    album2.add(song3_album2)
    album2.add(song4_album2)

    idol.add(album)
    idol.add(album2)
    idol.display()


