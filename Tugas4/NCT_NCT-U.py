print('Aghisna Baihaqi\n210511034\nT121A(R1)\n')

class Nct:
    def __init__(self,member=None):
        if member is None:
            self.member = []
        else:
            self.member = member

    def add_member(self,nct_member):
        self.member.append(nct_member)

    def daftar_member(self):
        print('\t\tDaftar Member\t\t')
        print('\t','='*27,'\t')
        for nct_member in self.member:
            print(f'Name\t\t: ',nct_member.name)
            print(f'Unit\t\t: ',nct_member.unit)

class Nct_member:
    def __init__(self,name,unit):
        self.name = name
        self.unit = unit

    def get_name(self):
        return self.name

    def get_unit(self):
        return self.unit
    
class Comeback:
    def __init__(self,comeback,title,song,Nct):
        self.comeback = comeback
        self.title = title
        self.song = song
        self.Nct = Nct

    def tampil(self):
        print(f'Comeback\t: {self.comeback}')
        print(f'Album\t\t: {self.title}')
        print(f'Song\t\t: {self.song}\n')

member1 = Nct_member('Taeyong', 'NCT-127\n')
member2 = Nct_member('Doyoung', 'NCT-127\n')
member3 = Nct_member('Jaehyun', 'NCT-127\n')
member4 = Nct_member('Lucas', 'WayV\n')
member5 = Nct_member('Xiaojun', 'WayV\n')
member6 = Nct_member('Jaemin', 'NCT-Dream\n')
member7 = Nct_member('Shotaro', '-\n')
nct_2020 = Nct([member1, member2, member3, member4, member5, member6, member7])
nct_comeback = Comeback('NCT-U 2020', 'NCT RESONANCE Pt.1', 'Make A Wish', nct_2020)
nct_comeback.Nct.member
nct_comeback.tampil()
nct_comeback.Nct.daftar_member()
