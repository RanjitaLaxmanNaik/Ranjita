from textwrap import fill
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("House rental management")
        self.root.geometry("1289x550+230+220")
        #**************************variables********************#
        
        self.var_name=StringVar()
        self.var_house_rented=StringVar()
        self.var_monthly_rate=StringVar()
        
        self.var_outstaffing_balence=StringVar()
        self.var_last_payment=StringVar()
        
        
        




        
        lbl_title=Label(self.root,text="House Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img2=Image.open(r"C:\ranjita\istockphoto-1257951336-170667a.jpg")
        img2=img2.resize((100,40),Image.Resampling.NEAREST)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=5,y=2,width=230,height=40)
           
           #****************************label Frame***************************#
        labelframeleft=LabelFrame(self.root,bd=2,text="Tenant details",font=("times new roman",16,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #*****************************label entries*******************************#
        lbl_cust_ref=Label(labelframeleft,text="Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_name,font=("times new roman",13,"bold"),width=29)
        enty_ref.grid(row=0,column=1)

        cname=Label(labelframeleft,text="House rented",font=("times new roman",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_house_rented,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=1,column=1)

        lblmname=Label(labelframeleft,text="Monthly Rate",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_monthly_rate,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        
        
        lblPostCode=Label(labelframeleft,text="Outstaffing Balence",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_outstaffing_balence,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        lblMobile=Label(labelframeleft,text="Last payment",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_last_payment,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        
        #**************************************btn***************************#

        btn_frame=Frame(labelframeleft,bd=2)
        btn_frame.place(x=0,y=400,width=412,height=40)

        
        btnAdd=Button(btn_frame,text="add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=3,padx=1)
        #*********************************************************************#

        Table_Frame=LabelFrame(self.root,bd=2,text="view details and search system",font=("arial",12,"bold"),padx=2)
        
        Table_Frame.place(x=435,y=50,width=860,height=490)
        
        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="search by:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        txtSearch=ttk.Entry(Table_Frame,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="search",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="show all",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #********************************** show data tables***************************************#
        

        details_table=Frame(Table_Frame,bd=2)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("Name","House Rented","Monthly Rate","Outstaffing Details","Last payment"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Name",text="Name")
        self.Cust_Details_Table.heading("House Rented",text="House Rented")
        self.Cust_Details_Table.heading("Monthly Rate",text="Monthly Rate")
        
        self.Cust_Details_Table.heading("Outstaffing Details",text="Outstaffing Details")
        self.Cust_Details_Table.heading("Last payment",text="Last payment")
        
        self.Cust_Details_Table["show"]="headings"

        
        self.Cust_Details_Table.column("Name",width=100)
        self.Cust_Details_Table.column("House Rented",width=100)
        self.Cust_Details_Table.column("Monthly Rate",width=100)
        
        self.Cust_Details_Table.column("Outstaffing Details",width=100)
        self.Cust_Details_Table.column("Last payment",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        #***********************fetch_data***************************#
        self.fetch_data()

    def add_data(self):
        if self.var_name.get()=="" or self.var_house_rented.get()=="":
            messagebox.showerror("Error","All fields Required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="houserental")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s)",(
                                                                         self.var_name.get(),
                                                                         self.var_house_rented.get(),
                                                                         self.var_monthly_rate.get(),
                                                                         
                                                                         self.var_outstaffing_balence.get(),
                                                                         self.var_last_payment.get()
                                                                         
                                                                    ))
                conn.commit()
                #***********************it shows the table details********************#
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)

    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="houserental")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
            conn.close()   

    def update(self):
        if self.var_name.get()=="":
            messagebox.showerror("error","please enter name field",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="houserental")
           my_cursor=conn.cursor()
           my_cursor.execute("update customer")



    

if __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()
    