import tkinter as tk
from tkinter import *
from datetime import datetime
from tkinter import messagebox
import PIL
from PIL import ImageTk, Image
import pyodbc
conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
import tkinter.font as tkFont




class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        f1 = GradientFrame(self, borderwidth=0, relief="sunken")
        f2 = GradientFrame(self, "#DECBA4", "#3E5151", borderwidth=0, relief="sunken")
        f1.pack(side="top", fill="both", expand=True)
        f2.pack(side="bottom", fill="both", expand=True)

class GradientFrame(tk.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1="#DECBA4", color2="#3E5151", **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")

def homepage():
    
    def GButton_645_command():
        root.destroy()
        user_log()

    def GButton_238_command():
        root.destroy()
        admin_log()

    def GButton_240_command():
        root.destroy()
        admin_unsc()

    def GButton_239_command():
        root.destroy()
        admin_reg()

    def GButton_912_command():
        root.destroy()
        user_reg()

    def GButton_913_command():
        root.destroy()
        user_unsc()

    #setting title
    root=tk.Tk()
    root.title("Login page")
    #setting window size
    width=970
    height=437
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    bg = ImageTk.PhotoImage(Image.open("pic.png"))
    GLabel_326=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_326["font"] = ft
    GLabel_326["fg"] = "#333333"
    GLabel_326["justify"] = "center"
    GLabel_326["text"] = "label"
    GLabel_326["image"]=bg
    GLabel_326.place(x=0,y=0,width=970,height=437)

    GLabel_578=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_578["font"] = ft
    GLabel_578["bg"] = "#15161a"
    GLabel_578["fg"] = "#f4eded"
    GLabel_578["justify"] = "center"
    GLabel_578["text"] = "McQUEEN RENTALS"

    GLabel_578.place(x=320,y=30,width=380,height=45)

    GLabel_639=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_639["font"] = ft
    GLabel_639["bg"] = "#15161a"
    GLabel_639["fg"] = "#f4eded"
    GLabel_639["justify"] = "center"
    GLabel_639["text"] = "WELCOME!!"
    GLabel_639.place(x=380,y=110,width=220,height=30)

    GButton_645=tk.Button(root)
    GButton_645["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_645["font"] = ft
    GButton_645["fg"] = "#f3eeee"
    GButton_645["bg"] = "#f6382b"
    GButton_645["justify"] = "center"
    GButton_645["text"] = "Customer login"
    GButton_645.place(x=230,y=210,width=143,height=30)
    GButton_645["command"] = GButton_645_command

    GButton_912=tk.Button(root)
    GButton_912["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_912["font"] = ft
    GButton_912["fg"] = "#f3eeee"
    GButton_912["bg"] = "#f6382b"
    GButton_912["justify"] = "center"
    GButton_912["text"] = "Customer signup"
    GButton_912.place(x=440,y=210,width=141,height=30)
    GButton_912["command"] = GButton_912_command

    GButton_913=tk.Button(root)
    GButton_913["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_913["font"] = ft
    GButton_913["fg"] = "#f3eeee"
    GButton_913["bg"] = "#f6382b"
    GButton_913["justify"] = "center"
    GButton_913["text"] = "Customer unsubscribe"
    GButton_913.place(x=680,y=210,width=141,height=30)
    GButton_913["command"] = GButton_913_command

    GButton_238=tk.Button(root)
    GButton_238["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_238["font"] = ft
    GButton_238["fg"] = "#191616"
    GButton_238["bg"] = "#ffb800"
    GButton_238["justify"] = "center"
    GButton_238["text"] = "Admin login"
    GButton_238.place(x=230,y=290,width=141,height=30)
    GButton_238["command"] = GButton_238_command

    GButton_239=tk.Button(root)
    GButton_239["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_239["font"] = ft
    GButton_239["fg"] = "#191616"
    GButton_239["bg"] = "#ffb800"
    GButton_239["justify"] = "center"
    GButton_239["text"] = "Admin signup"
    GButton_239.place(x=440,y=290,width=141,height=30)
    GButton_239["command"] = GButton_239_command

    GButton_240=tk.Button(root)
    GButton_240["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_240["font"] = ft
    GButton_240["fg"] = "#191616"
    GButton_240["bg"] = "#ffb800"
    GButton_240["justify"] = "center"
    GButton_240["text"] = "Admin unsubscribe"
    GButton_240.place(x=680,y=290,width=141,height=30)
    GButton_240["command"] = GButton_240_command

    GLabel_671=tk.Label(root)
    ft = tkFont.Font(family='Times',size=14)
    GLabel_671["font"] = ft
    GLabel_671["fg"] = "#f3eeee"
    GLabel_671["bg"] = "#f6382b"
    GLabel_671["justify"] = "center"
    GLabel_671["text"] = "For customers"
    GLabel_671.place(x=60,y=210,width=117,height=30)

    GLabel_698=tk.Label(root)
    ft = tkFont.Font(family='Times',size=14)
    GLabel_698["font"] = ft
    GLabel_698["fg"] = "#191616"
    GLabel_698["bg"] = "#ffb800"
    GLabel_698["justify"] = "center"
    GLabel_698["text"] = "For admins"
    GLabel_698.place(x=60,y=290,width=115,height=30)
    root.mainloop()

def user_reg():
    def add_user():
        uname=str(GLineEdit_320.get())
        pwd=str(GLineEdit_269.get())
        if len(pwd)<8:
            messagebox.showinfo("Error","Password should be atleast 8 characters")
            return
        add=str(GLineEdit_321.get())
        phno=str(GLineEdit_322.get())
        if len(phno)!=10:
            messagebox.showinfo("Invalid","Phone number should be 10 digits")
            return
        conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
        cur=conn.cursor()
        cur.execute("insert into customer(c_id,username,password,address,contact) values(customer_seq.nextval,'%s','%s','%s','%s')"%(uname,pwd,add,phno))
        cur.commit()
        root2=tk.Tk()

        root2.title("Successful registration")
        #setting window size
        Example(root2).pack(fill="both", expand=True)
        width=300
        height=165
        screenwidth = root2.winfo_screenwidth()
        screenheight = root2.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root2.geometry(alignstr)
        root2.resizable(width=False, height=False)

        GLabel_536=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_536["font"] = ft
        GLabel_536["fg"] = "#333333"
        GLabel_536["justify"] = "center"
        GLabel_536["text"] = "Customer registered successfully!!"
        GLabel_536.place(x=30,y=60,width=241,height=36)

        root2.mainloop()

    def GButton_615_command():
        root.destroy()
        homepage()

    root=tk.Tk()
    #setting title
    root.title("User registration")
    #<color> root.configure(bg='')
    #setting window size
    width=486
    height=520
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    bg = ImageTk.PhotoImage(Image.open("pic.png"))
    GLabel_326=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_326["font"] = ft
    GLabel_326["fg"] = "#333333"
    GLabel_326["justify"] = "center"
    GLabel_326["text"] = "label"
    GLabel_326["image"]=bg
    GLabel_326.place(x=0,y=0,width=486,height=520)

    GLabel_578=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_578["font"] = ft
    GLabel_578["bg"] = "#15161a"
    GLabel_578["fg"] = "#f4eded"
    GLabel_578["justify"] = "center"
    GLabel_578["text"] = "McQUEEN RENTALS"
    GLabel_578.place(x=50,y=30,width=400,height=47)

    GLabel_907=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_907["font"] = ft
    GLabel_907["fg"] = "#333333"
    GLabel_907["justify"] = "center"
    GLabel_907["text"] = "USERNAME"
    GLabel_907.place(x=90,y=150,width=131,height=30)

    GLabel_818=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_818["font"] = ft
    GLabel_818["fg"] = "#333333"
    GLabel_818["justify"] = "center"
    GLabel_818["text"] = "PASSWORD"
    GLabel_818.place(x=90,y=230,width=131,height=30)

    GLabel_819=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_819["font"] = ft
    GLabel_819["fg"] = "#333333"
    GLabel_819["justify"] = "center"
    GLabel_819["text"] = "ADDRESS"
    GLabel_819.place(x=90,y=310,width=131,height=30)

    GLabel_820=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_820["font"] = ft
    GLabel_820["fg"] = "#333333"
    GLabel_820["justify"] = "center"
    GLabel_820["text"] = "PHONE NUMBER"
    GLabel_820.place(x=90,y=390,width=131,height=30)

    GButton_616=tk.Button(root)
    GButton_616["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_616["font"] = ft
    GButton_616["fg"] = "#000000"
    GButton_616["justify"] = "center"
    GButton_616["text"] = "Submit"
    GButton_616.place(x=120,y=450,width=115,height=30)
    GButton_616["command"] = add_user

    GButton_615=tk.Button(root)
    GButton_615["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_615["font"] = ft
    GButton_615["fg"] = "#000000"
    GButton_615["justify"] = "center"
    GButton_615["text"] = "Go to homepage"
    GButton_615.place(x=260,y=450,width=115,height=30)
    GButton_615["command"] = GButton_615_command

    GLineEdit_320=tk.Entry(root)
    GLineEdit_320["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_320["font"] = ft
    GLineEdit_320["fg"] = "#333333"
    GLineEdit_320["justify"] = "center"
    GLineEdit_320["text"] = ""
    GLineEdit_320.place(x=250,y=150,width=127,height=30)
    
    GLineEdit_269=tk.Entry(root)
    GLineEdit_269["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_269["font"] = ft
    GLineEdit_269["fg"] = "#333333"
    GLineEdit_269["justify"] = "center"
    GLineEdit_269["text"] = ""
    GLineEdit_269["show"]='*'
    GLineEdit_269.place(x=250,y=230,width=128,height=30)

    GLineEdit_321=tk.Entry(root)
    GLineEdit_321["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_321["font"] = ft
    GLineEdit_321["fg"] = "#333333"
    GLineEdit_321["justify"] = "center"
    GLineEdit_321["text"] = ""
    GLineEdit_321.place(x=250,y=310,width=127,height=30)

    GLineEdit_322=tk.Entry(root)
    GLineEdit_322["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_322["font"] = ft
    GLineEdit_322["fg"] = "#333333"
    GLineEdit_322["justify"] = "center"
    GLineEdit_322["text"] = ""
    GLineEdit_322.place(x=250,y=390,width=127,height=30)

    GLabel_553=tk.Label(root)
    ft = tkFont.Font(family='Times',size=14)
    GLabel_553["font"] = ft
    GLabel_553["bg"] = "#15161a"
    GLabel_553["fg"] = "#f4eded"
    GLabel_553["justify"] = "center"
    GLabel_553["text"] = "Enter new customer details"
    GLabel_553.place(x=140,y=90,width=210,height=30)

    root.mainloop()

def user_unsc():
    def del_user():
        uname=str(GLineEdit_320.get())
        pwd=str(GLineEdit_269.get())
        if len(pwd)<8:
            messagebox.showinfo("Error","Password should be atleast 8 characters")
        conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
        cur=conn.cursor()
        cur.execute("select username,password from customer where username='%s' and password='%s'"%(uname,pwd))
        x=cur.fetchone()
        if x:
            conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
            cur=conn.cursor()
            cur.execute("select * from rental where return_date is null and c_id=(select c_id from customer where username='%s' and password='%s')"%(uname,pwd))
            ch=cur.fetchone()
            if not ch:
                cur.execute("delete from customer where username='%s' and password='%s'"%(uname,pwd))
                cur.commit()
                root2=tk.Tk()

                root2.title("Unsubscribe successful")
                #setting window size
                Example(root2).pack(fill="both", expand=True)
                width=300
                height=165
                screenwidth = root2.winfo_screenwidth()
                screenheight = root2.winfo_screenheight()
                alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                root2.geometry(alignstr)
                root2.resizable(width=False, height=False)         

                GLabel_536=tk.Label(root2)
                ft = tkFont.Font(family='Times',size=12)
                GLabel_536["font"] = ft
                GLabel_536["bg"] = "#15161a"
                GLabel_536["fg"] = "#f4eded"
                GLabel_536["justify"] = "center"
                GLabel_536["text"] = "Sorry to see you leave"
                GLabel_536.place(x=30,y=60,width=241,height=36)

                root2.mainloop()
            else:
                messagebox.showinfo("Invalid","Please return the car you have currently rented")
        else:
            root2=tk.Tk()

            root2.title("Unsuccessful unsubscribe")
            Example(root2).pack(fill="both", expand=True)
            #setting window size
            width=300
            height=165
            screenwidth = root2.winfo_screenwidth()
            screenheight = root2.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root2.geometry(alignstr)
            root2.resizable(width=False, height=False)

            GLabel_536=tk.Label(root2)
            ft = tkFont.Font(family='Times',size=14)
            GLabel_536["font"] = ft
            GLabel_536["bg"] = "#15161a"
            GLabel_536["fg"] = "#f4eded"
            GLabel_536["justify"] = "center"
            GLabel_536["text"] = "Wrong credentials!!"
            GLabel_536.place(x=30,y=60,width=241,height=36)

            root2.mainloop()


    def GButton_615_command():
        root.destroy()
        homepage()

    root=tk.Tk()
    #setting title
    root.title("Customer unsubscribe")
    #<color> root.configure(bg='')
    #setting window size
    width=486
    height=370
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    bg = ImageTk.PhotoImage(Image.open("pic.png"))
    GLabel_326=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_326["font"] = ft
    GLabel_326["fg"] = "#333333"
    GLabel_326["justify"] = "center"
    GLabel_326["text"] = "label"
    GLabel_326["image"]=bg
    GLabel_326.place(x=0,y=0,width=486,height=370)

    GLabel_578=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_578["font"] = ft
    GLabel_578["bg"] = "#15161a"
    GLabel_578["fg"] = "#f4eded"
    GLabel_578["justify"] = "center"
    GLabel_578["text"] = "McQUEEN RENTALS"
    GLabel_578.place(x=50,y=30,width=400,height=47)

    GLabel_907=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_907["font"] = ft
    GLabel_907["fg"] = "#333333"
    GLabel_907["justify"] = "center"
    GLabel_907["text"] = "USERNAME"
    GLabel_907.place(x=90,y=150,width=131,height=30)

    GLabel_818=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_818["font"] = ft
    GLabel_818["fg"] = "#333333"
    GLabel_818["justify"] = "center"
    GLabel_818["text"] = "PASSWORD"
    GLabel_818.place(x=90,y=230,width=131,height=30)

    GButton_616=tk.Button(root)
    GButton_616["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_616["font"] = ft
    GButton_616["fg"] = "#000000"
    GButton_616["justify"] = "center"
    GButton_616["text"] = "Submit"
    GButton_616.place(x=120,y=300,width=115,height=30)
    GButton_616["command"] = del_user

    GButton_615=tk.Button(root)
    GButton_615["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_615["font"] = ft
    GButton_615["fg"] = "#000000"
    GButton_615["justify"] = "center"
    GButton_615["text"] = "Go to homepage"
    GButton_615.place(x=260,y=300,width=115,height=30)
    GButton_615["command"] = GButton_615_command

    GLineEdit_320=tk.Entry(root)
    GLineEdit_320["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_320["font"] = ft
    GLineEdit_320["fg"] = "#333333"
    GLineEdit_320["justify"] = "center"
    GLineEdit_320["text"] = ""
    GLineEdit_320.place(x=250,y=150,width=127,height=30)
    
    GLineEdit_269=tk.Entry(root)
    GLineEdit_269["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_269["font"] = ft
    GLineEdit_269["fg"] = "#333333"
    GLineEdit_269["justify"] = "center"
    GLineEdit_269["text"] = ""
    GLineEdit_269["show"]='*'
    GLineEdit_269.place(x=250,y=230,width=128,height=30)

    GLabel_553=tk.Label(root)
    ft = tkFont.Font(family='Times',size=14)
    GLabel_553["font"] = ft
    GLabel_553["bg"] = "#15161a"
    GLabel_553["fg"] = "#f4eded"
    GLabel_553["justify"] = "center"
    GLabel_553["text"] = "Enter customer details"
    GLabel_553.place(x=140,y=90,width=210,height=30)

    root.mainloop()









def user_homepage():

    def payment():

        conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
        cur=conn.cursor()
        cur.execute("select * from rental where return_date is null and c_id=(select c_id from customer where username='%s' and password='%s')"%(uname,pwd))
        c=cur.fetchall()
        #print(c)
        if c:
            def GButton_792_command():
                gaid=int(GLineEdit_465.get())
                conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
                cur=conn.cursor()
                cur.execute("select a_id from admin where a_id='%d'"%(gaid))
                ch=cur.fetchone()
                if ch:
                    root2=tk.Tk()
                    #setting title
                    root2.title("Payment")
                    Example(root2).pack(fill="both", expand=True)
                    #setting window size
                    width=530
                    height=368
                    screenwidth = root2.winfo_screenwidth()
                    screenheight = root2.winfo_screenheight()
                    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                    root2.geometry(alignstr)
                    root2.resizable(width=False, height=False)
                    
                    conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
                    cur=conn.cursor()
                    cur.execute("select * from rental where return_date is null and c_id=(select c_id from customer where username='%s' and password='%s')"%(uname,pwd))
                    po=cur.fetchone()
                    print(po)
                    conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
                    cur=conn.cursor()
                    cur.execute("update rental set return_date=sysdate where c_id=(select c_id from customer where username='%s' and password='%s')"%(uname,pwd))
                    cur.commit()

                    GLabel_735=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=16)
                    GLabel_735["font"] = ft
                    GLabel_735["bg"] = "#15161a"
                    GLabel_735["fg"] = "#f4eded"
                    GLabel_735["justify"] = "center"
                    GLabel_735["text"] = "PAYMENT DETAILS"
                    GLabel_735.place(x=120,y=30,width=263,height=34)

                    GLabel_545=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=10)
                    GLabel_545["font"] = ft
                    GLabel_545["fg"] = "#333333"
                    GLabel_545["justify"] = "center"
                    GLabel_545["text"] = "Car ID"
                    GLabel_545.place(x=150,y=80,width=97,height=30)

                    GLabel_233=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=10)
                    GLabel_233["font"] = ft
                    GLabel_233["fg"] = "#333333"
                    GLabel_233["justify"] = "center"
                    GLabel_233["text"] = "Rental Date"
                    GLabel_233.place(x=150,y=120,width=95,height=32)

                    GLabel_234=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=10)
                    GLabel_234["font"] = ft
                    GLabel_234["fg"] = "#333333"
                    GLabel_234["justify"] = "center"
                    GLabel_234["text"] = "Return Date"
                    GLabel_234.place(x=150,y=160,width=95,height=32)

                    GLabel_235=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=10)
                    GLabel_235["font"] = ft
                    GLabel_235["fg"] = "#333333"
                    GLabel_235["justify"] = "center"
                    GLabel_235["text"] = "Amount"
                    GLabel_235.place(x=150,y=200,width=95,height=32)

                    GLabel_235=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=10)
                    GLabel_235["font"] = ft
                    GLabel_235["fg"] = "#333333"
                    GLabel_235["justify"] = "center"
                    GLabel_235["text"] = po[3]
                    GLabel_235.place(x=250,y=80,width=95,height=32)

                    GLabel_236=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=10)
                    GLabel_236["font"] = ft
                    GLabel_236["fg"] = "#333333"
                    GLabel_236["justify"] = "center"
                    GLabel_236["text"] = po[1].strftime("%m/%d/%Y, %H:%M:%S")
                    GLabel_236.place(x=250,y=120,width=175,height=32)

                    po[2]=datetime.now()

                    GLabel_237=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=10)
                    GLabel_237["font"] = ft
                    GLabel_237["fg"] = "#333333"
                    GLabel_237["justify"] = "center"
                    GLabel_237["text"] = po[2].strftime("%m/%d/%Y, %H:%M:%S")
                    GLabel_237.place(x=250,y=160,width=175,height=32)

                    diff=(po[2]-po[1]).total_seconds()//3600
                    #diff_hrs=diff.totalseconds()/3600

                    GLabel_237=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=10)
                    GLabel_237["font"] = ft
                    GLabel_237["fg"] = "#333333"
                    GLabel_237["justify"] = "center"
                    GLabel_237["text"] =diff*100+100
                    GLabel_237.place(x=250,y=200,width=95,height=32)

                    GLabel_238=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=10)
                    GLabel_238["font"] = ft
                    GLabel_238["bg"] = "#15161a"
                    GLabel_238["fg"] = "#f4eded"
                    GLabel_238["justify"] = "center"
                    GLabel_238["text"] ="THANK YOU FOR RENTING FROM US!"
                    GLabel_238.place(x=120,y=270,width=300,height=32)

                    conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
                    cur=conn.cursor()
                    cur.execute("select c_id from customer where username='%s' and password='%s'"%(uname,pwd))
                    cid=int(cur.fetchone()[0])
                    rid=int(po[0])
                    cur.execute("insert into payment values(payment_seq.nextval,'%d','%d','%d',sysdate,'%d')"%(gaid,cid,rid,diff*100+100))
                    cur.commit()
                else:
                    root2=tk.Tk()
                    root2.title("Invalid")
                    Example(root2).pack(fill="both", expand=True)
                    #setting window size
                    width=300
                    height=165
                    screenwidth = root2.winfo_screenwidth()
                    screenheight = root2.winfo_screenheight()
                    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                    root2.geometry(alignstr)
                    root2.resizable(width=False, height=False)
                    

                    GLabel_536=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=14)
                    GLabel_536["font"] = ft
                    GLabel_536["bg"] = "#15161a"
                    GLabel_536["fg"] = "#f4eded"
                    GLabel_536["justify"] = "center"
                    GLabel_536["text"] = "Wrong Admin ID"
                    GLabel_536.place(x=30,y=60,width=241,height=36)

                    root2.mainloop()

            root3=tk.Tk()
            root3.title("Payment")
            Example(root3).pack(fill="both", expand=True)
            #setting window size
            width=400
            height=200
            screenwidth = root3.winfo_screenwidth()
            screenheight = root3.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root3.geometry(alignstr)
            root3.resizable(width=False, height=False)

            GLabel_769=tk.Label(root3)
            ft = tkFont.Font(family='Times',size=10)
            GLabel_769["font"] = ft
            GLabel_769["fg"] = "#333333"
            GLabel_769["justify"] = "center"
            GLabel_769["text"] = "Enter Admin ID"
            GLabel_769.place(x=60,y=90,width=120,height=30)

            GLineEdit_465=tk.Entry(root3)
            GLineEdit_465["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            GLineEdit_465["font"] = ft
            GLineEdit_465["fg"] = "#333333"
            GLineEdit_465["justify"] = "center"
            GLineEdit_465["text"] = ""
            GLineEdit_465.place(x=200,y=90,width=115,height=30)

            GLabel_99=tk.Label(root3)
            ft = tkFont.Font(family='Times',size=16)
            GLabel_99["font"] = ft
            GLabel_99["fg"] = "#333333"
            GLabel_99["justify"] = "center"
            GLabel_99["text"] = "PAYMENT"
            GLabel_99.place(x=110,y=30,width=158,height=31)

            GButton_792=tk.Button(root3)
            GButton_792["bg"] = "#efefef"
            ft = tkFont.Font(family='Times',size=10)
            GButton_792["font"] = ft
            GButton_792["fg"] = "#000000"
            GButton_792["justify"] = "center"
            GButton_792["text"] = "Proceed"
            GButton_792.place(x=140,y=150,width=84,height=30)
            GButton_792["command"] = GButton_792_command

        else:
            root2=tk.Tk()

            root2.title("Unsuccessful return")
            Example(root2).pack(fill="both", expand=True)
            #setting window size
            width=300
            height=165
            screenwidth = root2.winfo_screenwidth()
            screenheight = root2.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root2.geometry(alignstr)
            root2.resizable(width=False, height=False)

            GLabel_536=tk.Label(root2)
            ft = tkFont.Font(family='Times',size=14)
            GLabel_536["font"] = ft
            GLabel_536["fg"] = "#333333"
            GLabel_536["justify"] = "center"
            GLabel_536["text"] = "You have not rented a car"
            GLabel_536.place(x=30,y=60,width=241,height=36)

            root2.mainloop()

    def book():
        def GButton_792_command():
            gcarid=int(GLineEdit_465.get())
            conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
            cur=conn.cursor()
            cur.execute("select car_id from car_desc")
            c=cur.fetchall()
            qw=[]
            for i in range(len(c)):
                qw.append(int(c[i][0]))
            if gcarid in qw:
                conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
                cur=conn.cursor()
                cur.execute("select car_id from rental where return_date is null")
                allcid=cur.fetchall()
                print(allcid)
                qwe=[]
                for i in range(len(allcid)):
                    qwe.append(int(allcid[i][0]))
                print(qwe)
                if gcarid in qwe:
                    #setting title
                    root2=tk.Tk()
                    root2.title("Unsuccessful")
                    Example(root2).pack(fill="both", expand=True)
                    #setting window size
                    width=356
                    height=214
                    screenwidth = root2.winfo_screenwidth()
                    screenheight = root2.winfo_screenheight()
                    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                    root2.geometry(alignstr)
                    root2.resizable(width=False, height=False)

                    GLabel_459=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=14)
                    GLabel_459["font"] = ft
                    GLabel_459["fg"] = "#333333"
                    GLabel_459["justify"] = "center"
                    GLabel_459["text"] = "Sorry! Car already booked"
                    GLabel_459.place(x=80,y=50,width=204,height=30)

                    GLabel_476=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=14)
                    GLabel_476["font"] = ft
                    GLabel_476["fg"] = "#333333"
                    GLabel_476["justify"] = "center"
                    GLabel_476["text"] = "Choose another car"
                    GLabel_476.place(x=90,y=110,width=169,height=37)
                    root2.mainloop()
                else:
                    conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
                    cur=conn.cursor()
                    c=cur.execute("select c_id from customer where username='%s' and password='%s'"%(uname,pwd))
                    fcid=int(c.fetchone()[0])
                    cur.execute("insert into rental(r_id,rental_date,car_id,c_id) values(Rental_seq.nextval,sysdate,'%d','%d')"%(gcarid,fcid))
                    cur.commit()
                    #setting title
                    root2=tk.Tk()
                    root2.title("Success")
                    Example(root2).pack(fill="both", expand=True)
                    #setting window size
                    width=356
                    height=215
                    screenwidth = root2.winfo_screenwidth()
                    screenheight = root2.winfo_screenheight()
                    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                    root2.geometry(alignstr)
                    root2.resizable(width=False, height=False)

                    GLabel_213=tk.Label(root2)
                    ft = tkFont.Font(family='Times',size=14)
                    GLabel_213["font"] = ft
                    GLabel_213["fg"] = "#333333"
                    GLabel_213["justify"] = "center"
                    GLabel_213["text"] = "Car booked successfully!"
                    GLabel_213.place(x=70,y=90,width=216,height=30)
                    root2.mainloop()
            else:
                messagebox.showinfo("Invalid","Invalid Car ID")
                root.lift

        #setting title
        root=tk.Tk()
        root.title("Book")
        Example(root).pack(fill="both", expand=True)
        #setting window size
        width=402
        height=215
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_769=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_769["font"] = ft
        GLabel_769["fg"] = "#333333"
        GLabel_769["justify"] = "center"
        GLabel_769["text"] = "Enter Car ID"
        GLabel_769.place(x=60,y=90,width=120,height=30)

        GLineEdit_465=tk.Entry(root)
        GLineEdit_465["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_465["font"] = ft
        GLineEdit_465["fg"] = "#333333"
        GLineEdit_465["justify"] = "center"
        GLineEdit_465["text"] = ""
        GLineEdit_465.place(x=200,y=90,width=115,height=30)

        GLabel_99=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_99["font"] = ft
        GLabel_99["bg"] = "#15161a"
        GLabel_99["fg"] = "#f4eded"
        GLabel_99["justify"] = "center"
        GLabel_99["text"] = "CAR BOOKING"
        GLabel_99.place(x=110,y=30,width=158,height=31)

        GButton_792=tk.Button(root)
        GButton_792["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_792["font"] = ft
        GButton_792["fg"] = "#000000"
        GButton_792["justify"] = "center"
        GButton_792["text"] = "Book"
        GButton_792.place(x=140,y=150,width=84,height=30)
        GButton_792["command"] = GButton_792_command


    def disp():
        root=tk.Tk()
        root.title("Display")
        #setting window size
        width=800
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        bg = ImageTk.PhotoImage(Image.open("pic.png"))
        GLabel_326=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_326["font"] = ft
        GLabel_326["fg"] = "#333333"
        GLabel_326["justify"] = "center"
        GLabel_326["text"] = "label"
        GLabel_326["image"]=bg
        GLabel_326.place(x=0,y=0,width=800,height=500)

        conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
        cur=conn.cursor()
        cur.execute('select * from car_desc')
        c=cur.fetchall()        
        cid=Label(root,text='Car ID',width=13)
        cid.place(x=60,y=10)
        pno=Label(root,text='Plate No',width=13)
        pno.place(x=160,y=10)
        pno=Label(root,text='Name',width=13)
        pno.place(x=260,y=10)
        pno=Label(root,text='Capacity',width=13)
        pno.place(x=360,y=10)
        pno=Label(root,text='Milage',width=13)
        pno.place(x=460,y=10)
        pno=Label(root,text='Name',width=13)
        pno.place(x=560,y=10)
        pno=Label(root,text='Review',width=13)
        pno.place(x=660,y=10)

        k=1
        for i in c:
            for j in range(len(i)):
                e=Label(root,text=i[j],width=13)
                e.place(x=j*100+60,y=30*k)
            k+=1
        b=Button(root,text='Proceed to Book',command=book)
        b.place(x=(j/2-2)*100+60,y=30*k)
        h=Button(root,text='Go to homepage',command=user_homepage)
        h.place(x=(j/2+2)*100,y=30*k)
        root.mainloop()

    def GButton_616_command():
        root.destroy()
        payment()
    def GButton_617_command():
        root.destroy()
        disp()
    root=tk.Tk()
    root.title("Homepage")
    Example(root).pack(fill="both", expand=True)
    width=500
    height=400
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    GLabel_578=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_578["font"] = ft
    GLabel_578["bg"] = "#15161a"
    GLabel_578["fg"] = "#f4eded"
    GLabel_578["justify"] = "center"
    GLabel_578["text"] = "McQUEEN RENTALS"
    GLabel_578.place(x=50,y=30,width=400,height=47)

    GLabel_639=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_639["font"] = ft
    GLabel_639["bg"] = "#15161a"
    GLabel_639["fg"] = "#f4eded"
    GLabel_639["justify"] = "center"
    GLabel_639["text"] = "WELCOME!!"
    GLabel_639.place(x=150,y=110,width=220,height=30)

    GButton_616=tk.Button(root)
    GButton_616["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_616["font"] = ft
    GButton_616["fg"] = "#000000"
    GButton_616["justify"] = "center"
    GButton_616["text"] = "Return car"
    GButton_616.place(x=120,y=250,width=115,height=30)
    GButton_616["command"] = GButton_616_command

    GButton_617=tk.Button(root)
    GButton_617["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_617["font"] = ft
    GButton_617["fg"] = "#000000"
    GButton_617["justify"] = "center"
    GButton_617["text"] = "Rent car"
    GButton_617.place(x=260,y=250,width=115,height=30)
    GButton_617["command"] = GButton_617_command

uname=None
pwd=None

def user_log():
    def chk_user():
        global uname,pwd
        uname=str(GLineEdit_320.get())
        pwd=str(GLineEdit_269.get())
        if len(pwd)<8:
            messagebox.showinfo("Error","Password should be atleast 8 characters")
        conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
        cur=conn.cursor()
        cur.execute("select username,password from customer where username='%s' and password='%s'"%(uname,pwd))
        x=cur.fetchone()
        if x:
            root.destroy()
            user_homepage()
        else:
            root2=tk.Tk()

            root2.title("Unsuccessful login")
            Example(root2).pack(fill="both", expand=True)
            #setting window size
            width=300
            height=165
            screenwidth = root2.winfo_screenwidth()
            screenheight = root2.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root2.geometry(alignstr)
            root2.resizable(width=False, height=False)

            GLabel_536=tk.Label(root2)
            ft = tkFont.Font(family='Times',size=14)
            GLabel_536["font"] = ft
            GLabel_536["bg"] = "#15161a"
            GLabel_536["fg"] = "#f4eded"
            GLabel_536["justify"] = "center"
            GLabel_536["text"] = "Wrong credentials!!"
            GLabel_536.place(x=30,y=60,width=241,height=36)

            root2.mainloop()

    def GButton_617_command():
        root.destroy()
        homepage()

    root=tk.Tk()
    #setting title
    root.title("Customer login")
    #<color> root.configure(bg='')
    #setting window size
    width=486
    height=376
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    bg = ImageTk.PhotoImage(Image.open("pic.png"))
    GLabel_326=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_326["font"] = ft
    GLabel_326["fg"] = "#333333"
    GLabel_326["justify"] = "center"
    GLabel_326["text"] = "label"
    GLabel_326["image"]=bg
    GLabel_326.place(x=0,y=0,width=486,height=376)

    GLabel_578=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_578["font"] = ft
    GLabel_578["bg"] = "#15161a"
    GLabel_578["fg"] = "#f4eded"
    GLabel_578["justify"] = "center"
    GLabel_578["text"] = "McQUEEN RENTALS"
    GLabel_578.place(x=50,y=30,width=400,height=47)

    GLabel_907=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_907["font"] = ft
    GLabel_907["fg"] = "#333333"
    GLabel_907["justify"] = "center"
    GLabel_907["text"] = "USERNAME"
    GLabel_907.place(x=90,y=150,width=131,height=30)

    GLabel_818=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_818["font"] = ft
    GLabel_818["fg"] = "#333333"
    GLabel_818["justify"] = "center"
    GLabel_818["text"] = "PASSWORD"
    GLabel_818.place(x=90,y=230,width=131,height=30)

    GButton_616=tk.Button(root)
    GButton_616["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_616["font"] = ft
    GButton_616["fg"] = "#000000"
    GButton_616["justify"] = "center"
    GButton_616["text"] = "Submit"
    GButton_616.place(x=120,y=300,width=115,height=30)
    GButton_616["command"] = chk_user

    GButton_617=tk.Button(root)
    GButton_617["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_617["font"] = ft
    GButton_617["fg"] = "#000000"
    GButton_617["justify"] = "center"
    GButton_617["text"] = "Go to homepage"
    GButton_617.place(x=260,y=300,width=115,height=30)
    GButton_617["command"] = GButton_617_command


    GLineEdit_269=tk.Entry(root)
    GLineEdit_269["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_269["font"] = ft
    GLineEdit_269["fg"] = "#333333"
    GLineEdit_269["justify"] = "center"
    GLineEdit_269["text"] = ""
    GLineEdit_269["show"]='*'
    GLineEdit_269.place(x=250,y=230,width=128,height=30)

    GLineEdit_320=tk.Entry(root)
    GLineEdit_320["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_320["font"] = ft
    GLineEdit_320["fg"] = "#333333"
    GLineEdit_320["justify"] = "center"
    GLineEdit_320["text"] = ""
    GLineEdit_320.place(x=250,y=150,width=127,height=30)

    GLabel_553=tk.Label(root)
    ft = tkFont.Font(family='Times',size=14)
    GLabel_553["font"] = ft
    GLabel_553["bg"] = "#15161a"
    GLabel_553["fg"] = "#f4eded"
    GLabel_553["justify"] = "center"
    GLabel_553["text"] = "Enter customer details"
    GLabel_553.place(x=140,y=90,width=200,height=30)

    root.mainloop()


def admin_homepage():
    def GButton_740_command():
        
        def add_car():
            pno=str(GLineEdit_320.get())
            mod=str(GLineEdit_269.get())
            cap=int(GLineEdit_321.get())
            mil=float(GLineEdit_322.get())
            nam=str(GLineEdit_323.get())
            rev=float(GLineEdit_324.get())
            conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
            cur=conn.cursor()
            cur.execute("insert into car_desc values(car_desc_seq.nextval,'%s','%s','%d','%d','%s','%f')"%(pno,mod,cap,mil,nam,rev))
            cur.commit()

            root2.destroy()
            root3=tk.Tk()
            root3.title("New car")
            Example(root3).pack(fill="both", expand=True)
            #<color> root.configure(bg='')
            #setting window size
            width=300
            height=165
            screenwidth = root3.winfo_screenwidth()
            screenheight = root3.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root3.geometry(alignstr)
            root3.resizable(width=False, height=False)
            

            GLabel_907=tk.Label(root3)
            ft = tkFont.Font(family='Times',size=12)
            GLabel_907["font"] = ft
            GLabel_907["bg"] = "#15161a"
            GLabel_907["fg"] = "#f4eded"
            GLabel_907["justify"] = "center"
            GLabel_907["text"] = "New car added!"
            GLabel_907.place(x=90,y=50,width=131,height=30)
            root3.mainloop()

        root2=tk.Tk()
        #setting title
        root2.title("New car")
        Example(root2).pack(fill="both", expand=True)
        #<color> root.configure(bg='')
        #setting window size
        width=486
        height=650
        screenwidth = root2.winfo_screenwidth()
        screenheight = root2.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root2.geometry(alignstr)
        root2.resizable(width=False, height=False)

        GLabel_578=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_578["font"] = ft
        GLabel_578["bg"] = "#15161a"
        GLabel_578["fg"] = "#f4eded"
        GLabel_578["justify"] = "center"
        GLabel_578["text"] = "McQUEEN RENTALS"
        GLabel_578.place(x=50,y=30,width=400,height=47)

        GLabel_907=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_907["font"] = ft
        GLabel_907["fg"] = "#333333"
        GLabel_907["justify"] = "center"
        GLabel_907["text"] = "PLATE NUMBER"
        GLabel_907.place(x=90,y=150,width=131,height=30)

        GLabel_818=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_818["font"] = ft
        GLabel_818["fg"] = "#333333"
        GLabel_818["justify"] = "center"
        GLabel_818["text"] = "MODEL"
        GLabel_818.place(x=90,y=230,width=131,height=30)

        GLabel_819=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_819["font"] = ft
        GLabel_819["fg"] = "#333333"
        GLabel_819["justify"] = "center"
        GLabel_819["text"] = "CAPACITY"
        GLabel_819.place(x=90,y=310,width=131,height=30)

        GLabel_820=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_820["font"] = ft
        GLabel_820["fg"] = "#333333"
        GLabel_820["justify"] = "center"
        GLabel_820["text"] = "MILEAGE"
        GLabel_820.place(x=90,y=390,width=131,height=30)

        GLabel_821=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_821["font"] = ft
        GLabel_821["fg"] = "#333333"
        GLabel_821["justify"] = "center"
        GLabel_821["text"] = "NAME"
        GLabel_821.place(x=90,y=460,width=131,height=30)

        GLabel_822=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_822["font"] = ft
        GLabel_822["fg"] = "#333333"
        GLabel_822["justify"] = "center"
        GLabel_822["text"] = "REVIEW"
        GLabel_822.place(x=90,y=530,width=131,height=30)

        GButton_616=tk.Button(root2)
        GButton_616["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_616["font"] = ft
        GButton_616["fg"] = "#000000"
        GButton_616["justify"] = "center"
        GButton_616["text"] = "Submit"
        GButton_616.place(x=120,y=590,width=115,height=30)
        GButton_616["command"] = add_car

        GButton_615=tk.Button(root2)
        GButton_615["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_615["font"] = ft
        GButton_615["fg"] = "#000000"
        GButton_615["justify"] = "center"
        GButton_615["text"] = "Go to homepage"
        GButton_615.place(x=260,y=590,width=125,height=30)
        GButton_615["command"] = root.lift

        GLineEdit_320=tk.Entry(root2)
        GLineEdit_320["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_320["font"] = ft
        GLineEdit_320["fg"] = "#333333"
        GLineEdit_320["justify"] = "center"
        GLineEdit_320["text"] = ""
        GLineEdit_320.place(x=250,y=150,width=127,height=30)
        
        GLineEdit_269=tk.Entry(root2)
        GLineEdit_269["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_269["font"] = ft
        GLineEdit_269["fg"] = "#333333"
        GLineEdit_269["justify"] = "center"
        GLineEdit_269["text"] = ""
        GLineEdit_269.place(x=250,y=230,width=128,height=30)

        GLineEdit_321=tk.Entry(root2)
        GLineEdit_321["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_321["font"] = ft
        GLineEdit_321["fg"] = "#333333"
        GLineEdit_321["justify"] = "center"
        GLineEdit_321["text"] = ""
        GLineEdit_321.place(x=250,y=310,width=127,height=30)

        GLineEdit_322=tk.Entry(root2)
        GLineEdit_322["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_322["font"] = ft
        GLineEdit_322["fg"] = "#333333"
        GLineEdit_322["justify"] = "center"
        GLineEdit_322["text"] = ""
        GLineEdit_322.place(x=250,y=390,width=127,height=30)

        GLineEdit_323=tk.Entry(root2)
        GLineEdit_323["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_323["font"] = ft
        GLineEdit_323["fg"] = "#333333"
        GLineEdit_323["justify"] = "center"
        GLineEdit_323["text"] = ""
        GLineEdit_323.place(x=250,y=460,width=127,height=30)

        GLineEdit_324=tk.Entry(root2)
        GLineEdit_324["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_324["font"] = ft
        GLineEdit_324["fg"] = "#333333"
        GLineEdit_324["justify"] = "center"
        GLineEdit_324["text"] = ""
        GLineEdit_324.place(x=250,y=530,width=127,height=30)

        GLabel_553=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_553["font"] = ft
        GLabel_553["bg"] = "#15161a"
        GLabel_553["fg"] = "#f4eded"
        GLabel_553["justify"] = "center"
        GLabel_553["text"] = "Enter new car details"
        GLabel_553.place(x=140,y=90,width=210,height=30)

        root.mainloop()


    def GButton_882_command():
        #root.destroy()
        def delete():
            def GButton_792_command():
                gcarid=int(GLineEdit_465.get())
                conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
                cur=conn.cursor()
                cur.execute("select car_id from car_desc where car_id='%d'"%(gcarid))
                c=cur.fetchone()
                if c:
                    conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
                    cur=conn.cursor()
                    cur.execute("delete from car_desc where car_id='%d'"%(gcarid))
                    cur.commit()
                    #setting title
                    root=tk.Tk()
                    root.title("Deleted successfully")
                    Example(root).pack(fill="both", expand=True)
                    #setting window size
                    width=363
                    height=223
                    screenwidth = root.winfo_screenwidth()
                    screenheight = root.winfo_screenheight()
                    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                    root.geometry(alignstr)
                    root.resizable(width=False, height=False)

                    GLabel_857=tk.Label(root)
                    ft = tkFont.Font(family='Times',size=18)
                    GLabel_857["font"] = ft
                    GLabel_857["fg"] = "#333333"
                    GLabel_857["justify"] = "center"
                    GLabel_857["text"] = "Car deleted sucessfully!"
                    GLabel_857.place(x=50,y=80,width=255,height=47)
                    root.mainloop()
                else:
                    root=tk.Tk()
                    root.title("Unsuccessfull")
                    Example(root).pack(fill="both", expand=True)
                    #setting window size
                    width=363
                    height=223
                    screenwidth = root.winfo_screenwidth()
                    screenheight = root.winfo_screenheight()
                    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                    root.geometry(alignstr)
                    root.resizable(width=False, height=False)

                    GLabel_857=tk.Label(root)
                    ft = tkFont.Font(family='Times',size=18)
                    GLabel_857["font"] = ft
                    GLabel_857["fg"] = "#333333"
                    GLabel_857["justify"] = "center"
                    GLabel_857["text"] = "Car not found"
                    GLabel_857.place(x=50,y=80,width=255,height=47)
                    root.mainloop()

            root=tk.Tk()
            root.title("Delete")
            Example(root).pack(fill="both", expand=True)
            #setting window size
            width=402
            height=215
            screenwidth = root.winfo_screenwidth()
            screenheight = root.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root.geometry(alignstr)
            root.resizable(width=False, height=False)

            GLabel_769=tk.Label(root)
            ft = tkFont.Font(family='Times',size=10)
            GLabel_769["font"] = ft
            GLabel_769["fg"] = "#333333"
            GLabel_769["justify"] = "center"
            GLabel_769["text"] = "Enter Car ID"
            GLabel_769.place(x=60,y=90,width=120,height=30)

            GLineEdit_465=tk.Entry(root)
            GLineEdit_465["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            GLineEdit_465["font"] = ft
            GLineEdit_465["fg"] = "#333333"
            GLineEdit_465["justify"] = "center"
            GLineEdit_465["text"] = ""
            GLineEdit_465.place(x=200,y=90,width=115,height=30)

            GLabel_99=tk.Label(root)
            ft = tkFont.Font(family='Times',size=16)
            GLabel_99["font"] = ft
            GLabel_99["bg"] = "#15161a"
            GLabel_99["fg"] = "#f4eded"
            GLabel_99["justify"] = "center"
            GLabel_99["text"] = "CAR BOOKING"
            GLabel_99.place(x=110,y=30,width=158,height=31)

            GButton_792=tk.Button(root)
            GButton_792["bg"] = "#efefef"
            ft = tkFont.Font(family='Times',size=10)
            GButton_792["font"] = ft
            GButton_792["fg"] = "#000000"
            GButton_792["justify"] = "center"
            GButton_792["text"] = "Delete"
            GButton_792.place(x=140,y=150,width=84,height=30)
            GButton_792["command"] = GButton_792_command
            root.mainloop()

        root2=tk.Tk()
        root2.title("Display")
        Example(root2).pack(fill="both", expand=True)
        #setting window size
        width=800
        height=500
        screenwidth = root2.winfo_screenwidth()
        screenheight = root2.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root2.geometry(alignstr)
        root2.resizable(width=False, height=False)

        conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
        cur=conn.cursor()
        cur.execute('select * from car_desc')
        c=cur.fetchall()        
        cid=Label(root2,text='Car ID',width=13)
        cid.place(x=60,y=10)
        pno=Label(root2,text='Plate No',width=13)
        pno.place(x=160,y=10)
        pno=Label(root2,text='Model',width=13)
        pno.place(x=260,y=10)
        pno=Label(root2,text='Capacity',width=13)
        pno.place(x=360,y=10)
        pno=Label(root2,text='Milage',width=13)
        pno.place(x=460,y=10)
        pno=Label(root2,text='Name',width=13)
        pno.place(x=560,y=10)
        pno=Label(root2,text='Review',width=13)
        pno.place(x=660,y=10)

        k=1
        for i in c:
            for j in range(len(i)):
                e=Label(root2,text=i[j],width=13)
                e.place(x=j*100+60,y=30*k)
            k+=1
        b=Button(root2,text='Proceed to delete',command=delete)
        b.place(x=(j/2-2)*100+60,y=30*k)
        h=Button(root2,text='Go to homepage',command=root.lift)
        h.place(x=(j/2+2)*100,y=30*k)
        root.mainloop()


    #setting title
    root=tk.Tk()
    root.title("Admin homepage")
    #setting window size
    width=531
    height=332
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    bg = ImageTk.PhotoImage(Image.open("pic.png"))
    GLabel_326=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_326["font"] = ft
    GLabel_326["fg"] = "#333333"
    GLabel_326["justify"] = "center"
    GLabel_326["text"] = "label"
    GLabel_326["image"]=bg
    GLabel_326.place(x=0,y=0,width=531,height=332)

    GLabel_972=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_972["font"] = ft
    GLabel_972["bg"] = "#15161a"
    GLabel_972["fg"] = "#f4eded"
    GLabel_972["justify"] = "center"
    GLabel_972["text"] = "McQUEEN RENTALS"
    GLabel_972.place(x=80,y=40,width=400,height=44)

    GLabel_747=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_747["font"] = ft
    GLabel_747["bg"] = "#15161a"
    GLabel_747["fg"] = "#f4eded"
    GLabel_747["justify"] = "center"
    GLabel_747["text"] = "WELCOME!!"
    GLabel_747.place(x=120,y=110,width=250,height=32)

    GButton_740=tk.Button(root)
    GButton_740["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_740["font"] = ft
    GButton_740["fg"] = "#000000"
    GButton_740["justify"] = "center"
    GButton_740["text"] = "Add car"
    GButton_740.place(x=60,y=210,width=116,height=30)
    GButton_740["command"] = GButton_740_command

    GButton_882=tk.Button(root)
    GButton_882["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_882["font"] = ft
    GButton_882["fg"] = "#000000"
    GButton_882["justify"] = "center"
    GButton_882["text"] = "Remove car"
    GButton_882.place(x=300,y=210,width=115,height=30)
    GButton_882["command"] = GButton_882_command

    root.mainloop()



def admin_reg():
    def add_admin():
        uname=str(GLineEdit_320.get())
        pwd=str(GLineEdit_269.get())
        if len(pwd)<8:
            messagebox.showinfo("Error","Password should be atleast 8 characters")
        conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
        cur=conn.cursor()
        cur.execute("insert into admin values(admin_seq.nextval,'%s','%s')"%(uname,pwd))
        cur.commit()
        root2=tk.Tk()

        root2.title("Successful registration")
        Example(root2).pack(fill="both", expand=True)
        #setting window size
        width=300
        height=165
        screenwidth = root2.winfo_screenwidth()
        screenheight = root2.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root2.geometry(alignstr)
        root2.resizable(width=False, height=False)

        GLabel_536=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_536["font"] = ft
        GLabel_536["fg"] = "#333333"
        GLabel_536["justify"] = "center"
        GLabel_536["text"] = "Admin registered successfully!!"
        GLabel_536.place(x=30,y=60,width=241,height=36)

        conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
        cur=conn.cursor()
        cur.execute("select a_id from admin where username='%s' and password='%s'"%(uname,pwd))
        c=cur.fetchone()[0]

        GLabel_536=tk.Label(root2)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_536["font"] = ft
        GLabel_536["fg"] = "#333333"
        GLabel_536["justify"] = "center"
        GLabel_536["text"] = "Admin ID           "+str(c)
        GLabel_536.place(x=30,y=90,width=241,height=36)

        root2.mainloop()
        cur.commit()

    def GButton_615_command():
        root.destroy()
        homepage()

    root=tk.Tk()
    #setting title
    root.title("Admin registration")
    #<color> root.configure(bg='')
    #setting window size
    width=486
    height=376
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    bg = ImageTk.PhotoImage(Image.open("pic.png"))
    GLabel_326=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_326["font"] = ft
    GLabel_326["fg"] = "#333333"
    GLabel_326["justify"] = "center"
    GLabel_326["text"] = "label"
    GLabel_326["image"]=bg
    GLabel_326.place(x=0,y=0,width=486,height=376)

    GLabel_578=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_578["font"] = ft
    GLabel_578["bg"] = "#15161a"
    GLabel_578["fg"] = "#f4eded"
    GLabel_578["justify"] = "center"
    GLabel_578["text"] = "McQUEEN RENTALS"
    GLabel_578.place(x=50,y=30,width=400,height=47)

    GLabel_907=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_907["font"] = ft
    GLabel_907["fg"] = "#333333"
    GLabel_907["justify"] = "center"
    GLabel_907["text"] = "USERNAME"
    GLabel_907.place(x=90,y=150,width=131,height=30)

    GLabel_818=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_818["font"] = ft
    GLabel_818["fg"] = "#333333"
    GLabel_818["justify"] = "center"
    GLabel_818["text"] = "PASSWORD"
    GLabel_818.place(x=90,y=230,width=131,height=30)

    GButton_616=tk.Button(root)
    GButton_616["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_616["font"] = ft
    GButton_616["fg"] = "#000000"
    GButton_616["justify"] = "center"
    GButton_616["text"] = "Submit"
    GButton_616.place(x=120,y=300,width=115,height=30)
    GButton_616["command"] = add_admin

    GButton_615=tk.Button(root)
    GButton_615["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_615["font"] = ft
    GButton_615["fg"] = "#000000"
    GButton_615["justify"] = "center"
    GButton_615["text"] = "Go to homepage"
    GButton_615.place(x=260,y=300,width=115,height=30)
    GButton_615["command"] = GButton_615_command

    GLineEdit_269=tk.Entry(root)
    GLineEdit_269["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_269["font"] = ft
    GLineEdit_269["fg"] = "#333333"
    GLineEdit_269["justify"] = "center"
    GLineEdit_269["text"] = "Password"
    GLineEdit_269["show"]='*'
    GLineEdit_269.place(x=250,y=230,width=128,height=30)

    GLineEdit_320=tk.Entry(root)
    GLineEdit_320["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_320["font"] = ft
    GLineEdit_320["fg"] = "#333333"
    GLineEdit_320["justify"] = "center"
    GLineEdit_320["text"] = ""
    GLineEdit_320.place(x=250,y=150,width=127,height=30)

    GLabel_553=tk.Label(root)
    ft = tkFont.Font(family='Times',size=14)
    GLabel_553["font"] = ft
    GLabel_553["bg"] = "#15161a"
    GLabel_553["fg"] = "#f4eded"
    GLabel_553["justify"] = "center"
    GLabel_553["text"] = "Enter new admin details"
    GLabel_553.place(x=140,y=90,width=200,height=30)

    root.mainloop()



def admin_unsc():
    def del_admin():
        uname=str(GLineEdit_320.get())
        pwd=str(GLineEdit_269.get())
        if len(pwd)<8:
            messagebox.showinfo("Error","Password should be atleast 8 characters")
        conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
        cur=conn.cursor()
        cur.execute("select username,password from admin where username='%s' and password='%s'"%(uname,pwd))
        x=cur.fetchone()
        if x:
            cur.execute("delete from admin where username='%s' and password='%s'"%(uname,pwd))
            cur.commit()
            root2=tk.Tk()

            root2.title("Unsubscribe successful")
            Example(root2).pack(fill="both", expand=True)
            #setting window size
            width=300
            height=165
            screenwidth = root2.winfo_screenwidth()
            screenheight = root2.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root2.geometry(alignstr)
            root2.resizable(width=False, height=False)

            GLabel_536=tk.Label(root2)
            ft = tkFont.Font(family='Times',size=12)
            GLabel_536["font"] = ft
            GLabel_536["fg"] = "#333333"
            GLabel_536["justify"] = "center"
            GLabel_536["text"] = "Sorry to see you leave"
            GLabel_536.place(x=30,y=60,width=241,height=36)

            root2.mainloop()
        else:
            root2=tk.Tk()

            root2.title("Unsuccessful unsubscribe")
            Example(root2).pack(fill="both", expand=True)
            #setting window size
            width=300
            height=165
            screenwidth = root2.winfo_screenwidth()
            screenheight = root2.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root2.geometry(alignstr)
            root2.resizable(width=False, height=False)
        
            GLabel_536=tk.Label(root2)
            ft = tkFont.Font(family='Times',size=14)
            GLabel_536["font"] = ft
            GLabel_536["fg"] = "#333333"
            GLabel_536["justify"] = "center"
            GLabel_536["text"] = "Wrong credentials!!"
            GLabel_536.place(x=30,y=60,width=241,height=36)

            root2.mainloop()


    def GButton_615_command():
        root.destroy()
        homepage()

    root=tk.Tk()
    #setting title
    root.title("Admin unsubscribe")
    #<color> root.configure(bg='')
    #setting window size
    width=486
    height=370
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    bg = ImageTk.PhotoImage(Image.open("pic.png"))
    GLabel_326=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_326["font"] = ft
    GLabel_326["fg"] = "#333333"
    GLabel_326["justify"] = "center"
    GLabel_326["text"] = "label"
    GLabel_326["image"]=bg
    GLabel_326.place(x=0,y=0,width=486,height=370)

    GLabel_578=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_578["font"] = ft
    GLabel_578["bg"] = "#15161a"
    GLabel_578["fg"] = "#f4eded"
    GLabel_578["justify"] = "center"
    GLabel_578["text"] = "McQUEEN RENTALS"
    GLabel_578.place(x=50,y=30,width=400,height=47)

    GLabel_907=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_907["font"] = ft
    GLabel_907["fg"] = "#333333"
    GLabel_907["justify"] = "center"
    GLabel_907["text"] = "USERNAME"
    GLabel_907.place(x=90,y=150,width=131,height=30)

    GLabel_818=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_818["font"] = ft
    GLabel_818["fg"] = "#333333"
    GLabel_818["justify"] = "center"
    GLabel_818["text"] = "PASSWORD"
    GLabel_818.place(x=90,y=230,width=131,height=30)

    GButton_616=tk.Button(root)
    GButton_616["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_616["font"] = ft
    GButton_616["fg"] = "#000000"
    GButton_616["justify"] = "center"
    GButton_616["text"] = "Submit"
    GButton_616.place(x=120,y=300,width=115,height=30)
    GButton_616["command"] = del_admin

    GButton_615=tk.Button(root)
    GButton_615["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_615["font"] = ft
    GButton_615["fg"] = "#000000"
    GButton_615["justify"] = "center"
    GButton_615["text"] = "Go to homepage"
    GButton_615.place(x=260,y=300,width=115,height=30)
    GButton_615["command"] = GButton_615_command

    GLineEdit_320=tk.Entry(root)
    GLineEdit_320["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_320["font"] = ft
    GLineEdit_320["fg"] = "#333333"
    GLineEdit_320["justify"] = "center"
    GLineEdit_320["text"] = ""
    GLineEdit_320.place(x=250,y=150,width=127,height=30)
    
    GLineEdit_269=tk.Entry(root)
    GLineEdit_269["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_269["font"] = ft
    GLineEdit_269["fg"] = "#333333"
    GLineEdit_269["justify"] = "center"
    GLineEdit_269["text"] = ""
    GLineEdit_269["show"]='*'
    GLineEdit_269.place(x=250,y=230,width=128,height=30)

    GLabel_553=tk.Label(root)
    ft = tkFont.Font(family='Times',size=14)
    GLabel_553["font"] = ft
    GLabel_553["bg"] = "#15161a"
    GLabel_553["fg"] = "#f4eded"
    GLabel_553["justify"] = "center"
    GLabel_553["text"] = "Enter admin details"
    GLabel_553.place(x=140,y=90,width=210,height=30)

    root.mainloop()

def admin_log():
    def chk_admin():
        uname=str(GLineEdit_320.get())
        pwd=str(GLineEdit_269.get())
        if len(pwd)<8:
            messagebox.showinfo("Error","Password should be atleast 8 characters")
        conn=pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=LAPTOP-0DDTBLRJ;Service Name=orcl;User ID=system;Password=sup123')
        cur=conn.cursor()
        cur.execute("select username,password from admin where username='%s' and password='%s'"%(uname,pwd))
        x=cur.fetchone()
        if x:
            root.destroy()
            admin_homepage()
        else:
            root2=tk.Tk()

            root2.title("Unsuccessful login")
            Example(root2).pack(fill="both", expand=True)
            #setting window size
            width=300
            height=165
            screenwidth = root2.winfo_screenwidth()
            screenheight = root2.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root2.geometry(alignstr)
            root2.resizable(width=False, height=False)

            GLabel_536=tk.Label(root2)
            ft = tkFont.Font(family='Times',size=14)
            GLabel_536["font"] = ft
            GLabel_536["fg"] = "#333333"
            GLabel_536["justify"] = "center"
            GLabel_536["text"] = "Wrong credentials!!"
            GLabel_536.place(x=30,y=60,width=241,height=36)

            root2.mainloop()

    def GButton_617_command():
        root.destroy()
        homepage()

    root=tk.Tk()
    #setting title
    root.title("Admin login")
    #<color> root.configure(bg='')
    #setting window size
    width=486
    height=376
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    bg = ImageTk.PhotoImage(Image.open("pic.png"))
    GLabel_326=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_326["font"] = ft
    GLabel_326["fg"] = "#333333"
    GLabel_326["justify"] = "center"
    GLabel_326["text"] = "label"
    GLabel_326["image"]=bg
    GLabel_326.place(x=0,y=0,width=486,height=376)

    GLabel_578=tk.Label(root)
    ft = tkFont.Font(family='Times',size=28)
    GLabel_578["font"] = ft
    GLabel_578["bg"] = "#15161a"
    GLabel_578["fg"] = "#f4eded"
    GLabel_578["justify"] = "center"
    GLabel_578["text"] = "McQUEEN RENTALS"
    GLabel_578.place(x=50,y=30,width=400,height=47)

    GLabel_907=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_907["font"] = ft
    GLabel_907["fg"] = "#333333"
    GLabel_907["justify"] = "center"
    GLabel_907["text"] = "USERNAME"
    GLabel_907.place(x=90,y=150,width=131,height=30)

    GLabel_818=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_818["font"] = ft
    GLabel_818["fg"] = "#333333"
    GLabel_818["justify"] = "center"
    GLabel_818["text"] = "PASSWORD"
    GLabel_818.place(x=90,y=230,width=131,height=30)

    GButton_616=tk.Button(root)
    GButton_616["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_616["font"] = ft
    GButton_616["fg"] = "#000000"
    GButton_616["justify"] = "center"
    GButton_616["text"] = "Submit"
    GButton_616.place(x=120,y=300,width=115,height=30)
    GButton_616["command"] = chk_admin

    GButton_617=tk.Button(root)
    GButton_617["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_617["font"] = ft
    GButton_617["fg"] = "#000000"
    GButton_617["justify"] = "center"
    GButton_617["text"] = "Go to homepage"
    GButton_617.place(x=260,y=300,width=115,height=30)
    GButton_617["command"] = GButton_617_command


    GLineEdit_269=tk.Entry(root)
    GLineEdit_269["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_269["font"] = ft
    GLineEdit_269["fg"] = "#333333"
    GLineEdit_269["justify"] = "center"
    GLineEdit_269["text"] = "Password"
    GLineEdit_269["show"]='*'
    GLineEdit_269.place(x=250,y=230,width=128,height=30)

    GLineEdit_320=tk.Entry(root)
    GLineEdit_320["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_320["font"] = ft
    GLineEdit_320["fg"] = "#333333"
    GLineEdit_320["justify"] = "center"
    GLineEdit_320["text"] = ""
    GLineEdit_320.place(x=250,y=150,width=127,height=30)

    GLabel_553=tk.Label(root)
    ft = tkFont.Font(family='Times',size=14)
    GLabel_553["font"] = ft
    GLabel_553["bg"] = "#15161a"
    GLabel_553["fg"] = "#f4eded"
    GLabel_553["justify"] = "center"
    GLabel_553["text"] = "Enter admin details"
    GLabel_553.place(x=140,y=90,width=200,height=30)

    root.mainloop()
    
homepage()
