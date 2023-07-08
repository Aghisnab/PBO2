import requests
import json
class Pinjam:
    def __init__(self):
        self.__id=None
        self.__kodePinjam = None
        self.__kodeAnggota = None
        self.__kodeBuku = None
        self.__tglKembali = None
        self.__url = "http://localhost/MYLIBRARY/pinjam_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodePinjam(self):
        return self.__kodePinjam
        
    @kodePinjam.setter
    def kodePinjam(self, value):
        self.__kodePinjam = value
    @property
    def kodeAnggota(self):
        return self.__kodeAnggota
        
    @kodeAnggota.setter
    def kodeAnggota(self, value):
        self.__kodeAnggota = value
    @property
    def kodeBuku(self):
        return self.__kodeBuku
        
    @kodeBuku.setter
    def kodeBuku(self, value):
        self.__kodeBuku = value
    @property
    def tglKembali(self):
        return self.__tglKembali
        
    @tglKembali.setter
    def tglKembali(self, value):
        self.__tglKembali = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodePinjam(self, kodePinjam):
        url = self.__url+"?kodePinjam="+kodePinjam
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idPinjam']
            self.__kodePinjam = item['kodePinjam']
            self.__kodeAnggota = item['kodeAnggota']
            self.__kodeBuku = item['kodeBuku']
            self.__tglKembali = item['tglKembali']
        return data
    def simpan(self):
        payload = {
            "kodePinjam":self.__kodePinjam,
            "kodeAnggota":self.__kodeAnggota,
            "kodeBuku":self.__kodeBuku,
            "tglKembali":self.__tglKembali
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodePinjam(self, kodePinjam):
        url = self.__url+"?kodePinjam="+kodePinjam
        payload = {
            "kodePinjam":self.__kodePinjam,
            "kodeAnggota":self.__kodeAnggota,
            "kodeBuku":self.__kodeBuku,
            "tglKembali":self.__tglKembali
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodePinjam(self,kodePinjam):
        url = self.__url+"?kodePinjam="+kodePinjam
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text