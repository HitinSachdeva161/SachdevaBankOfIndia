from tkinter import *
from tkinter import messagebox
import pymysql.cursors
class srch: 
    def __init__(self):
        self.root=Tk()
        self.root.geometry('800x500+300+0')     #
        self.root.title("Search By A/c No")
        self.root.config(background='#51b9fa')
        self.l1=Label(self.root,text='Search By A/c No',font=("Arial", 30,'bold'))
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
        self.lb5=Label(self.f2,text='Mobile No.',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.lb4=Label(self.f2,text='Gender',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.lb6=Label(self.f2,text='Date',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.lb7=Label(self.f2,text='Balance',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        
        self.t1=Entry(self.f2)#ac
        self.t2=Entry(self.f2)#nm
        self.t3=Entry(self.f2)#ad
        self.t4=Entry(self.f2)#mb
        self.t5=Entry(self.f2)#gen
        self.t6=Entry(self.f2)#dt
        self.t7=Entry(self.f2)#ba
        
      
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
        self.t5.grid(row=4,column=3,pady=10)
        self.t6.grid(row=5,column=3,pady=10)
        self.t7.grid(row=6,column=3,pady=10)
        
        self.b2=Button(self.f2,text="Back",command=self.bk,width=6)
        self.b2.grid(row=7,column=2,columnspan=2,stick="w")
        self.root.mainloop()

    def qry(self):
        val=self.e1.get()
        conn=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn.cursor()
        cursor.execute("select * from tblaccount where accno=%s",(val))
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
                self.t5.insert(0,str(row[4]))
                self.t6.insert(0,str(row[5]))
                self.t7.insert(0,str(row[6]))
                
                self.e1.config(state='disabled')
                self.t1.config(state='disabled')
                self.t2.config(state='disabled')
                self.t3.config(state='disabled')
                self.t4.config(state='disabled')
                self.t5.config(state='disabled')
                self.t6.config(state='disabled')
                self.t7.config(state='disabled')
        
        else:
            messagebox.showerror("Error", "Invalid A/c No")
            self.root.destroy()
            from home_pg import Mn
            op=Mn()
     
        conn.close()
    
       
    def bk(self):
        self.root.destroy()
        from home_pg import Mn
        op=Mn()
        
#obh=srch()