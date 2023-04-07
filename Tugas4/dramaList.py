print('Aghisna Baihaqi\n210511034\nT121A(R1)\n')

class List_drama:
    def __init__(self,tanggal):
        self.tanggal = tanggal
        self.list = List()
    
    def tampil(self):
        print('\t\t\tDrama List\t\t\t\n','\t','='*37,'\t')
        print(f'Date\t\t:  {self.tanggal}\n')

class Drama:
    def __init__(self,judul,status,genre,tayang,pemeran):
        self.judul = judul
        self.status = status
        self.genre = genre
        self.tayang = tayang
        self.pemeran = pemeran

    def get_judul(self):
        return self.judul
    def get_status(self):
        return self.status
    def get_genre(self):
        return self.genre
    def get_tayang(self):
        return self.tayang
    def get_pemeran(self):
        return self.pemeran

class List:
    def __init__(self):
        self.kDrama = []

    def add_drama(self,drama):
        self.kDrama.append(drama)

    def daftar_drama(self):
        for drama in self.kDrama:
            print(f'Judul\t\t: ',drama.judul)
            print(f'Status\t\t: ',drama.status)
            print(f'Genre\t\t: ',drama.genre)
            print(f'Tayang\t\t: ',drama.tayang)
            print(f'Pemeran\t\t: ',drama.pemeran,'\n')

listMaret = List_drama('Maret 2023')
drakor1 = Drama('Taxi Driver Season 2', 'ON GOING', 'Action, Revenge Tragedy, Criminal', 'Jumat-Sabtu Pukul 22.00', 'Lee Je Hoon, Kim Eui Sung, Pyo Ye Jin')
drakor2 = Drama('Oasis', 'ON GOING', 'Melodrama, Coming of Age', 'Senin-Selasa Pukul 21.50', 'Jang Dong Yoon, Seol In Ah, Choo Yeong Woo')
drakor3 = Drama('The Glory Season 2', 'END', 'Revenge Tragedy', 'Jumat Pukul 15.00', 'Song Hye Kyo, Lee Do Hyun, Lim Ji Yeon')
drakor4 = Drama('The Heavenly Idol', 'END', 'Fantasy, Romance Comedy', 'Rabu-Kamis Pukul 22.30', 'Kim Min Kyu, Go Bo Gyeol, Lee Jang Woo')
listMaret.list.add_drama(drakor1)
listMaret.list.add_drama(drakor2)
listMaret.list.add_drama(drakor3)
listMaret.list.add_drama(drakor4)
listMaret.list.kDrama
listMaret.tampil()
listMaret.list.daftar_drama()