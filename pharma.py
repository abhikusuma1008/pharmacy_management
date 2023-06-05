from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import os
import sys
import pymysql

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")


        self.addmed_var=StringVar()
        self.refMed_var=StringVar()


        self.ref_no_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()



        lbltitle=Label(self.root,text="PHARAMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open(r"D:\Users\sreet\Desktop\ms\project\logo.jpg")
        img1=img1.resize((70,70),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=60,y=20)


        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine And Department",fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)


        


        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

        


        btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(ButtonFrame,command=self.update_data,text="UPDATE",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(ButtonFrame,command=self.delete_data,text="DELETE",font=("arial",13,"bold"),width=14,bg="red",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(ButtonFrame,command=self.reset,text="RESET",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(ButtonFrame,text="EXIT",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=4)



        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",17,"bold"),state="readonly")
        search_combo["values"]=("Ref_no","medName","Lot","Expdate")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)



        searchBtn=Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        searchBtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,command=self.fatch_data,text="SHOW ALL",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)

        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)


        con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)
        cur=con.cursor()
        cur.execute("select Ref_no from pharma")
        row=cur.fetchall()

        

        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_no_var,width=27,font=("arial",12,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current("0")

        lblCmpName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name",padx=8,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtCmpName.grid(row=1,column=1,sticky=W)

        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type of Medicine",padx=8,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,width=27,font=("arial",12,"bold"),state="readonly")
        comTypeofMedicine["values"]=("Tablet","Liquid","capsules","Topical Medicine","Drops","Inhales","Injections")
        comTypeofMedicine.grid(row=2,column=1)
        comTypeofMedicine.current(0)

        



        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=8,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)
        cur=con.cursor()
        cur.execute("select MedName from pharma")
        med=cur.fetchall()

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,width=27,font=("arial",12,"bold"),state="readonly")
        comMedicineName["values"]=med
        comMedicineName.grid(row=3,column=1)
        comMedicineName.current(0)

        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No",padx=8,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1,sticky=W)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date",padx=8,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1,sticky=W)

        lblExDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expire Date",padx=8,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1,sticky=W)

        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses",padx=8,pady=6)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1,sticky=W)

        lblSideEffects=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effects",padx=8,pady=6)
        lblSideEffects.grid(row=8,column=0,sticky=W)
        txtSideEffects=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffects.grid(row=8,column=1,sticky=W)

        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning",padx=8,pady=6)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrecWarning.grid(row=0,column=3,sticky=W)

        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage",padx=8,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtDosage.grid(row=1,column=3,sticky=W)

        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Price",padx=8,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrice.grid(row=2,column=3,sticky=W)

        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT",padx=8,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtProductQt.grid(row=3,column=3,sticky=W)

        

        lblhome=Label(DataFrameLeft,font=("arial",12,"bold"),text="Stay Home Stay Safe:",padx=10,pady=6,bg="white",fg="red",width=37)
        lblhome.place(x=465,y=140)

        img2=Image.open(r"D:\Users\sreet\Desktop\ms\project\tab.jpg")
        img2=img2.resize((150,135),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=770,y=340)

        img3=Image.open(r"D:\Users\sreet\Desktop\ms\project\eng.jpg")
        img3=img3.resize((150,135),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=620,y=340)

        img4=Image.open(r"D:\Users\sreet\Desktop\ms\project\madam.jpg")
        img4=img4.resize((150,135),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=525,y=340)


        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine And Department",fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        img5=Image.open(r"D:\Users\sreet\Desktop\ms\project\tablets.jpg")
        img5=img5.resize((200,75),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=960,y=160)


        img6=Image.open(r"D:\Users\sreet\Desktop\ms\project\tablets.jpg")
        img6=img6.resize((200,75),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.photoimg6,borderwidth=0)
        b1.place(x=1160,y=160)


        img7=Image.open(r"D:\Users\sreet\Desktop\ms\project\tablets.jpg")
        img7=img7.resize((200,145),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(self.root,image=self.photoimg7,borderwidth=0)
        b1.place(x=1270,y=160)


        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference No:",padx=8,pady=6)
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=15)
        txtrefno.place(x=135,y=80)

        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:",padx=8,pady=6)
        lblmedName.place(x=0,y=110)
        txtmedName=Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=15)
        txtmedName.place(x=135,y=110)



        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        



        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")


        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)


        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=150,width=135,height=160)


        btnAddmed=Button(down_frame,text="ADD",command=self.AddMed,font=("arial",13,"bold"),width=12,bg="lime",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="UPDATE",command=self.UpdateMed,font=("arial",13,"bold"),width=12,bg="purple",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="DELETE",command=self.DeleteMed,font=("arial",13,"bold"),width=12,bg="red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnAddClearmed=Button(down_frame,text="CLEAR",command=self.ClearMed,font=("arial",13,"bold"),width=12,bg="orange",fg="white",pady=4)
        btnAddClearmed.grid(row=3,column=0)

        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1530,height=210)

        Table_frame=Frame(Framedetails,bd=15,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1500,height=180)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("ref","medname","type","tablename","lotno","issuedate","expdate","uses","sideeffects","warning","dosage","price","productqt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("ref",text="Reference No")
        self.pharmacy_table.heading("medname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tablename",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffects",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("medname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tablename",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffects",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()
        self.fatch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

    def AddMed(self):
        try:

                con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)

                cur=con.cursor()

                cur.execute("insert into pharma(Ref_no,MedName) value(%s,%s)",(self.refMed_var.get(),self.addmed_var.get()))

                

                
                con.commit()
                self.fetch_dataMed()
                con.close()

                messagebox.showinfo("Success","Register Succesfull",parent=self.root)

        except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

    def fetch_dataMed(self):
        try:
                con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)
                cur=con.cursor()
                cur.execute("select * from pharma")
                row=cur.fetchall()
                if len(row)!=0:
                    self.medicine_table.delete(*self.medicine_table.get_children())
                    for i in row:
                        self.medicine_table.insert("",END,values=i)
                    con.commit()
                con.close()
        except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    

    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])


    def UpdateMed(self):
        if self.refMed_var.get()== "" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)
                cur=con.cursor()
                cur.execute("update pharma set MedName=%s where Ref_no=%s",(self.addmed_var.get(),self.refMed_var.get()))
                con.commit()
                self.fetch_dataMed()
                con.close()
                messagebox.showinfo("Success","Medicine has been Updated")
            except Exception as es:

                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    def DeleteMed(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)
            cur=con.cursor()

            sql="delete from pharma where Ref_no=%s"
            val=(self.refMed_var.get(),)
            cur.execute(sql,val)

            con.commit()
            self.fetch_dataMed()
            con.close()
            messagebox.showinfo("Success","Medicine has been Deleted")
        except Exception as es:

                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")
    

    def add_data(self):
        if self.ref_no_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)

                cur=con.cursor()

                cur.execute("insert into pharmacy(Ref_no,CmpName,TypeMed,medName,Lot,Issuedate,Expdate,Uses,sideeffects,warning,dosage,price,product) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ref_no_var.get(),self.cmpName_var.get(),self.typeMed_var.get(),self.medName_var.get(),self.lot_var.get(),self.issuedate_var.get(),self.expdate_var.get(),self.uses_var.get(),self.sideEffect_var.get(),self.warning_var.get(),self.dosage_var.get(),self.price_var.get(),self.product_var.get()))
                
                con.commit()
                self.fatch_data()
                con.close()
                messagebox.showinfo("Success","data has been inserted")

            except Exception as es:

                    messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    

    def fatch_data(self):
        try:
                con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)

                cur=con.cursor()

                cur.execute("select * from pharmacy")
                row=cur.fetchall()
                if len(row)!=0:
                    self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                    for i in row:
                        self.pharmacy_table.insert("",END,values=i)
                    con.commit()
                con.close()

        except Exception as es:

                    messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)


    def get_cursor(self,ev=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        self.ref_no_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12])

    def update_data(self):
        if self.ref_no_var.get()== "" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)
                cur=con.cursor()
                cur.execute("update pharmacy set cmpName=%s,typeMed=%s,medName=%s,lot=%s,issuedate=%s,expdate=%s,uses=%s,sideEffect=%s,warning=%s,dosage=%s,price=%s,product=%s where ref_no=%s",(self.cmpName_var.get(),self.typeMed_var.get(),self.medName_var.get(),self.lot_var.get(),self.issuedate_var.get(),self.expdate_var.get(),self.uses_var.get(),self.sideEffect_var.get(),self.warning_var.get(),self.dosage_var.get(),self.price_var.get(),self.product_var.get(),self.ref_no_var.get()))
                con.commit()
                self.fetch_dataMed()
                con.close()
                messagebox.showinfo("Success","Medicine has been Updated")
            except Exception as es:

                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
        
        
    def delete_data(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)
            cur=con.cursor()

            sql="delete from pharmacy where Ref_no=%s"
            val=(self.ref_no_var.get(),)
            cur.execute(sql,val)

            con.commit()
            self.fetch_dataMed()
            con.close()
            messagebox.showinfo("Delete","Info Deleted Successfully")
        except Exception as es:

                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

    def reset(self):
        #self.ref_no_var.set("")
        self.cmpName_var.set("")
        #self.typeMed_var.set("")
        #self.medName_var.set("")
        self.lot_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        self.sideEffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.product_var.set("")
        messagebox.showinfo("Cleared","Info Cleared Successfully")


    def search_data(self):
        try:
                con=pymysql.connect(host="localhost",user="root",password="Sreethu@12345",database="mydata",port=3306)
                cur=con.cursor()
                cur.execute("select * from pharmacy where "+str(self.search_var.get())+" LIKE '%"+str(self.searchTxt_var.get())+"%'")

                row=cur.fetchall()
                if len(row)!=0:
                    self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                    for i in row:
                        self.pharmacy_table.insert("",END,values=i)
                    con.commit()
                con.close()
        except Exception as es:

                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)            

if __name__ == "__main__":
            
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()

