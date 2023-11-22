from tkinter import *
from PIL import Image,ImageTk
import pymysql.cursors
from tkinter import messagebox
import forget
#import home_pg
#from progress import pro
class ln:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('800x500+300+0')
        self.root.config(background='#83cdfb')
        #img=Image.open('E:\eclipse\work_eclipse\Bank_project\images\Login.png')
        #i2=img.resize((500,120))
        #self.iz1=ImageTk.PhotoImage(i2)
        #self.l1=Label(self.root)
        #self.l1.config(image=self.iz1)#,background='#83cdfb')
        
        #self.l1.pack()
        self.l11=Label(self.root,text='User Id-',font=("Georgia",12,'bold'), bg="#83cdfb")
        
        self.l2=Label(self.root,text='Password-',font=("Georgia",12,'bold'), bg="#83cdfb")
        self.t1=Entry(self.root)
        self.t2=Entry(self.root,show='*')
        self.l11.place(x=220,y=200)
        self.l2.place(x=220,y=280)
        self.t1.place(x=420,y=200)
        self.t2.place(x=420,y=280)
        self.b1=Button(self.root,text='Login',width=10,command=self.fnc)
        self.b1.place(x=220,y=400)
        self.b2=Button(self.root,text='Forgot password',command=self.reset)
        self.b2.place(x=420,y=400)
        self.raju='HelooIIII'
        
        
        self.root.mainloop()
     
    def fnc(self):
        
        #self.info=str(self.t1.get())
        #print(self.info)
        
        conn=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn.cursor()
        a=str(self.t1.get())
        b=str(self.t2.get())
        cursor.execute("select * from tbladmin where admid=%s and admpwd=%s",(a,b))
        conn.commit()
        rows=cursor.rowcount
        if rows>0:
            messagebox.showinfo("Login successful", "WELCOME SIR/MADAM")
            self.root.destroy()
            from home_pg import Mn
            Mn()
    
        else:
            messagebox.showerror("Login Failed", "Invalid User ID/Password")
        conn.close()

    def reset(self):
        self.root.destroy()
        obl=forget.forg()     
           
    def nakli(self):
        self.info2=str(self.t1.get())   
        

#ob=ln()     
