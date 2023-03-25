print('\nMultilevel Inheritance_AGENSI\n')

class Agensi:
   def __init__(self,agensi):
     self.agensi = agensi

   def get_agensi(self):
     return self.agensi

class Grup(Agensi):
   def __init__(self,agensi,grup):
     Agensi.__init__(self,agensi)
     self.grup = grup

   def get_grup(self):
     return self.grup

class Idol(Grup):
   def __init__(self,agensi,grup,idol):
     Grup.__init__(self,agensi,grup)
     self.idol = idol

   def get_idol(self):
     return self.idol

gc = Idol("SMENT","EX0","CHANYEOL\n")
print('Agensi: ',gc.get_agensi())
print('Grup: ',gc.get_grup())
print('Idol: ',gc.get_idol())

gc1 = Idol("SMENT","AESPA","WINTER\n")
print('Agensi: ',gc1.get_agensi())
print('Grup: ',gc1.get_grup())
print('Idol: ',gc1.get_idol())