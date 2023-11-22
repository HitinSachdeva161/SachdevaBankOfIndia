from tkinter import *
from PIL import Image,ImageTk
import pymysql.cursors
from tkinter import messagebox
from PIL.ImageOps import expand
from tkinter.simpledialog import askstring
import login
#from progress import pro
class forg:
    def __init__(self):
        self.root=Tk()
        #self.root.geometry('800x500+300+0')
        self.root.geometry('800x500+300+0')
        
        self.f2=Frame(self.root,background='white')
        self.f2.place(x=0, y=0, relwidth=1.0, relheight=.5, anchor="nw")
       
        
        img=Image.open('E:\eclipse\work_eclipse\Bank_project\images/ww1.jpg')
        i2=img.resize((500,120))
        self.i1=ImageTk.PhotoImage(i2)
        self.l2=Label(self.f2)
        self.l2.config(image=self.i1,background='white')
        self.l2.pack()
        
        self.l1=Label(self.f2,text='User ID->')
        self.l1.place(relx=0.4,rely=0.71,anchor="e")
        self.t1=Entry(self.f2,borderwidth=5,foreground='red')
        self.t1.place(relx=0.6,rely=0.71,anchor="w")
        self.ok=Button(self.f2,text='OK',width=15,background='#57a1f8',command=self.show)
        self.ok.place(relx=0.8,rely=0.71,anchor="w")
        #self.t1.pack()
        
        self.f1=Frame(self.root,width=300, height=200,background='#83cdfb')  
        
       
        
        self.q=Label(self.f1,text='Hekko',background='#83cdfb',font=("Arial", 16))
        self.q.place(relx=0.3,rely=0.4,anchor="e")
        self.ans=Entry(self.f1)
        self.ans.place(relx=0.5,rely=0.4,anchor="w")
        self.b1=Button(self.f1,text='Verify',width=15,command=self.disp)
        self.b1.place(relx=0.45,rely=0.71,anchor="s")
        self.ti=Label(self.f1,text="Security Question",bg='white',font=("Arial", 26,'bold','underline'))
        self.ti.pack()
        
        self.f3=Frame(self.root,bg='black')
        self.f3.place(relx=0.0001,rely=0.5,relwidth=300,height=2,anchor="nw")
        self.root.mainloop()   
    a1=StringVar
    def show(self):
       
        conn=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn.cursor()
        a1=self.t1.get()
        cursor.execute("select * from tbladmin where admid=%s",(a1))
        conn.commit()
        rows=cursor.rowcount
        for row in cursor:
            #print(row[3])
            self.q.config(text=row[2])
        if rows>0:  
            self.f1.place(x=0, rely=0.5, relwidth=1.0, relheight=.5, anchor="nw")
            self.t1.config(state='disabled')
    
        else:
            messagebox.showerror("Login Failed", "Invalid User ID")
        conn.close()
        
    def disp(self):
        
        conn1=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor1=conn1.cursor()
        a1=self.t1.get()
        cursor1.execute("select admpwd,admsecans from tbladmin where admid=%s",(a1))
        conn1.commit()
        #rows=cursor.rowcount
        #aq=rows[0]
        #print(ag)
        
        for row in cursor1:
            #print(row[1])
            abc=row[1]
            pas=row[0]
            
        if self.ans.get()==abc:
            #messagebox.showinfo('Password',row[0])
            ms=askstring('New Password','Please Enter New Password')
            ax=askstring('Confirm Password','Please Confirm New Password')
            if ms==ax:
                cursor1.execute("update tbladmin set admpwd=%s where admid=%s",(ms,a1))
                conn1.commit()
                self.root.destroy()
                pp=login.ln()
            else:
                messagebox.showerror("Process Failed", "Passwords doesn't Match")
            
        else:
            messagebox.showerror("Process Failed", "Invalid Answer")
        conn1.close()   
        
        
        
        
        
    
#obl=forg()      
   