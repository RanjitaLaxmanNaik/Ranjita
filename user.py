from textwrap import fill
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class user:
    def __init__(self,root):
        self.root=root
        self.root.title("hotel management")
        self.root.geometry("1289x550+230+220")
       
        self.var_username=StringVar()
        self.var_userid=StringVar()
        self.var_password=StringVar()
        

        lbl_title=Label(self.root,text="User Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        
        
           #****************************label Frame***************************#
        labelframeleft=LabelFrame(self.root,bd=2,text="User details",font=("times new roman",16,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #*****************************label entries*******************************#
        lbl_cust_ref=Label(labelframeleft,text="User Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_username,font=("times new roman",13,"bold"),width=29)
        enty_ref.grid(row=0,column=1)

        cname=Label(labelframeleft,text="UserId",font=("times new roman",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_userid,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=1,column=1)

        lblmname=Label(labelframeleft,text="Password",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_password,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        
        btn_frame=Frame(labelframeleft,bd=2)
        btn_frame.place(x=0,y=400,width=412,height=40)

        
        btnAdd=Button(btn_frame,text="add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        Table_Frame=LabelFrame(self.root,bd=2,text="view details and search system",font=("arial",12,"bold"),padx=2)
        
        Table_Frame.place(x=435,y=50,width=860,height=490)
        
        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="search by:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("UserName","UserId")
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

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("userName","userId","password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("userName",text="UserName")
        self.Cust_Details_Table.heading("userId",text="UserId")
        self.Cust_Details_Table.heading("password",text="Password")
        

        self.Cust_Details_Table["show"]="headings"

        
        self.Cust_Details_Table.column("userName",width=100)
        self.Cust_Details_Table.column("userId",width=100)
        self.Cust_Details_Table.column("password",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_username.get()=="" or self.var_userid.get()=="":
            messagebox.showerror("Error","All fields Required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into user values(%s,%s,%s)",(
                                                                         self.var_username.get(),
                                                                         self.var_userid.get(),
                                                                         self.var_password.get(),
                                                                         
                                                                    ))
                conn.commit()
                #***********************it shows the table details********************#
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","user has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from user")
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
        self.var_username.set(row[0]),
        self.var_userid.set(row[1]),
        self.var_password.set(row[2]),

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from user where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
            conn.close()
        

        

        
        
        

        
    

             


        



if __name__ == "__main__":
    root=Tk()
    obj=user(root)
    root.mainloop()