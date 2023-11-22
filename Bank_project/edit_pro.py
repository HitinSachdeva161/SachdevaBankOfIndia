from tkinter import *
from tkinter import messagebox
import pymysql.cursors
class edp: 
    def __init__(self):
        self.root=Tk()
        self.root.geometry('800x500+300+0')     #
        self.root.title("Edit Profile")
        self.root.config(background='#51b9fa')
        self.x1=Label(self.root,text='Edit Profile',font=("Arial", 30,'bold'))
        self.x1.pack(pady=5)
        self.ll2=Label(self.root,text="Enter Admin Id-",background='#51b9fa',font=("Century Schoolbook", 10,'bold'))
        self.ll2.place(relx=0.21,rely=0.21,anchor="sw")
        self.e1=Entry(self.root)
        self.e1.place(relx=0.51,rely=0.21,anchor="sw")
        self.f2=Frame(self.root,height=400,width=700,background='#83cdfb')
        
        self.b1=Button(self.root,text="Show",command=self.qry)
        self.b1.place(relx=0.8,rely=0.21,anchor="sw")
        
        self.l1=Label(self.f2,text='Name',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l2=Label(self.f2,text='Address',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l3=Label(self.f2,text='Email',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l4=Label(self.f2,text='Mobile No.',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        
        self.t1=Entry(self.f2)#ac
        self.t2=Entry(self.f2)#nm
        self.t3=Entry(self.f2)#ad
        self.t4=Entry(self.f2)#mb
        
      
        self.l1.grid(row=0,column=0,padx=100,pady=10)
        self.l2.grid(row=1,column=0,pady=10)
        self.l3.grid(row=2,column=0,pady=10)
        self.l4.grid(row=3,column=0,pady=10)
        
        self.t1.grid(row=0,column=3,padx=100,pady=10)
        self.t2.grid(row=1,column=3,pady=10)
        self.t3.grid(row=2,column=3,pady=10)
        self.t4.grid(row=3,column=3,pady=10)
        
        self.b3=Button(self.f2,text="Update",command=self.up,width=6)
        self.b3.grid(row=8,column=2,columnspan=2,stick="w")
        self.b2=Button(self.f2,text="Back",command=self.bk,width=6)
        self.b2.grid(row=8,column=4,columnspan=2,stick="w")
        self.zom()
        
        self.root.mainloop()

    def qry(self):
        val=self.e1.get()
        conn=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn.cursor()
        cursor.execute("select admname,admadd,admemail,admphno from tbladmin where admid=%s",(val))
        conn.commit()
        rows=cursor.rowcount
        
        if rows>0:
            self.f2.place(relx=0.0701,rely=0.3,relwidth=0.8)
            for row in cursor:
                #print(row[3])
                self.t1.insert(0,str(row[0]))
                self.t2.insert(0,str(row[1]))
                self.t3.insert(0,str(row[2]))
                self.t4.insert(0,str(row[3]))
                
                self.e1.config(state='disabled')
                
                
        else:
            messagebox.showerror("Error", "Invalid Admin ID")
            self.root.destroy()
            from home_pg import Mn
            op=Mn()
     
        conn.close()
    def up(self):
        val=self.e1.get()
        admname=self.t1.get()
        admadd=self.t2.get()
        admemail=self.t3.get()     
        admphno=self.t4.get()
        if len(admphno)!=10:
            messagebox.showerror("Error", "Enter valid values")
        else:        
            conn2=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
            cursor=conn2.cursor()
            cursor.execute("UPDATE tbladmin SET admname=%s,admadd=%s,admemail=%s,admphno=%s WHERE admid=%s", (admname,admadd,admemail,admphno,val))
            conn2.commit()
            conn2.close()
            messagebox.showinfo("Succesful","Update Operation was Succesfully")
       
    def bk(self):
        self.root.destroy()
        from home_pg import Mn
        op=Mn()
        
    def zom(self):
        from login import ln
        obk=ln()
        
        #print(self.obk.fnc.info)
        print(obk.raju)
        
        #print(obk.a)
        da=ln()
        da.nakli()
        #obk.nakli()
        as1=str(da.info2)
        print(as1)
        #print(obk.info)
        
#obh=edp()