print('\nAghisna Baihaqi\n210511034\nTI21A(R1)\n')
from playsound import playsound

class hewan:
    def __init__(self,hewan):
        self.hewan = hewan
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')

class anjing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\Punya Aghis\Materi Kuliah\PBO2\Pertemuan3\Tugas3\sound\hewan_anjing.mp3")

class ayam(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\Punya Aghis\Materi Kuliah\PBO2\Pertemuan3\Tugas3\sound\hewan_ayam.mp3")

class babi(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\Punya Aghis\Materi Kuliah\PBO2\Pertemuan3\Tugas3\sound\hewan_babi.mp3")

class bebek(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\Punya Aghis\Materi Kuliah\PBO2\Pertemuan3\Tugas3\sound\hewan_bebek.mp3")

class burunghantu(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\Punya Aghis\Materi Kuliah\PBO2\Pertemuan3\Tugas3\sound\hewan_burunghantu.mp3")

class kambing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\Punya Aghis\Materi Kuliah\PBO2\Pertemuan3\Tugas3\sound\hewan_kambing.mp3")

class kucing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\Punya Aghis\Materi Kuliah\PBO2\Pertemuan3\Tugas3\sound\hewan_kucing.mp3")

class kuda(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\Punya Aghis\Materi Kuliah\PBO2\Pertemuan3\Tugas3\sound\hewan_kuda.mp3")

class sapi(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\Punya Aghis\Materi Kuliah\PBO2\Pertemuan3\Tugas3\sound\hewan_sapi.mp3")

class serigala(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("E:\Punya Aghis\Materi Kuliah\PBO2\Pertemuan3\Tugas3\sound\hewan_serigala(2).mp3")

def hewan_bersuara(hewan):
    hewan.bersuara()

hewan0 = hewan('Hewan')
hewan1 = anjing('Anjing')
hewan2 = ayam('Ayam')
hewan3 = babi('Babi')
hewan4 = bebek('Bebek')
hewan5 = burunghantu('Burung Hantu')
hewan6 = kambing('Kambing')
hewan7 = kucing('Kucing')
hewan8 = kuda('Kuda')
hewan9 = sapi('Sapi')
hewan10 = serigala('Serigala')

hewan_bersuara(hewan0)
hewan_bersuara(hewan1)
hewan_bersuara(hewan2)
hewan_bersuara(hewan3)
hewan_bersuara(hewan4)
hewan_bersuara(hewan5)
hewan_bersuara(hewan6)
hewan_bersuara(hewan7)
hewan_bersuara(hewan8)
hewan_bersuara(hewan9)
hewan_bersuara(hewan10)
