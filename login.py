from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tenants import Tenant
from Payment import payment
from houseform import houses
from type import type
from user import user


import random

from tkinter import messagebox



class hotelmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")
        #**********************put image on the screen************************#
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\naikr\OneDrive\Desktop\ranjita\10733049.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        #**********************************************************************#
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        
        
        img1=Image.open(r"C:\Users\naikr\OneDrive\Desktop\ranjita\download (1).png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbling=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbling.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="get started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)
        #*****************label**********************#
        username=lbl=Label(frame,text="username",font=("times new roman",18,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        #****************************************************#

        password=lbl=Label(frame,text="password",font=("times new roman",18,"bold"),fg="white",bg="black")
        password.place(x=70,y=220)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        
        #******************************Login button********************************#
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=160,height=35)



        
    def login(self):
        
        
        
        if self.txtuser.get()=="Pannaga" or self.txtpass.get()=="123":
           self.root=root
           self.root.title("House rental management System")
           self.root.geometry("1550x800+0+0")

           img1=Image.open(r"C:\Users\naikr\OneDrive\Desktop\ranjita\1.jpg")
           img1=img1.resize((1550,140),Image.Resampling.NEAREST)
           self.photoimg1=ImageTk.PhotoImage(img1)

           lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
           lblimg.place(x=0,y=0,width=1550,height=140)

           img2=Image.open(r"C:\Users\naikr\OneDrive\Desktop\ranjita\711851.jpg")
           img2=img2.resize((230,140),Image.Resampling.NEAREST)
           self.photoimg2=ImageTk.PhotoImage(img2)

           lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
           lblimg.place(x=0,y=0,width=230,height=140)

           lbl_title=Label(self.root,text="House rental management system",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,)
           lbl_title.place(x=0,y=140,width=1550,height=50)

           main_frame=Frame(self.root,bd=4)
           main_frame.place(x=0,y=190,width=1550,height=620)

           lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,)
           lbl_menu.place(x=0,y=0,width=230)

           btn_frame=Frame(main_frame,bd=4)
           btn_frame.place(x=0,y=35,width=228,height=300)

           

        
     
           cust_btn=Button(btn_frame,text="HouseType",command=self.type_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
           cust_btn.grid(row=0,column=0,pady=1)
    

           room_btn=Button(btn_frame,text="Houses",command=self.house_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
           room_btn.grid(row=1,column=0,pady=1)
      #***************************************tenants information**************************************#
           details_btn=Button(btn_frame,text="Tenants",command=self.tenant_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
           details_btn.grid(row=2,column=0,pady=1)
        #*********************************************************************************************#

           payment_btn=Button(btn_frame,text="Payments",command=self.payment_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
           payment_btn.grid(row=3,column=0,pady=1)

           user_btn=Button(btn_frame,text="User",command=self.user_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
           user_btn.grid(row=4,column=0,pady=1)

          
           

          

           

           logout_btn=Button(btn_frame,text="Logout",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
           logout_btn.grid(row=5,column=0,pady=1)


           img3=Image.open(r"C:\Users\naikr\OneDrive\Desktop\ranjita\1700222.jpg")
           img3=img3.resize((1310,590),Image.Resampling.NEAREST)
           self.photoimg3=ImageTk.PhotoImage(img3)

           lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
           lblimg1.place(x=225,y=0,width=1310,height=590)

        

           img5=Image.open(r"C:\Users\naikr\OneDrive\Desktop\ranjita\house-1477041__340.jpg")
           img5=img5.resize((230,190),Image.Resampling.NEAREST)
           self.photoimg5=ImageTk.PhotoImage(img5)
           lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
           lblimg1.place(x=0,y=420,width=230,height=190)
        elif self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Invalid","Please enter username and password")
        
        elif self.txtuser.get()=="" or self.txtpass.get()=="123":
            messagebox.showerror("Invalid","Please enter username")
        elif self.txtuser.get()!="Pannaga" or self.txtpass.get()!="123":
            messagebox.showerror("Invalid","Please enter correct username and password")
        


    def tenant_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Tenant(self.new_window)

    def payment_details(self):
        self.new_window=Toplevel(self.root)
        self.app=payment(self.new_window)

    def house_details(self):
        self.new_window=Toplevel(self.root)
        self.app=houses(self.new_window)

    def type_details(self):
        self.new_window=Toplevel(self.root)
        self.app=type(self.new_window)

    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=user(self.new_window)

   
    
   

    def logout(self):
        self.root.destroy()


    







        
        
        




        
            




        
        
        




        
#**********************************************************#
if __name__ =="__main__":
    root=Tk()
    obj=hotelmanagementsystem(root)
    root.mainloop()
    