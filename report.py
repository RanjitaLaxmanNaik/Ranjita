from textwrap import fill
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Report:
    def __init__(self,root):
        self.root=root
        self.root.title("hotel management")
        self.root.geometry("1289x550+230+220")
        #**************************variables********************#
        
        lbl_title=Label(self.root,text="Report",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        labelframeleft=LabelFrame(self.root,bd=2,text="Tenant details",font=("times new roman",16,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=500)

        btn_frame=Frame(labelframeleft,bd=9)
        btn_frame.place(x=0,y=0,width=0,height=0)

        
        btnAdd=Button(btn_frame,text="Final Report",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)
        
        
        
        
    
        
        
       
        
        
        #*********************************************************************#

        

        
    

if __name__ == "__main__":
    root=Tk()
    obj=Report(root)
    root.mainloop()