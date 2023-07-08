import requests
import json
class Kategori:
    def __init__(self):
        self.__id=None
        self.__kodeKategori = None
        self.__namaKategori = None
        self.__url = "http://localhost/MYLIBRARY/kategori_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodeKategori(self):
        return self.__kodeKategori
        
    @kodeKategori.setter
    def kodeKategori(self, value):
        self.__kodeKategori = value
    @property
    def namaKategori(self):
        return self.__namaKategori
        
    @namaKategori.setter
    def namaKategori(self, value):
        self.__namaKategori = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodeKategori(self, kodeKategori):
        url = self.__url+"?kodeKategori="+kodeKategori
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idKategori']
            self.__kodeKategori = item['kodeKategori']
            self.__namaKategori = item['namaKategori']
        return data
    def simpan(self):
        payload = {
            "kodeKategori":self.__kodeKategori,
            "namaKategori":self.__namaKategori
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodeKategori(self, kodeKategori):
        url = self.__url+"?kodeKategori="+kodeKategori
        payload = {
            "kodeKategori":self.__kodeKategori,
            "namaKategori":self.__namaKategori
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodeKategori(self,kodeKategori):
        url = self.__url+"?kodeKategori="+kodeKategori
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text