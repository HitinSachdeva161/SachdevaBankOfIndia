from tkinter import *
from tkinter import messagebox
import pymysql.cursors
class dlt: 
    def __init__(self):
        self.root=Tk()
        self.root.geometry('800x500+300+0')     #
        self.root.title("Delete")
        self.root.config(background='#51b9fa')
        self.l1=Label(self.root,text='Delete A/c',font=("Arial", 30,'bold'))
        self.l1.pack(pady=5)
        self.l2=Label(self.root,text="Enter A/c No",background='#51b9fa',font=("Century Schoolbook", 10,'bold'))
        self.l2.place(relx=0.21,rely=0.21,anchor="sw")
        self.e1=Entry(self.root)
        self.e1.place(relx=0.51,rely=0.21,anchor="sw")
        self.f2=Frame(self.root,height=400,width=700,background='#83cdfb')
        
        self.b1=Button(self.root,text="Show",command=self.qry)
        self.b1.place(relx=0.8,rely=0.21,anchor="sw")
        
        self.l1=Label(self.f2,text='A/c No',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l2=Label(self.f2,text='Customer Name',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l3=Label(self.f2,text='Address',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l5=Label(self.f2,text='Mobile No.',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l4=Label(self.f2,text='Gender',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l6=Label(self.f2,text='Date',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        self.l7=Label(self.f2,text='Balance',background='#51b9fa',font=("Century Schoolbook", 9,'bold'))
        
        self.t1=Entry(self.f2)
        self.t2=Entry(self.f2)
        self.t3=Entry(self.f2)
        self.t4=Entry(self.f2)
        self.t5=Entry(self.f2)
        self.t6=Entry(self.f2)
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
        self.t5.grid(row=4,column=3,pady=10)
        self.t6.grid(row=5,column=3,pady=10)
        self.t7.grid(row=6,column=3,pady=10)
        
        self.b2=Button(self.f2,text="Back",command=self.bk,width=6)
        self.b2.grid(row=7,column=2,columnspan=2,stick="w")
        self.b3=Button(self.f2,text="Delete",command=self.dl,width=6)
        self.b3.grid(row=7,column=4,columnspan=2,stick="w")
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
                self.t1.insert(0,str(row[0]))
                self.t2.insert(0,str(row[1]))
                self.t3.insert(0,str(row[2]))
                self.t4.insert(0,str(row[3]))
                self.t5.insert(0,str(row[4]))
                self.t6.insert(0,str(row[5]))
                self.t7.insert(0,str(row[6]))
                
                self.e1.config(state='disabled')
                self.t1.config(state='disable')
                self.t2.config(state='disable')
                self.t3.config(state='disable')
                self.t4.config(state='disable')
                self.t5.config(state='disable')
                self.t6.config(state='disable')
                self.t7.config(state='disable')
                conn.close()
                                
        
        else:
            messagebox.showerror("Error", "Invalid A/c No")
            self.root.destroy()
            from home_pg import Mn
            op=Mn()
     
    def dl(self):
        accno=self.t1.get()
        
        conn2=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn2.cursor()
        cursor.execute("DELETE FROM tblaccount WHERE accno=%s", (accno))
        conn2.commit()
        conn2.close()
        messagebox.showinfo("Succesful","Delete Operation was Succesfully")
           
       
    def bk(self):
        self.root.destroy()
        from home_pg import Mn
        op=Mn()
        
#bh=dlt()