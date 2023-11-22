from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql.cursors
from datetime import date
from datetime import datetime
#from pip._vendor.rich.prompt import password
class depos: 
    password1=""
    def __init__(self):
        self.root=Tk()
        self.root.geometry('800x500+300+0')     
        self.root.title("Deposit")
        self.root.config(background='#51b9fa')
        
        self.ll2=Label(self.root,text="Deposit",background='white',font=("Century Schoolbook", 15,'bold'))
        img=Image.open('E:\eclipse\work_eclipse\Bank_project\images\depositx.png')
        i2=img.resize((40,40))
        self.i1=ImageTk.PhotoImage(i2)
        self.ll2.config(image=self.i1,background='white',compound='right')
        self.ll2.pack()
        
        self.l1=Label(self.root,text="Enter A/c No.",background='#83cdfb')
        self.l2=Label(self.root,text="Amount to be deposit",background='#83cdfb')
        self.t1=Entry(self.root)
        self.t2=Entry(self.root)
        self.b1=Button(self.root,text="Deposit",command=self.qry)
        self.b2=Button(self.root,text="Back",command=self.bk)
        
        self.l1.place(relx=0.2,rely=0.2)
        self.l2.place(relx=0.2,rely=0.3)
        self.t1.place(relx=0.5,rely=0.2)
        self.t2.place(relx=0.5,rely=0.3)
        self.b1.place(relx=0.25,rely=0.5)
        self.b2.place(relx=0.6,rely=0.5)
        
        
        self.root.mainloop()
        
    def qry(self):
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        now = datetime.now()
        crt = now.strftime("%H:%M:%S")
        
        
        if self.t1.get()=="" or self.t2.get()=="" or int(self.t2.get())<0:
            messagebox.showerror("Error","Enter Valid Input")
            self.root.destroy()
            from home_pg import Mn
            op=Mn()
        else:
            acc=self.t1.get()
            dep=int(self.t2.get())
            conn=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
            cursor=conn.cursor()
            cursor.execute("SELECT balance FROM tblaccount WHERE accno=%s",(acc))
            conn.commit()
        
            rows=cursor.rowcount
            conn.close()
            for row in cursor:
                bal=int(row[0])
            #print(int(row[0]))
            if rows>0:
            #print(bal)
                bal=bal+dep
            #print(bal)
                conn1=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
                cursor=conn1.cursor() 
                cursor.execute("UPDATE tblaccount SET balance=%s WHERE accno=%s",(bal,acc))
                conn1.commit()
                conn1.close()
            #====================================================================
                conn2=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
                cursor=conn2.cursor()
                cursor.execute("select ifnull(max(transid),0)tmax from tbltransaction")
                conn2.commit()
                for row1 in cursor:
                    id=int(row1[0])
                id=id+1
            
                cursor.execute("INSERT INTO tbltransaction SET transid=%s,transsrcaccno=%s,transtype='Deposit',transamt=%s,transdate=%s,transtime=%s",(id,acc,dep,d1,crt))
                conn2.commit()
                conn2.close()
                messagebox.showinfo("Successful","Transaction Completed")
            
            else:
                messagebox.showerror("Error","No A/c Found")
    def bk(self):
        self.root.destroy()
        from home_pg import Mn
        op=Mn()        
        
#ob=depos()
