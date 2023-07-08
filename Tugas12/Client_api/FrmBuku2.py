import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import *
class FrmBuku2:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("600x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE BUKU:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUDUL:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE KATEGORI:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENULIS:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENERBIT:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TAHUN:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKodeBuku = Entry(mainFrame) 
        self.txtKodeBuku.grid(row=0, column=1, padx=5, pady=5)
        self.txtKodeBuku.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtJudul = Entry(mainFrame) 
        self.txtJudul.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodeKategori = Entry(mainFrame) 
        self.txtKodeKategori.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenulis = Entry(mainFrame) 
        self.txtPenulis.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenerbit = Entry(mainFrame) 
        self.txtPenerbit.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtTahun = Entry(mainFrame) 
        self.txtTahun.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=6, column=3, padx=5, pady=5)
        # define columns
        columns = ('kodeBuku','judul','kodeKategori','penulis','penerbit','tahun')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('kodeBuku', text='KODEBUKU')
        self.tree.column('kodeBuku', width="100")
        self.tree.heading('judul', text='JUDUL')
        self.tree.column('judul', width="130")
        self.tree.heading('kodeKategori', text='KODEKATEGORI')
        self.tree.column('kodeKategori', width="100")
        self.tree.heading('penulis', text='PENULIS')
        self.tree.column('penulis', width="100")
        self.tree.heading('penerbit', text='PENERBIT')
        self.tree.column('penerbit', width="100")
        self.tree.heading('tahun', text='TAHUN')
        self.tree.column('tahun', width="50")
        # set tree position
        self.tree.place(x=0, y=230)
        
    def onClear(self, event=None):
        self.txtKodeBuku.delete(0,END)
        self.txtKodeBuku.insert(END,"")
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,"")
        self.txtKodeKategori.delete(0,END)
        self.txtKodeKategori.insert(END,"")
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,"")
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,"")
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,"")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        obj = Buku()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["kodeBuku"],d["judul"],d["kodeKategori"],d["penulis"],d["penerbit"],d["tahun"]))
    def onCari(self, event=None):
        kodeBuku = self.txtKodeBuku.get()
        obj = Buku()
        a = obj.get_by_kodeBuku(kodeBuku)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kodeBuku = self.txtKodeBuku.get()
        obj = Buku()
        res = obj.get_by_kodeBuku(kodeBuku)
        self.txtKodeBuku.delete(0,END)
        self.txtKodeBuku.insert(END,obj.kodeBuku)
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,obj.judul)
        self.txtKodeKategori.delete(0,END)
        self.txtKodeKategori.insert(END,obj.kodeKategori)
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,obj.penulis)
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,obj.penerbit)
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,obj.tahun)
                            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmBuku2(root2, "Aplikasi Data Buku")
    root2.mainloop()