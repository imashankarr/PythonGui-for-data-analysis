# PythonGui-for-data-analysis
This is a sample GUI application that uses Tkinter. It connects the database using SQLite.
The current login and password for the application is admin. If the user enters the username/password
correctly, it redirects it to a dashboard. There user can select csv file and plot graphs. currently the application
works only for data.csv which is also uploaded. You need to install python,Tkinter,sqlite,numpy,matplotlib libraries
for the code to work properly.

#Files:
gui.py:       Is the main login page of the application. It prompts with username, password and submit button
database.py : Creates a database file and stores admin as username and password.If the user enters the correct uername
              and pasword, it redirects the application to dashboard which is stored in method.py
method.py :   It consist of two methods, plotGraph and HomeWindow. HomeWindow is the dashboard for the application and
              plotGraph plots the graph from a user selected csv.

Future updates will come soon.
