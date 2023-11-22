from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql.cursors
from datetime import date
from datetime import datetime
class view: 
    def __init__(self):
        self.root=Tk()
        self.root.geometry('800x500+300+0')     
        self.root.title("View all")
        self.root.config(background='#51b9fa')
        self.head=Label(self.root,text="View All",background='white',font=("Century Schoolbook", 15,'bold'))
        self.head.pack(pady=5)
        self.b1=Button(self.root,text="Ok",command=self.okay)
        self.b1.pack()
        self.txt=Text(self.root,height=8)
        self.txt1=Text(self.root,height=8)
        self.b2=Button(self.root,text="Back",command=self.bkk)
        self.scr=Scrollbar(self.root,orient='vertical',width=20,command=self.txt.yview)
        self.scr1=Scrollbar(self.root,orient='vertical',width=20,command=self.txt1.yview)
        
        
        self.root.mainloop()
    
    def okay(self):
        self.txt.place(relx=0.1,rely=0.2)
        self.txt1.place(relx=0.1,rely=0.6)
        self.scr.place(relx=0.9,rely=0.2,relheight=0.265)
        self.scr1.place(relx=0.9,rely=0.6,relheight=0.265)
        self.txt.config(yscrollcommand = self.scr.set)
        self.b2.place(relx=0.4,rely=0.9)
        conn=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn.cursor()
        cursor.execute("select * from tbltransaction")
        conn.commit()
        rows = cursor.fetchall()
        table_data = []
        for row in rows:
                table_data.append(list(row))     
                table_string = ""
                for row in table_data:
                    table_string += "\t".join(str(col) for col in row) + "\n"
        self.txt.insert("3.0", table_string)
        self.txt.insert("1.0","id  From A/c   To A/c   type    Amt       date      time \n")
        self.txt.insert("2.0","------------------------------------------------------------------ \n")
        
        self.txt.config(state='disabled')
        conn.close()
        self.lb1=Label(self.root,text="A/c Summary",font=("Century Schoolbook", 8,'bold'))
        self.lb1.place(relx=0.45,rely=0.5)
        conn1=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn1.cursor()
        cursor.execute("select accno,cname,balance from tblaccount")
        conn1.commit()    
        self.txt1.config(state='normal')
        self.txt1.delete('1.0', END)
        msg="id"+'\t'+'name'+'\t'+'Balance'+'\n'+'------------------------'+'\n'
        for row in cursor:
            msg=msg+str(row[0])+'\t'+str(row[1])+'\t'+str(row[2])+'\n'
           
        self.txt1.insert('1.0',msg)
        self.txt1.config(state='disabled')
        
    def bkk(self):
        self.root.destroy()
        from home_pg import Mn
        Mn()     
#b=view()
        
