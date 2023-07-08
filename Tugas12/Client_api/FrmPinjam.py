import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pinjam import *
class FrmPinjam:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("475x475")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE PINJAM:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE ANGGOTA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE BUKU:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGL KEMBALI:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKodePinjam = Entry(mainFrame) 
        self.txtKodePinjam.grid(row=0, column=1, padx=5, pady=5)
        self.txtKodePinjam.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtKodeAnggota = Entry(mainFrame) 
        self.txtKodeAnggota.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodeBuku = Entry(mainFrame) 
        self.txtKodeBuku.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtTglKembali = Entry(mainFrame) 
        self.txtTglKembali.grid(row=3, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('kodePinjam','kodeAnggota','kodeBuku','tglKembali')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('kodePinjam', text='KODEPINJAM')
        self.tree.column('kodePinjam', width="100")
        self.tree.heading('kodeAnggota', text='KODEANGGOTA')
        self.tree.column('kodeAnggota', width="100")
        self.tree.heading('kodeBuku', text='KODEBUKU')
        self.tree.column('kodeBuku', width="100")
        self.tree.heading('tglKembali', text='TGLKEMBALI')
        self.tree.column('tglKembali', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKodePinjam.delete(0,END)
        self.txtKodePinjam.insert(END,"")
        self.txtKodeAnggota.delete(0,END)
        self.txtKodeAnggota.insert(END,"")
        self.txtKodeBuku.delete(0,END)
        self.txtKodeBuku.insert(END,"")
        self.txtTglKembali.delete(0,END)
        self.txtTglKembali.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pinjam
        obj = Pinjam()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["kodePinjam"],d["kodeAnggota"],d["kodeBuku"],d["tglKembali"]))
    def onCari(self, event=None):
        kodePinjam = self.txtKodePinjam.get()
        obj = Pinjam()
        a = obj.get_by_kodePinjam(kodePinjam)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kodePinjam = self.txtKodePinjam.get()
        obj = Pinjam()
        res = obj.get_by_kodePinjam(kodePinjam)
        self.txtKodePinjam.delete(0,END)
        self.txtKodePinjam.insert(END,obj.kodePinjam)
        self.txtKodeAnggota.delete(0,END)
        self.txtKodeAnggota.insert(END,obj.kodeAnggota)
        self.txtKodeBuku.delete(0,END)
        self.txtKodeBuku.insert(END,obj.kodeBuku)
        self.txtTglKembali.delete(0,END)
        self.txtTglKembali.insert(END,obj.tglKembali)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kodePinjam = self.txtKodePinjam.get()
        kodeAnggota = self.txtKodeAnggota.get()
        kodeBuku = self.txtKodeBuku.get()
        tglKembali = self.txtTglKembali.get()
        # create new Object
        obj = Pinjam()
        obj.kodePinjam = kodePinjam
        obj.kodeAnggota = kodeAnggota
        obj.kodeBuku = kodeBuku
        obj.tglKembali = tglKembali
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kodePinjam(kodePinjam)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kodePinjam = self.txtKodePinjam.get()
        obj = Pinjam()
        obj.kodePinjam = kodePinjam
        if(self.ditemukan==True):
            res = obj.delete_by_kodePinjam(kodePinjam)
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
    aplikasi = FrmPinjam(root2, "Aplikasi Data Pinjam")
    root2.mainloop()