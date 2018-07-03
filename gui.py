'''
Author: Aditya Mayank Shankar, Date: June 30th 2018
A sample demonstration of GUI in Python using Tkinter.
User can plot graphs from the database and from the csv,
and email the plots as an attachments.

Python version: 3.6
Tkinter version: 8.6
Sqlite3 version: 3.14.6
Matlabplot Version:2.2.2
Code Version: 1.0
'''

# Import for Gui Tk
from tkinter import *
#Import for css for Tk
from tkinter import ttk as tkk
#import for database class function
from database import conn 
#import for using method class function
from method import main
#import fro sqlite functions
import sqlite3
#import message box for error messages
from tkinter import messagebox


#define root for window management
root = Tk()

#root.iconbitmap('icon.icon')
root.title("Login Application")


#set height and width according to the screen.
width = 600
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

#calculates the centre of the screen to display the contents
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


'''
Method checks the database connection from sqlite database.
If the value entered by the user matches with the database,
Homewindow method is called. Else it throws an error message.
'''
def Login(event=None):
    conn.databaseConnection()

    #fetch value enetred by the user
    uname = USERNAME.get()
    passwd = PASSWORD.get()

    #check for the blank
    if USERNAME.get() == "" or PASSWORD.get() == "":
        
        messagebox.showinfo("Error", "Password cannot be empty")
    else:
        test= conn.checkUserPassword(uname,passwd) 

        if test:
            root.withdraw()
            main.HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else :
            messagebox.showinfo("Error", "Username or Password does not match")
            USERNAME.set("")
            PASSWORD.set("")


#Variables to fetch the username, password value by the user
USERNAME = StringVar()
PASSWORD = StringVar()

# Frame
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=280)
Form.pack(side=TOP, pady=25)

#Lables
lbl_title = Label(Top, text = "Bozzuto Analytics Application", font=('arial', 14))
lbl_title.pack(fill=X)
lbl_username = tkk.Label(Form, text = "Username:",font=('arial', 14))
lbl_username.grid(row=1)
lbl_password = tkk.Label(Form, text = "Password:", font=('arial', 14))
lbl_password.grid(row=2)
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

#Widgets
username = tkk.Entry(Form, textvariable=USERNAME, font=(12))
username.grid(row=1, column=1)
password = tkk.Entry(Form, textvariable=PASSWORD, show="*", font=(12))
password.grid(pady=50,row=2, column=1)

#buttons
btn_login = tkk.Button(Form, text="Login", width=15, command=Login)
#btn_register = tkk.Button(Form, text="Register", width=15, command = lambda:x())

#btn_register.grid(pady=25,sticky = "E")
btn_login.grid(row=3,column=1,sticky="W",padx =15 )

btn_login.bind('<Return>', Login)

#Initialize
if __name__ == '__main__':
    root.mainloop()