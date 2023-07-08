import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import *
class FrmAnggota:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("500x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE ANGGOTA:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='BERGABUNG:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKodeAnggota = Entry(mainFrame) 
        self.txtKodeAnggota.grid(row=0, column=1, padx=5, pady=5)
        self.txtKodeAnggota.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtBergabung = Entry(mainFrame) 
        self.txtBergabung.grid(row=3, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('kodeAnggota','nama','alamat','bergabung')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('kodeAnggota', text='KODEANGGOTA')
        self.tree.column('kodeAnggota', width="100")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="120")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="150")
        self.tree.heading('bergabung', text='BERGABUNG')
        self.tree.column('bergabung', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKodeAnggota.delete(0,END)
        self.txtKodeAnggota.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.txtBergabung.delete(0,END)
        self.txtBergabung.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data anggota
        obj = Anggota()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["kodeAnggota"],d["nama"],d["alamat"],d["bergabung"]))
    def onCari(self, event=None):
        kodeAnggota = self.txtKodeAnggota.get()
        obj = Anggota()
        a = obj.get_by_kodeAnggota(kodeAnggota)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kodeAnggota = self.txtKodeAnggota.get()
        obj = Anggota()
        res = obj.get_by_kodeAnggota(kodeAnggota)
        self.txtKodeAnggota.delete(0,END)
        self.txtKodeAnggota.insert(END,obj.kodeAnggota)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.txtBergabung.delete(0,END)
        self.txtBergabung.insert(END,obj.bergabung)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kodeAnggota = self.txtKodeAnggota.get()
        nama = self.txtNama.get()
        alamat = self.txtAlamat.get()
        bergabung = self.txtBergabung.get()
        # create new Object
        obj = Anggota()
        obj.kodeAnggota = kodeAnggota
        obj.nama = nama
        obj.alamat = alamat
        obj.bergabung = bergabung
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kodeAnggota(kodeAnggota)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kodeAnggota = self.txtKodeAnggota.get()
        obj = Anggota()
        obj.kodeAnggota = kodeAnggota
        if(self.ditemukan==True):
            res = obj.delete_by_kodeAnggota(kodeAnggota)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmAnggota(root2, "Aplikasi Data Anggota")
    root2.mainloop()