from tkinter import *
from PIL import Image,ImageTk
#from progress import pro
import progress
class wel1:
    def __init__(self):
        self.root=Tk()
      
        self.f1=Frame(self.root,relief=RAISED,bd=10,background='#83cdfb')
        self.f2=Frame(self.root)
        self.f2.config(bg='#056dae')
        self.root.geometry('800x500+300+0')
        self.root.config(background='#83cdfb')
        img=Image.open('E:\eclipse\work_eclipse\Bank_project\Sachdeva Bank of India.jpg')
        i2=img.resize((800,400))
        self.i1=ImageTk.PhotoImage(i2)
        self.l1=Label(self.f1)
        self.l1.config(image=self.i1, compound='center')
        self.f1.pack(side=TOP, expand=NO, fill=BOTH)
        self.b1=Button(self.f2,text='Click to continue',command=self.next)
        self.b1.pack()
        self.f2.pack(side=TOP, expand=NO, fill=BOTH)
        self.l1.pack()
        
        self.root.mainloop()
        
    def next(self):
        self.root.destroy()
        #oba=pro()
        oba=progress.pro()
        
obj=wel1()