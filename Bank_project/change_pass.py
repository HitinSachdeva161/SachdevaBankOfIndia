from tkinter import *
from tkinter import messagebox
import pymysql.cursors
class chp: 
    password1=""
    def __init__(self):
        self.root=Tk()
        self.root.geometry('800x500+300+0')     #
        self.root.title("Change Password")
        self.root.config(background='#51b9fa')
        self.x1=Label(self.root,text='Change Password',font=("Arial", 30,'bold'))
        self.x1.pack(pady=5)
        self.ll2=Label(self.root,text="Enter Admin Id-",background='#51b9fa',font=("Century Schoolbook", 10,'bold'))
        self.ll2.place(relx=0.21,rely=0.21,anchor="sw")
        self.e1=Entry(self.root)
        self.e1.place(relx=0.51,rely=0.21,anchor="sw")
        self.f2=Frame(self.root,height=400,width=700,background='#83cdfb')
        
        self.b1=Button(self.root,text="Show",command=self.qry)
        self.b1.place(relx=0.8,rely=0.21,anchor="sw")
        
        self.l1=Label(self.f2,text='Current Password',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l2=Label(self.f2,text='New Password',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        
        self.t1=Entry(self.f2,show="*")#ac
        self.t2=Entry(self.f2,show="*")#nm
        
      
        self.l1.grid(row=0,column=0,padx=100,pady=10)
        self.l2.grid(row=1,column=0,pady=10)
        
        self.t1.grid(row=0,column=3,padx=100,pady=10)
        self.t2.grid(row=1,column=3,pady=10)
        
        self.b3=Button(self.f2,text="Ok",command=self.up,width=6)
        self.b3.grid(row=8,column=1,columnspan=2)
        self.b2=Button(self.f2,text="Back",command=self.bk,width=6)
        self.b2.grid(row=8,column=3,columnspan=2)
        
        self.root.mainloop()

    def qry(self):
        val=self.e1.get()
        conn=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn.cursor()
        cursor.execute("select admpwd from tbladmin where admid=%s",(val))
        conn.commit()
        rows=cursor.rowcount
        
        if rows>0:
            self.f2.place(relx=0.0701,rely=0.3,relwidth=0.8)
            for row in cursor:
                #print(row[3])
                global password1 
                password1 = row[0]
                self.e1.config(state='disabled')
                
                
        else:
            messagebox.showerror("Error", "Invalid Admin Id")
            self.root.destroy()
            from home_pg import Mn
            op=Mn()
     
        conn.close()
    def up(self):
        val=self.e1.get()
        o_admpass=self.t1.get()
        n_admpass=self.t2.get()
        global password1
        chk=password1
        if o_admpass==chk:        
            conn2=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
            cursor=conn2.cursor()
            cursor.execute("UPDATE tbladmin SET admpwd=%s WHERE admid=%s", (n_admpass,val))
            conn2.commit()
            conn2.close()
            messagebox.showinfo("Succesful","Update Operation was Succesfully")
        else:
            messagebox.showerror("Error","You entered wrong Password!")
       
    def bk(self):
        self.root.destroy()
        from home_pg import Mn
        op=Mn()
        
#obh=chp()