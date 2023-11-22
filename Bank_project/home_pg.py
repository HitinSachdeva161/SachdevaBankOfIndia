from tkinter import *
from PIL import Image,ImageTk
#import opennew
#from opennew import *
class Mn:
    def __init__(self):
        self.root=Tk()
        self.root.title("Home")
        self.root.geometry('800x500+300+0')
        self.root.config(background='#83cdfb')
        
        img=Image.open('E:\eclipse\work_eclipse\Bank_project\images\Bank-PO-2.png')
        #img=Image.open('E:\eclipse\work_eclipse\Bank_project\Sachdeva Bank of India.jpg')

        i2=img.resize((440,440))
        self.i1=ImageTk.PhotoImage(i2)
        self.l1=Label(self.root)
        self.l1.config(image=self.i1)
        self.l1.place(relx=0.22,rely=0.1)
        
        self.menubar = Menu(self.root)  
        self.file = Menu(self.menubar, tearoff=0)    
        self.file.add_command(label="Open New Account",command=self.fn1)   
        self.file.add_command(label="Log Off",command=self.fn2)  
        self.menubar.add_cascade(label="File", menu=self.file) 
        self.root.config(menu=self.menubar)
        
        self.edit = Menu(self.menubar, tearoff=0)    
        self.edit.add_command(label="Modify",command=self.fn3)   
        self.edit.add_command(label="Delete",command=self.fn4)  
        self.edit.add_command(label="Search by A/c No",command=self.fn5)  
        self.edit.add_command(label="Search by Name",command=self.fn6)  
        self.edit.add_command(label="View All",command=self.fn7)              #############
        self.edit.add_command(label="View Mini Statement",command=self.fn8)   ###########
        self.menubar.add_cascade(label="Edit", menu=self.edit) 
        #self.root.config(menu=self.menubar)
        
        self.Transaction = Menu(self.menubar, tearoff=0)    
        self.Transaction.add_command(label="Deposit",command=self.fn9)   
        self.Transaction.add_command(label="Withdraw",command=self.fn10)  
        self.Transaction.add_command(label="Transfer",command=self.fn11)    ################### 
        self.menubar.add_cascade(label="Transaction", menu=self.Transaction) 
        #self.root.config(menu=self.menubar)
        self.Profile = Menu(self.menubar, tearoff=0)    
        self.Profile.add_command(label="Edit Profile",command=self.fn12)   
        self.Profile.add_command(label="Edit Security Settings",command=self.fn13)  
        self.Profile.add_command(label="Change the Password",command=self.fn14)     
        self.menubar.add_cascade(label="Profile", menu=self.Profile)
        
        self.help = Menu(self.menubar, tearoff=0)    
        self.help.add_command(label="About the Software",command=self.fn15)   
        self.menubar.add_cascade(label="Help", menu=self.help)
           
        self.root.mainloop()
        
    def fn1(self):
        self.root.destroy()
        from opennew import opn
        opn()
    
    def fn2(self):
        self.root.destroy()
    def fn3(self):
        self.root.destroy()
        from modify import modf
        modf()
    def fn4(self):
        self.root.destroy()
        from delete import dlt
        dlt()
    def fn5(self):
        self.root.destroy()
        from search_acc import srch
        srch()
    def fn6(self):
        self.root.destroy()
        from search_nm import srchnm
        srchnm()
        
    def fn7(self):
        self.root.destroy()
        from view_all import view
        view()
    def fn8(self):
        self.root.destroy()
        from ministate import mini
        mini()
    def fn9(self):
        self.root.destroy()
        from deposit import depos
        depos()
    def fn10(self):
        self.root.destroy()
        from withdraw import withd
        withd()
    def fn11(self):
        self.root.destroy()
        from transfer import transf
        transf()
    def fn12(self):
        self.root.destroy()
        from edit_pro import edp
        edp()
    def fn13(self):
        self.root.destroy()
        from edit_secur import edq
        edq()
    def fn14(self):
        self.root.destroy()
        from change_pass import chp
        chp()
        #print('Hello')
    def fn15(self):
        self.root.destroy()
        from Help import about
        about()
            
#on=Mn()