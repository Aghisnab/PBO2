import requests
import json
class Anggota:
    def __init__(self):
        self.__id=None
        self.__kodeAnggota = None
        self.__nama = None
        self.__alamat = None
        self.__bergabung = None
        self.__url = "http://localhost/MYLIBRARY/anggota_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodeAnggota(self):
        return self.__kodeAnggota
        
    @kodeAnggota.setter
    def kodeAnggota(self, value):
        self.__kodeAnggota = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    @property
    def bergabung(self):
        return self.__bergabung
        
    @bergabung.setter
    def bergabung(self, value):
        self.__bergabung = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodeAnggota(self, kodeAnggota):
        url = self.__url+"?kodeAnggota="+kodeAnggota
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idAnggota']
            self.__kodeAnggota = item['kodeAnggota']
            self.__nama = item['nama']
            self.__alamat = item['alamat']
            self.__bergabung = item['bergabung']
        return data
    def simpan(self):
        payload = {
            "kodeAnggota":self.__kodeAnggota,
            "nama":self.__nama,
            "alamat":self.__alamat,
            "bergabung":self.__bergabung
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodeAnggota(self, kodeAnggota):
        url = self.__url+"?kodeAnggota="+kodeAnggota
        payload = {
            "kodeAnggota":self.__kodeAnggota,
            "nama":self.__nama,
            "alamat":self.__alamat,
            "bergabung":self.__bergabung
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodeAnggota(self,kodeAnggota):
        url = self.__url+"?kodeAnggota="+kodeAnggota
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text