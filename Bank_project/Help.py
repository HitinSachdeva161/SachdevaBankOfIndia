from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql.cursors
from datetime import date
from datetime import datetime
#from pip._vendor.rich.prompt import password
class about: 
    #password1=""
    def __init__(self):
        self.root=Tk()
        self.root.geometry('800x500+300+0')     
        self.root.title("About")
        self.root.config(background='#51b9fa')
        
        self.ll2=Label(self.root,text="About the Software",background='white',font=("Century Schoolbook", 20,'bold'))
        self.ll2.pack(pady=5)
        
        self.l1=Label(self.root,text='',background='#83cdfb',font=("Century Schoolbook", 12))
        ad="This software was developed by Hitin Sachdeva \n This software was developed for employees of bank so that they can manage customers\nThis software is running through ussage of sbibank Database \n which further consists of tables named as tblaccount, tbltransaction that holds customers data in backend \n and  tbladmin which holds data of login credentials of admin.\n \n Contact Developer for Help at :- hitinsachdeva12@gmail.com"
        self.l1.config(text=ad)
        self.l1.pack(pady=10)
        
        self.b1=Button(self.root,text="Back",command=self.bk)
        self.b1.pack()
        self.root.mainloop()
        
    def bk(self):
        self.root.destroy()
        from home_pg import Mn
        Mn()
        
#q=about()