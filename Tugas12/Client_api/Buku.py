import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__kodeBuku = None
        self.__judul = None
        self.__kodeKategori = None
        self.__penulis = None
        self.__penerbit = None
        self.__tahun = None
        self.__url = "http://localhost/MYLIBRARY/buku_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodeBuku(self):
        return self.__kodeBuku
        
    @kodeBuku.setter
    def kodeBuku(self, value):
        self.__kodeBuku = value
    @property
    def judul(self):
        return self.__judul
        
    @judul.setter
    def judul(self, value):
        self.__judul = value
    @property
    def kodeKategori(self):
        return self.__kodeKategori
        
    @kodeKategori.setter
    def kodeKategori(self, value):
        self.__kodeKategori = value
    @property
    def penulis(self):
        return self.__penulis
        
    @penulis.setter
    def penulis(self, value):
        self.__penulis = value
    @property
    def penerbit(self):
        return self.__penerbit
        
    @penerbit.setter
    def penerbit(self, value):
        self.__penerbit = value
    @property
    def tahun(self):
        return self.__tahun
        
    @tahun.setter
    def tahun(self, value):
        self.__tahun = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodeBuku(self, kodeBuku):
        url = self.__url+"?kodeBuku="+kodeBuku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idBuku']
            self.__kodeBuku = item['kodeBuku']
            self.__judul = item['judul']
            self.__kodeKategori = item['kodeKategori']
            self.__penulis = item['penulis']
            self.__penerbit = item['penerbit']
            self.__tahun = item['tahun']
        return data
    def simpan(self):
        payload = {
            "kodeBuku":self.__kodeBuku,
            "judul":self.__judul,
            "kodeKategori":self.__kodeKategori,
            "penulis":self.__penulis,
            "penerbit":self.__penerbit,
            "tahun":self.__tahun
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodeBuku(self, kodeBuku):
        url = self.__url+"?kodeBuku="+kodeBuku
        payload = {
            "kodeBuku":self.__kodeBuku,
            "judul":self.__judul,
            "kodeKategori":self.__kodeKategori,
            "penulis":self.__penulis,
            "penerbit":self.__penerbit,
            "tahun":self.__tahun
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodeBuku(self,kodeBuku):
        url = self.__url+"?kodeBuku="+kodeBuku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text