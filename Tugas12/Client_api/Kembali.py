import requests
import json
class Kembali:
    def __init__(self):
        self.__id=None
        self.__kodeKembali = None
        self.__kodeAnggota = None
        self.__kodePinjam = None
        self.__kodeBuku = None
        self.__tglDikembalikan = None
        self.__denda = None
        self.__url = "http://localhost/MYLIBRARY/kembali_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodeKembali(self):
        return self.__kodeKembali
        
    @kodeKembali.setter
    def kodeKembali(self, value):
        self.__kodeKembali = value
    @property
    def kodeAnggota(self):
        return self.__kodeAnggota
        
    @kodeAnggota.setter
    def kodeAnggota(self, value):
        self.__kodeAnggota = value
    @property
    def kodePinjam(self):
        return self.__kodePinjam
        
    @kodePinjam.setter
    def kodePinjam(self, value):
        self.__kodePinjam = value
    @property
    def kodeBuku(self):
        return self.__kodeBuku
        
    @kodeBuku.setter
    def kodeBuku(self, value):
        self.__kodeBuku = value
    @property
    def tglDikembalikan(self):
        return self.__tglDikembalikan
        
    @tglDikembalikan.setter
    def tglDikembalikan(self, value):
        self.__tglDikembalikan = value
    @property
    def denda(self):
        return self.__denda
        
    @denda.setter
    def denda(self, value):
        self.__denda = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodeKembali(self, kodeKembali):
        url = self.__url+"?kodeKembali="+kodeKembali
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idKembali']
            self.__kodeKembali = item['kodeKembali']
            self.__kodeAnggota = item['kodeAnggota']
            self.__kodePinjam = item['kodePinjam']
            self.__kodeBuku = item['kodeBuku']
            self.__tglDikembalikan = item['tglDikembalikan']
            self.__denda = item['denda']
        return data
    def simpan(self):
        payload = {
            "kodeKembali":self.__kodeKembali,
            "kodeAnggota":self.__kodeAnggota,
            "kodePinjam":self.__kodePinjam,
            "kodeBuku":self.__kodeBuku,
            "tglDikembalikan":self.__tglDikembalikan,
            "denda":self.__denda
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodeKembali(self, kodeKembali):
        url = self.__url+"?kodeKembali="+kodeKembali
        payload = {
            "kodeKembali":self.__kodeKembali,
            "kodeAnggota":self.__kodeAnggota,
            "kodePinjam":self.__kodePinjam,
            "kodeBuku":self.__kodeBuku,
            "tglDikembalikan":self.__tglDikembalikan,
            "denda":self.__denda
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodeKembali(self,kodeKembali):
        url = self.__url+"?kodeKembali="+kodeKembali
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text