from textwrap import fill
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Tenant:
    def __init__(self,root):
        self.root=root
        self.root.title("hotel management")
        self.root.geometry("1289x550+230+220")
       
        self.var_house_rented=StringVar()
        self.var_first_name=StringVar()
        self.var_last_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_nationality=StringVar()
        
        

        lbl_title=Label(self.root,text="Tenant Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        
        
           #****************************label Frame***************************#
        labelframeleft=LabelFrame(self.root,bd=2,text="Tenant details",font=("times new roman",16,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #*****************************label entries*******************************#
        lbl_cust_ref=Label(labelframeleft,text="House No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_house_rented,font=("times new roman",13,"bold"),width=29)
        enty_ref.grid(row=0,column=1)

        cname=Label(labelframeleft,text="First Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_first_name,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=1,column=1)

        lblmname=Label(labelframeleft,text="Last Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_last_name,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        label_gender=Label(labelframeleft,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("male","Female","other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        lblPostCode=Label(labelframeleft,text="Mobile",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        lblMobile=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        lblEmail=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        lblNationality=Label(labelframeleft,text="Nationality",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("India","omeroca","other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        

       
        
        btn_frame=Frame(labelframeleft,bd=2)
        btn_frame.place(x=0,y=400,width=412,height=40)

        
        btnAdd=Button(btn_frame,text="add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.Update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=2,padx=1)

        Table_Frame=LabelFrame(self.root,bd=2,text="view details and search system",font=("arial",12,"bold"),padx=2)
        
        Table_Frame.place(x=435,y=50,width=860,height=490)
        
        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="search by:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Fname","HouseNo")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="show all",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        details_table=Frame(Table_Frame,bd=2)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("houseno","fname","lname","gender","mobile","email","address","nationality"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        
        self.Cust_Details_Table.heading("fname",text="Fname")
        self.Cust_Details_Table.heading("lname",text="Lname")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("mobile",text="Mobie")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("address",text="Address")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("houseno",text="HouseNo")
        

        self.Cust_Details_Table["show"]="headings"

        
        self.Cust_Details_Table.column("houseno",width=100)
        self.Cust_Details_Table.column("fname",width=100)


        
        self.Cust_Details_Table.column("lname",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("address",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_gender.get()=="" or self.var_first_name.get()=="":
            messagebox.showerror("Error","All fields Required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into tenant values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                         self.var_house_rented.get(),
                                                                         self.var_first_name.get(),
                                                                         self.var_last_name.get(),
                                                                         self.var_gender.get(),
                                                                         self.var_mobile.get(),
                                                                         self.var_email.get(),
                                                                         self.var_address.get(),
                                                                         self.var_nationality.get(),
                                                                         
                                                                    ))
                conn.commit()
                #***********************it shows the table details********************#
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","tenant has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from tenant")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
            conn.close() 

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]
        self.var_house_rented.set(row[0])
        self.var_first_name.set(row[1]),
        self.var_last_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_address.set(row[6]),
        self.var_nationality.set(row[7]),
        

    def Update(self):
        if self.var_first_name.get()=="":
            messagebox.showerror("error","Please enter the name",parent=self.root)
        else:

            conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update tenant set FName=%s,Lname=%s,Gender=%s,Mobile=%s,Email=%s,Address=%s,Nationality=%s where HouseNo=%s",(
                                                                                                                                                                                
                                                                                                                                                                                
                                                                         self.var_first_name.get(),
                                                                         self.var_last_name.get(),
                                                                         self.var_gender.get(),
                                                                         self.var_mobile.get(),
                                                                         self.var_email.get(),
                                                                         self.var_address.get(),
                                                                         self.var_nationality.get(),
                                                                         self.var_house_rented.get()
                                                                         
                                                                                                                                                                           ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","tenant details has been updated successfully",parent=self.root) 
                     
    def Delete(self):
        Delete=messagebox.askyesno("house rental management","do you want to delete the tenant",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="management")
            my_cursor=conn.cursor()
            query="delete from tenant where HouseNo=%s"
            value=(self.var_house_rented
            .get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from tenant where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
            conn.close()

             


        



if __name__ == "__main__":
    root=Tk()
    obj=Tenant(root)
    root.mainloop()