from tkinter import *
import pymysql.cursors
from tkinter import messagebox
from datetime import date
#from home_pg import Mn
class opn:
    def __init__(self):
        
        self.root=Tk()
        self.root.title("Create New Account")
        self.root.geometry('800x500+300+0')
        self.root.config(background='#51b9fa')
        self.fnan2=Frame(self.root,background='black',height=5,width=2000)
        self.fnan2.pack()
        today = date.today()
        d1 = today.strftime("%d-%m-%Y")
        v = StringVar()
        v.set(str(d1))
        self.lb=Label(self.root,text="Create New Account",font=("Arial", 30,'bold'))
        self.lb.pack(fill=BOTH)
        self.fnan=Frame(self.root,background='black',height=5,width=2000)
        self.fnan.pack()
        
        self.f2=Frame(self.root,background='#83cdfb')
        self.f2.place(relx=0.051,rely=0.21,relheight=1,relwidth=0.9)
        
        self.l1=Label(self.f2,text='A/c No',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l2=Label(self.f2,text='Customer Name',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l3=Label(self.f2,text='Address',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l4=Label(self.f2,text='Mobile No.',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l5=Label(self.f2,text='Gender',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l6=Label(self.f2,text='Date',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l7=Label(self.f2,text='Balance',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        
        self.t1=Entry(self.f2)
        self.t2=Entry(self.f2)
        self.t3=Entry(self.f2)
        self.t4=Entry(self.f2)
        self.t6=Entry(self.f2,text=v)
        self.t6.config(state='disabled')
        self.t7=Entry(self.f2)
      
        self.l1.grid(row=0,column=0,padx=100,pady=10)
        self.l2.grid(row=1,column=0,pady=10)
        self.l3.grid(row=2,column=0,pady=10)
        self.l4.grid(row=3,column=0,pady=10)
        self.l5.grid(row=4,column=0,pady=10)
        self.l6.grid(row=5,column=0,pady=10)
        self.l7.grid(row=6,column=0,pady=10)
        
        self.t1.grid(row=0,column=3,padx=100,pady=10)
        self.t2.grid(row=1,column=3,pady=10)
        self.t3.grid(row=2,column=3,pady=10)
        self.t4.grid(row=3,column=3,pady=10)
        self.t6.grid(row=5,column=3,pady=10)
        self.t7.grid(row=6,column=3,pady=10)
        
        self.radio= StringVar()
        
        r1=Radiobutton(self.f2,text='Male',variable=self.radio,value='Male')
        r2=Radiobutton(self.f2,text='Female',variable=self.radio,value='Female')
        self.radio.set('Male')
        r1.grid(row=4,column=3)
        r2.grid(row=4,column=5)
        self.b1=Button(self.f2,text='Register',width=10,command=self.subm)
        self.b2=Button(self.f2,text='Back',width=10,command=self.xcan)
        self.b1.grid(row=7,column=0)
        self.b2.grid(row=7,column=3)
        
        conn2=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn2.cursor()
        cursor.execute("select ifnull(max(accno),0)tmax from tblaccount")
        conn2.commit()
        for row1 in cursor:
            id=int(row1[0])
        id=id+1
        
        self.t1.insert("0",str(id))
        self.t1.config(state='disabled')
        self.root.mainloop()
        conn2.close()
        
        #print(d1)
        #self.t6.insert("0",str(d1))
    def xcan(self):
        self.root.destroy()
        from home_pg import Mn
        Mn()
        
    def subm(self):
        conn=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn.cursor()
        accno=self.t1.get()
        cname=self.t2.get()
        cadd=self.t3.get()
        cgen=self.radio.get()
        cmob=self.t4.get()
        odate=self.t6.get()     
        balance=self.t7.get()
        #print(len(cmob))
        if accno=="" or cname=="" or cadd=="" or cgen=="" or cmob=="" or odate=="" or balance=="" or int(balance)<0 or len(cmob)!=10:
            messagebox.showerror("ERROR","Invalid Entry! Try again")
            self.root.destroy()
            from home_pg import Mn
            Mn()
            
        else:
            self.t1.config(state='disable')
            self.t2.config(state='disable')
            self.t3.config(state='disable')
            self.t4.config(state='disable')
            self.t6.config(state='disable')
            self.t7.config(state='disable')
      
            cursor.execute("INSERT INTO tblaccount (accno,cname,cadd,cgen,cmob,odate,balance) values (%s,%s,%s,%s,%s,%s,%s)", (accno,cname,cadd,cgen,cmob,odate,balance))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succesful","A/C Added Succesfully")
    
          
#ob3=opn()