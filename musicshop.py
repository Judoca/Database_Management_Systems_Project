from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter

class MusicShopDBMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Music Shop Managment System")
        self.root.geometry("1550x800+0+0")


        #=====================================variable=========================
        self.FirstName_var=StringVar()
        self.SurName_var=StringVar()
        self.Country_var=StringVar()
        self.City_var=StringVar()
        self.Address_var=StringVar()
        self.PostalCode_var=StringVar()
        self.MobileNo_var=StringVar()
        self.EmailId_var=StringVar()
        self.ProductId_var=StringVar()
        self.ProductTitle_var=StringVar()
        self.Brand_var=StringVar()
        self.Date_var=StringVar()
        self.Qty_var=StringVar()
        self.Price_var=StringVar()
        


        lbltitle=Label(self.root,text="Music Shop Managment System",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        #=======================================DataFrameLeft=============================

        DataFrameLeft=LabelFrame(frame,text="Customer Infomation",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        '''
        lblMember=Label(DataFrameLeft,bg="Powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),width=27)
        comMember["value"]=("Admin Staf","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblMember=Label(DataFrameLeft,bg="Powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)'''

        
        lblFirstName=Label(DataFrameLeft,bg="Powder blue",text="First Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=1,column=0,sticky=W)

        txtFirstName=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.FirstName_var,width=29)
        txtFirstName.grid(row=1,column=1)


        lblSurName=Label(DataFrameLeft,bg="Powder blue",text="Sur Name",font=("times new roman",15,"bold"),padx=2,pady=4)
        lblSurName.grid(row=2,column=0,sticky=W)

        txtSurName=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.SurName_var,width=29)
        txtSurName.grid(row=2,column=1)

        lblCountry=Label(DataFrameLeft,bg="Powder blue",text="Country",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblCountry.grid(row=3,column=0,sticky=W)

        txtCountry=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Country_var,width=29)
        txtCountry.grid(row=3,column=1)

        lblCity=Label(DataFrameLeft,bg="Powder blue",text="City",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblCity.grid(row=4,column=0,sticky=W)

        txtCity=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.City_var,width=29)
        txtCity.grid(row=4,column=1)

        lblAddress=Label(DataFrameLeft,bg="Powder blue",text="Address",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAddress.grid(row=5,column=0,sticky=W)

        txtAddress=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Address_var,width=29)
        txtAddress.grid(row=5,column=1)

        lblSPostalcode=Label(DataFrameLeft,bg="Powder blue",text="PostalCode",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblSPostalcode.grid(row=6,column=0,sticky=W)

        txtPostalcode=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.PostalCode_var,width=29)
        txtPostalcode.grid(row=6,column=1)

        lblMobileNo=Label(DataFrameLeft,bg="Powder blue",text="Mobile No",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMobileNo.grid(row=7,column=0,sticky=W)

        txtMobileNo=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.MobileNo_var,width=29)
        txtMobileNo.grid(row=7,column=1)

        lblEmailId=Label(DataFrameLeft,bg="Powder blue",text="EmailId",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblEmailId.grid(row=7,column=4,sticky=W)

        txtEmailId=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.EmailId_var,width=29)
        txtEmailId.grid(row=7,column=5)

        lblProductId=Label(DataFrameLeft,bg="Powder blue",text="ProductId",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblProductId.grid(row=1,column=4,sticky=W)

        txtProductId=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.ProductId_var,width=29)
        txtProductId.grid(row=1,column=5)

        lblProductTitle=Label(DataFrameLeft,bg="Powder blue",text="Product Title",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblProductTitle.grid(row=2,column=4,sticky=W)

        txtProductTitle=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.ProductTitle_var,width=29)
        txtProductTitle.grid(row=2,column=5)

        lblBrand=Label(DataFrameLeft,bg="Powder blue",text="Brand",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBrand.grid(row=3,column=4,sticky=W)

        txtBrand=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Brand_var,width=29)
        txtBrand.grid(row=3,column=5)

        lblDate=Label(DataFrameLeft,bg="Powder blue",text="Date",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDate.grid(row=4,column=4,sticky=W)

        txtDate=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Date_var,width=29)
        txtDate.grid(row=4,column=5)

        lblQty=Label(DataFrameLeft,bg="Powder blue",text="Qty",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblQty.grid(row=5,column=4,sticky=W)

        txtQty=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Qty_var,width=29)
        txtQty.grid(row=5,column=5)

        lblPrice=Label(DataFrameLeft,bg="Powder blue",text="Price",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPrice.grid(row=6,column=4,sticky=W)

        txtPrice=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Price_var,width=29)
        txtPrice.grid(row=6,column=5)

        #=============================DataFrameRight=========================


        DataFrameRight=LabelFrame(frame,text="Product Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=870,y=5,width=580,height=350)


        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=32,height=15,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listproduct=["Rickenbacker 330",
                     "Gibson Custom 1961",
                     "Gibson Custom 1963",
                     "Sire Marcus Miller",
                     "Fender American Professional II",
                     "Fender Tony Franklin",
                     "DW Collector's Series",
                     "Sonor SQ2",
                     "Pearl Masterworks",
                     "Moog One",
                     "Moog Matriarch",
                     "Oberheim OB-X8"]

        def SelectProduct(event=""):
            value = str(listbox.get(listbox.curselection()))
            x = value
            if x == "Rickenbacker 330":
                self.ProductId_var.set("330ThinFG")
                self.ProductTitle_var.set("Thinline Semi-Hollow Electric Guitar")
                self.Brand_var.set("Rickenbacker")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")

            elif x=="Gibson Custom 1961":
                self.ProductId_var.set("SGSR61VOCHNH")
                self.ProductTitle_var.set("Les Paul SG Standard Reissue")
                self.Brand_var.set("Gibson")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")

            elif x=="Gibson Custom 1963":
                self.ProductId_var.set("FB5VOVSNM")
                self.ProductTitle_var.set("Firebird V with Maestro Vibrola")
                self.Brand_var.set("Gibson")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")

            elif x=="Sire Marcus Miller":
                self.ProductId_var.set("MMM7S5FTBk")
                self.ProductTitle_var.set("M7 5-string Fretless Bass ")
                self.Brand_var.set("Sire Marcus Miller")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")

            elif x=="Fender American Professional II":
                self.ProductId_var.set("JBassAP2FROW")
                self.ProductTitle_var.set("American Professional II Jazz Bass Fretless")
                self.Brand_var.set("Fender")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")
            
            elif x=="Fender Tony Franklin":
                self.ProductId_var.set("PBassTFflBlk")
                self.ProductTitle_var.set("Tony Franklin Fretless Precision Bass")
                self.Brand_var.set("Fender")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")

            elif x=="DW Collector's Series":
                self.ProductId_var.set("DRKT722IV")
                self.ProductTitle_var.set("7-piece Shell Pack with Snare Drum")
                self.Brand_var.set("DW")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")
            
            elif x=="Sonor SQ2":
                self.ProductId_var.set("SQ2622ST")
                self.ProductTitle_var.set("Beech 6-piece Shell Pack")
                self.Brand_var.set("Sonor")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")
            
            elif x=="Pearl Masterworks":
                self.ProductId_var.set("MW922BN-BLZ ")
                self.ProductTitle_var.set("9-piece Shell Pack with Snare Drums")
                self.Brand_var.set("Sonor")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")
            
            elif x=="Moog One":
                self.ProductId_var.set("MoogOne16")
                self.ProductTitle_var.set("16-voice Analog Synthesizer")
                self.Brand_var.set("Moog")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")


            elif x=="Moog Matriarch":
                self.ProductId_var.set("Matriarch")
                self.ProductTitle_var.set("Semi-modular Analog Synthesizer and Step Sequencer")
                self.Brand_var.set("Moog")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")

            elif x=="Oberheim OB-X8":
                self.ProductId_var.set("OBX8")
                self.ProductTitle_var.set("8-voice Polyphonic Analog Synthesizer")
                self.Brand_var.set("Oberheim")
                self.Date_var.set("")
                self.Qty_var.set("")
                self.Price_var.set("")


        listbox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=20,height=15)
        listbox.bind("<<ListboxSelect>>",SelectProduct)
        listbox.grid(row=0,column=0,padx=4)

        listScrollbar.config(command=listbox.yview)

        for item in listproduct:
            listbox.insert(END,item)


        #========================================Button Frame==========================================
        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=530,width=1530,height=60)

        btnAddData=Button(framebutton,command=self.adda_data,text="Add Data",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,command=self.showData,text="Show Data",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(framebutton,command=self.update,text="Update",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(framebutton,command=self.delete,text="Delete",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(framebutton,command=self.reset,text="Reset",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebutton,command=self.iExit,text="Exit",font=("times new roman",12,"bold"),width=26 ,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

         #========================================Information  Frame==========================================
        frameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameDetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame(frameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)        
        self.library_table=ttk.Treeview(Table_frame,columns=("FirstName","SurName","Country","City","Address","PostalCode","MobileNo","EmailId","ProductId","ProductTitle","Brand","Date","Qty","Price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("FirstName",text="FirstName")
        self.library_table.heading("SurName",text="SurName")
        self.library_table.heading("Country",text="Country")
        self.library_table.heading("City",text="City")
        self.library_table.heading("Address",text="Address")
        self.library_table.heading("PostalCode",text="PostalCode")
        self.library_table.heading("MobileNo",text="MobileNo")
        self.library_table.heading("EmailId",text="EmailId")
        self.library_table.heading("ProductId",text="ProductId")
        self.library_table.heading("ProductTitle",text="ProductTitle")
        self.library_table.heading("Brand",text="Brand")
        self.library_table.heading("Date",text="Date")
        self.library_table.heading("Qty",text="Qty")
        self.library_table.heading("Price",text="Price")
        




        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("FirstName",width=100)
        self.library_table.column("SurName",width=100)
        self.library_table.column("Country",width=100)
        self.library_table.column("City",width=100)
        self.library_table.column("Address",width=100)
        self.library_table.column("PostalCode",width=100)
        self.library_table.column("MobileNo",width=100)
        self.library_table.column("EmailId",width=100)
        self.library_table.column("ProductId",width=100)
        self.library_table.column("ProductTitle",width=100)
        self.library_table.column("Brand",width=100)
        self.library_table.column("Date",width=100)
        self.library_table.column("Qty",width=100)
        self.library_table.column("Price",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
    
        conn = mysql.connector.connect(host="localhost", user="root", password="jnj012004", database="musicdbms")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO music (FirstName, SurName, Country, City, Address, PostalCode, MobileNo, EmailId, ProductId, ProductTitle, Brand, Date, Qty, Price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            self.FirstName_var.get(), self.SurName_var.get(), self.Country_var.get(),
            self.City_var.get(), self.Address_var.get(), self.PostalCode_var.get(),
            self.MobileNo_var.get(), self.EmailId_var.get(), self.ProductId_var.get(),
            self.ProductTitle_var.get(), self.Brand_var.get(), self.Date_var.get(),
            self.Qty_var.get(), self.Price_var.get()
        ))
        conn.commit()
        messagebox.showinfo("Success", "Member has been inserted successfully")
        print("FirstName:", self.FirstName_var.get())
        print("SurName:", self.SurName_var.get())
        # Repeat for each field to verify values are as expected
        self.fetch_data()

    
    
        conn.close()

    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="jnj012004", database="musicdbms")
        cursor = conn.cursor()
        cursor.execute("update music set FirstName=%s, SurName=%s, Country=%s, City=%s, Address=%s, PostalCode=%s,EmailId=%s,ProductId=%s,ProductTitle=%s, Brand=%s, Date=%s, Qty=%s, Price=%s where MobileNo=%s",(
            self.FirstName_var.get(), self.SurName_var.get(), self.Country_var.get(),
            self.City_var.get(), self.Address_var.get(), self.PostalCode_var.get(),
            self.EmailId_var.get(),self.ProductId_var.get(),
            self.ProductTitle_var.get(), self.Brand_var.get(), self.Date_var.get(),
            self.Qty_var.get(), self.Price_var.get(),self.MobileNo_var.get()))
        
        conn.commit()
        self.fetch_data()
        self.reset()
        messagebox.showinfo("Success","Member has been updated")
        conn.close()

        








        

    def fetch_data(self):
        
        # Establishing connection to the MySQL database
        conn = mysql.connector.connect(
                host="localhost",        # Replace with your database host
                user="root",             # Replace with your database username
                password="jnj012004",     # Replace with your database password
                database="musicdbms"    # Replace with your database name
            )
        cursor = conn.cursor()

        # SQL query to retrieve data
        query = "SELECT * FROM music"
        cursor.execute(query)

        rows = cursor.fetchall()
        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())  # Clears existing data
            for row in rows:
                self.library_table.insert('', 'end', values=row)  # Insert each row into the Treeview
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.FirstName_var.set(row[0]),
        self.SurName_var.set(row[1]),
        self.Country_var.set(row[2]),
        self.City_var.set(row[3]),
        self.Address_var.set(row[4]),
        self.PostalCode_var.set(row[5]),
        self.MobileNo_var.set(row[6]),
        self.EmailId_var.set(row[7]),
        self.ProductId_var.set(row[8]),
        self.ProductTitle_var.set(row[9]),
        self.Brand_var.set(row[10]),
        self.Date_var.set(row[11]),
        self.Qty_var.set(row[12]),
        self.Price_var.set(row[13])


    def showData(self):
        self.txtBox.insert(END,"First Name\t\t"+self.FirstName_var.get()+"\n")
        self.txtBox.insert(END,"Sur Name\t\t"+self.SurName_var.get()+"\n")
        self.txtBox.insert(END,"Country\t\t"+self.Country_var.get()+"\n")
        self.txtBox.insert(END,"City\t\t"+self.City_var.get()+"\n")
        self.txtBox.insert(END,"Address\t\t"+self.Address_var.get()+"\n")
        self.txtBox.insert(END,"Postal Code\t\t"+self.PostalCode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No\t\t"+self.MobileNo_var.get()+"\n")
        self.txtBox.insert(END,"Email Id\t\t"+self.EmailId_var.get()+"\n")
        self.txtBox.insert(END,"Product Id\t\t"+self.ProductId_var.get()+"\n")
        self.txtBox.insert(END,"Product Title\t\t"+self.ProductTitle_var.get()+"\n")
        self.txtBox.insert(END,"Brand\t\t"+self.Brand_var.get()+"\n")
        self.txtBox.insert(END,"Date\t\t"+self.Date_var.get()+"\n")
        self.txtBox.insert(END,"Qty\t\t"+self.Qty_var.get()+"\n")
        self.txtBox.insert(END,"Price\t\t"+self.Price_var.get()+"\n")


    def reset(self):
        self.FirstName_var.set("")
        self.SurName_var.set("")
        self.Country_var.set("")
        self.City_var.set("")
        self.Address_var.set("")
        self.PostalCode_var.set("")
        self.MobileNo_var.set("")
        self.EmailId_var.set("")
        self.ProductId_var.set("")
        self.ProductTitle_var.set("")
        self.Brand_var.set("")
        self.Date_var.set("")
        self.Qty_var.set("")
        self.Price_var.set("")
        self.txtBox.delete("1.0",END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Music Shop Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.MobileNo_var.get()=="":
            messagebox.showerror("Error","Select ")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="jnj012004", database="musicdbms")
            cursor = conn.cursor()
            query="delete from music where MobileNo=%s"
            values=(self.MobileNo_var.get(),)
            cursor.execute(query,values)

            conn.commit()
            self.fetch_data()
            self.reset()
            messagebox.showinfo("Success","Member has been deleted")
            conn.close()

            





if __name__ == "__main__":
    root=Tk()
    obj=MusicShopDBMS(root)
    root.mainloop()