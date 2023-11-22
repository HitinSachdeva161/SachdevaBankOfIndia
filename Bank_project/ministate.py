from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql.cursors
from datetime import date
from datetime import datetime
class mini: 
    def __init__(self):
        self.root=Tk()
        self.root.geometry('800x500+300+0')     
        self.root.title("Ministatement")
        self.root.config(background='#51b9fa')
        self.l1=Label(self.root,text="Enter A/c No")
        self.t1=Entry(self.root)
        self.head=Label(self.root,text="Mini-statement",background='white',font=("Century Schoolbook", 15,'bold'))
        self.head.pack(pady=5)
        self.b1=Button(self.root,text="Ok",command=self.okay)
        self.b1.place(relx=0.6,rely=0.1)
        self.l1.place(relx=0.2,rely=0.1)
        self.t1.place(relx=0.4,rely=0.1)
        self.txt=Text(self.root,height=20)
        self.b2=Button(self.root,text="Back",command=self.bkk)
        self.root.mainloop()
    
    def okay(self):
        self.txt.place(relx=0.1,rely=0.2)
        self.b2.place(relx=0.4,rely=0.9)
        acc=self.t1.get()
        self.t1.config(state='disabled')
        conn=pymysql.connect(host='localhost',user='root',password='root',db='sbibank')
        cursor=conn.cursor()
        cursor.execute("select * from tbltransaction where transsrcaccno=%s or transdestaccno=%s",(acc,acc))
        conn.commit()
        
        rows=cursor.rowcount
        #conn.close()
        if rows>0:
            #for row in cursor:
            #   self.txt.insert("1.0",row)
            #cursor.execute("SELECT * FROM your_table")
            rows = cursor.fetchall()
            
# Format and organize the data into a tabular structure
            table_data = []
            for row in rows:
                table_data.append(list(row))

# Create a formatted string representation of the tabular data
                table_string = ""
            for row in table_data:
                table_string += "\t".join(str(col) for col in row) + "\n"
            self.txt.insert("1.0","id  From A/c   To A/c   type    Amt       date      time \n")
            self.txt.insert("2.0","------------------------------------------------------------------ \n")
# Insert the formatted string into the text area
            self.txt.insert("3.0", table_string)
            self.txt.config(state='disabled')

        else:
            messagebox.showerror("Error", "No data found!!")
            self.bkk()
    def bkk(self):
        self.root.destroy()
        from home_pg import Mn
        Mn()     
#b=mini()
        
