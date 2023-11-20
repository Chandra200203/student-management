from tkinter import ttk
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import sqlite3

root = Tk()
root.title("Python: Online Attendance System")

width = 1000
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d"%(width,height,x,y))
root.resizable(0,0)

USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()

STUDENTNAME = StringVar()
REGNO = StringVar()
Var = IntVar()

def Database():
    global conn,cursor
    conn = sqlite3.connect("db_member3.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'member' (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,username TEXT,password TEXT,firstname TEXT,lastname TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS 'students' (stud_no INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Studentname TEXT, regno TEXT,var Text)")

    
def Exit():
    result = tkMessageBox.askquestion('System','Are you sure you want to exit?',icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

        
def LoginForm():
    global LoginFrame,lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP,pady = 80)
    title = Label(LoginFrame,text="LOGIN FORM",fg="red",font=('arial',25),bd=18)
    title.grid(row=0)
    lbl_username = Label(LoginFrame,text="Username:",font=('arial',25),bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame,text="Password:",font=('arial',25),bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame,text="",font=('arial',18))
    lbl_result1.grid(row=3,columnspan=2)
    username = Entry(LoginFrame,font=('arial,20'),textvariable=USERNAME,width = 15)
    username.grid(row=1,column=1)
    password = Entry(LoginFrame,font=('arial,20'),textvariable=PASSWORD,width = 15,show="*")
    password.grid(row=2,column=1)
    btn_login = Button(LoginFrame,text = "Login",font=('arial',18),width = 35,command = Login)
    btn_login.grid(row = 5,columnspan=2,pady=20)
    lbl_register = Label(LoginFrame,text="CREATE ACCOUNT",fg="Blue",font=('arial',18))
    lbl_register.grid(row = 4,sticky = W)
    lbl_register.bind('<Button-1>',ToggleToRegister)
def RegisterForm():
    global RegisterFrame,lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP,pady = 40)
    title1 = Label(RegisterFrame,text="REGISTRATION FORM",fg="red",font=('arial',25),bd=18)
    title1.grid(row=0)
    lbl_username = Label(RegisterFrame,text="Username:",font=('arial',18),bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame,text="Password:",font=('arial',18),bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame,text="Firstname:",font=('arial',18),bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame,text="Lastname:",font=('arial',18),bd=18)
    lbl_lastname.grid(row=4)
    lbl_result2 = Label(RegisterFrame,text="",font=('arial',18))
    lbl_result2.grid(row=5,columnspan=2)
    username = Entry(RegisterFrame,font=('arial,20'),textvariable=USERNAME,width = 15)
    username.grid(row=1,column=1)
    password = Entry(RegisterFrame,font=('arial,20'),textvariable=PASSWORD,width = 15,show="*")
    password.grid(row=2,column=1)
    firstname = Entry(RegisterFrame,font=('arial,20'),textvariable = FIRSTNAME,width=15)
    firstname.grid(row=3,column=1)
    lastname = Entry(RegisterFrame,font=('arial,20'),textvariable = LASTNAME,width=15)
    lastname.grid(row=4,column=1)
    btn_login = Button(RegisterFrame,text = "Register",font=('arial',18),width = 35,command = Register)
    btn_login.grid(row = 6,columnspan=2,pady=20)
    lbl_register = Label(RegisterFrame,text="GO TO LOGIN FORM",fg="Blue",font=('arial',15))
    lbl_register.grid(row = 7,sticky = W)
    lbl_register.bind('<Button-1>',ToggleToLogin)
def attendanceForm():
    global attendanceForm,lbl_result3
    attendanceFrame = Frame(root)
    attendanceFrame.pack(side=TOP,pady=20)
    title2 = Label(attendanceFrame,text="Online Attendance",fg = "red",font=('arial',25),bd=18)
    title2.grid(row=0)
    lbl_studentname = Label(attendanceFrame,text="Studentname:",font=('arial',25),bd=18)
    lbl_studentname.grid(row=1)
    lbl_regno = Label(attendanceFrame,text="RegNo:",font=('arial',25),bd=18)
    lbl_regno.grid(row=2)
    label_3 = Label(attendanceFrame,text="Status",width=20,font=('arial',20))
    label_3.grid(row=4,column=0)
    lbl_result3 = Label(attendanceFrame,text="",font=('arial',18))
    lbl_result3.grid(row=5,columnspan=2)
    studentname = Entry(attendanceFrame,font('arial',20),textVariable=STUDENTNAME,width=15)
    studentname.grid(row=2,column=1)
    regno = Entry(attendanceFrame,font('arial',20),textvariable=REGNO,width=15)
    regno.grid(row=2,column=1)
    present = Radiobutton(attendanceFrame,text="Present",padx=5,variable=Var,value=1)
    present.grid(row=4,column=1)
    absent = Radiobutton(attendanceFrame,text="absent",padx=20,variable=Var,value = 0)
    absent.grid(row=4,column=2)
    btn_submit = Button(attendanceFrame,text="SUBMIT",font=('arial',18),width=35,command=Submit)
    btn_submit.grid(row=6,columnspan=2,pady=20)
   
    
def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()
def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()
def ToggleToSubmit(event=None):
    LoginFrame.destroy()
    attendanceForm()
def Register():
    Database()
    if USERNAME.get == "" or PASSWORD.get() =="" or FIRSTNAME.get() == "" or LASTNAME.get() == "":
        lbl_result2.config(text="Please complete the required field!",fg="orange")
    else:
        cursor.execute("SELECT * FROM 'member' WHERE 'username' = ?",(USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken",fg="red")
        else:
            cursor.execute("INSERT INTO 'member' (username,password,firstname,lastname) VALUES(?,?,?,?)",(str(USERNAME.get()),str(PASSWORD.get()),str(FIRSTNAME.get()),str(LASTNAME.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            lbl_result2.config(text="successfully Created!",fg="black")
        cursor.close()
        conn.close()
def Login():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required filed!",fg="orange")
    else:
        cursor.execute("SELECT * FROM 'member' WHERE 'username' = ? and 'password' =?",(USERNAME.get(),PASSWORD.get()))
        if cursor.fetchone() is not None:
            ToggleToSubmit()
        else:
            lbl_result1.config(text="Invalid Username or password",fg="red")
def Submit():
    Database()
    if STUDENTNAME.get=="" or REGNO.get() == "" or var.get()=="":
        lbl_result3.config(text="Please complete the required field",fg="orange")
    else:
        cursor.execute("SELECT * FROM 'students' WHERE 'studentname' = ?",(STUDENTNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result3.config(text="Studentname is already taken",fg="red")
        else:
            cursor.execute("INSERT INTO 'students' (studentname,regno,var) VALUES(?,?,?)",(str(STUDENTNAME.get()),str(REGNO.get()),str(Var.get())))
            conn.commit()
            STUDENTNAME.set("")
            REGNO.set("")
            Var.set("")
            def View():
                conn = sqlite3.connect("db_member3.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM students")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                    tree.insert("",tk.END,values=row)
                conn.close()
            tree = ttk.Treeview(root,column=("column1","column2","column3","column4"),show='headings')
            tree.heading("#1",text="stud_no")
            tree.heading("#2",text="Studentname")
            tree.heading("#3",text="regno")
            tree.heading("#4",text="status")
            tree.pack()
            b2 = tk.Button(text="view data",command=View)
            b2.pack()
        cursor.close()
        conn.close()
LoginForm()
menubar = Menu(root)
filemenu =  Menu(menubar,tearoff=0)
filemenu.add_command(label="Exit",command=Exit)
menubar.add_cascade(label="File",menu=filemenu)
root.config(menu=menubar)

if _name_ == '_main_':
    root.mainloop()