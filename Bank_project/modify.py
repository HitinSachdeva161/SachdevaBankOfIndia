from tkinter import *
from tkinter import messagebox
import pymysql.cursors

class modf: 
    #genz= StringVar()
    def __init__(self):
        self.root=Tk()
        #global genz
        self.genz = StringVar(value='Male')
        self.root.geometry('800x500+300+0')     #
        self.root.title("Modify")
        self.root.config(background='#51b9fa')
        self.l1=Label(self.root,text='Modify',font=("Arial", 30,'bold'))
        self.l1.pack(pady=5)
        self.l2=Label(self.root,text="Enter A/c No",background='#51b9fa',font=("Century Schoolbook", 10,'bold'))
        self.l2.place(relx=0.21,rely=0.21,anchor="sw")
        self.e1=Entry(self.root)
        self.e1.place(relx=0.51,rely=0.21,anchor="sw")
        self.f2=Frame(self.root,height=400,width=700,background='#83cdfb')
        
        self.b1=Button(self.root,text="Show",command=self.qry)
        self.b1.place(relx=0.8,rely=0.21,anchor="sw")
        
        self.lb1=Label(self.f2,text='A/c No',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.lb2=Label(self.f2,text='Customer Name',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.lb3=Label(self.f2,text='Address',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.lb4=Label(self.f2,text='Mobile No.',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.lb5=Label(self.f2,text='Gender',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.lb6=Label(self.f2,text='Date',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.lb7=Label(self.f2,text='Balance',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        
        self.t1=Entry(self.f2)
        self.t2=Entry(self.f2)
        self.t3=Entry(self.f2)
        self.t4=Entry(self.f2)
        self.t5=Entry(self.f2)
        self.t6=Entry(self.f2)
        self.t7=Entry(self.f2)
        
        
        self.r1=Radiobutton(self.f2,text='Male',variable=self.genz,value='Male')
        self.r2=Radiobutton(self.f2,text='Female',variable=self.genz,value='Female')
        self.genz.set('Male')
        
        self.lb1.grid(row=0,column=0,padx=100,pady=10)
        self.lb2.grid(row=1,column=0,pady=10)
        self.lb3.grid(row=2,column=0,pady=10)
        self.lb4.grid(row=3,column=0,pady=10)
        self.lb5.grid(row=4,column=0,pady=10)
        self.lb6.grid(row=5,column=0,pady=10)
        self.lb7.grid(row=6,column=0,pady=10)
        
        self.t1.grid(row=0,column=3,padx=100,pady=10)
        self.t2.grid(row=1,column=3,pady=10)
        self.t3.grid(row=2,column=3,pady=10)
        self.t4.grid(row=3,column=3,pady=10)
        #self.t5.grid(row=4,column=3,pady=10)
        self.r1.grid(row=4,column=3)
        self.r2.grid(row=4,column=4)
        self.t6.grid(row=5,column=3,pady=10)
        self.t7.grid(row=6,column=3,pady=10)
        
        self.b2=Button(self.f2,text="Back",command=self.bk,width=6)
        self.b2.grid(row=7,column=2,columnspan=2,stick="w")
        self.b3=Button(self.f2,text="Update",command=self.modk,width=6)
        self.b3.grid(row=7,column=4,columnspan=2,stick="w")
        self.root.mainloop()

    def qry(self):
        val=self.e1.get()
        #print(self.genz.get())
        conn=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn.cursor()
        cursor.execute("select * from tblaccount where accno=%s",(val))
        conn.commit()
        rows=cursor.rowcount
        
        if rows>0:
            self.f2.place(relx=0.0701,rely=0.3,relwidth=0.8)
            for row in cursor:
                self.t1.insert(0,str(row[0]))
                self.t2.insert(0,str(row[1]))
                self.t3.insert(0,str(row[2]))
                self.t4.insert(0,str(row[4]))
                #self.t5.insert(0,str(row[4]))
                #print(row[3])
                self.genz.set(str(row[3]))
                #print(self.genz.get())
                self.t6.insert(0,str(row[5]))
                self.t7.insert(0,str(row[6]))
                
                self.e1.config(state='disabled')
                self.t1.config(state='disabled')
                self.t6.config(state='disabled')
                self.t7.config(state='disabled')
                conn.close()
                                
        
        else:
            messagebox.showerror("Error", "Invalid A/c No")
            self.root.destroy()
            from home_pg import Mn
            op=Mn()
     
    def modk(self):
        accno=self.t1.get()
        cname=self.t2.get()
        cadd=self.t3.get()
        cgen=self.genz.get()
        #print(self.genz.get())
        cmob=self.t4.get()
        #print(len(cmob))
        if len(cmob)!=10:
            messagebox.showerror("Error","Enter Valid Values")
            self.root.destroy()
            from home_pg import Mn
            Mn() 
        else:      
            conn2=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
            cursor=conn2.cursor()
            cursor.execute("UPDATE tblaccount SET cname=%s,cadd=%s,cgen=%s,cmob=%s WHERE accno=%s", (cname,cadd,cgen,cmob,accno))
            conn2.commit()
            conn2.close()
            messagebox.showinfo("Succesful","Update Operation was Succesfully")
           
       
    def bk(self):
        self.root.destroy()
        from home_pg import Mn
        op=Mn()
        
#obh=modf()