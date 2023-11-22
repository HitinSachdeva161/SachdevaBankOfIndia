from tkinter import *
from tkinter.ttk import Progressbar
#from login import ln
import login
class pro:
    def __init__(self):
        #super.__init__()
        self.root=Tk()
        self.root.config(background='#20a5f9')
        self.root.geometry('800x500+300+0')
        self.percentage = IntVar()
        self.percentage.set(0)
        self.prg1=Progressbar(self.root,orient=HORIZONTAL,length=400)
        self.l1 = Label(self.root, text="Loading....", font=("Arial", 26,'bold'), bg="#20a5f9")
        self.l1.pack(pady=50)
        self.prg1.pack(pady=25)
        self.prg1.config(mode='determinate',maximum=100)
        self.prg1.config(variable=self.percentage)
        self.increase()      
    
    def increase(self):
        i=self.percentage.get()    
        if i<100:
            i+=5
            self.prg1['value']=i
            self.percentage.set(i)
            self.root.after(100, self.increase)
            self.l1.config(text='Loading....'+str(self.percentage.get())+'%')
        else:
            self.root.destroy()
            obj=login.ln()

        self.root.mainloop()
        
