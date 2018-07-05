# imports tkinter form gui
from tkinter import *
# import matplotlib for graphs,figures,canvas
import matplotlib

matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2TkAgg)
from matplotlib.figure import Figure
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
# import csv for csv manipulation
import csv
# numby for creating dictionarires
import numpy as np
from tkinter import messagebox
# define css
from tkinter import ttk as tkk


class main:
    ''' Plotgraps asks the user to upload a file.. Currently it takes the two columns of the csv file.
	it creates a dictionay of the columns values (provided you know the column names).
	It plots a bar graph using plot.bar function of matplotlib. '''

    def plotGraph():

        try:
            filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
            # read values of csv file and store them into dicitionaries.

            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                print(filename)
                print(reader)
                if filename.rsplit(".")[-1] != "csv" or  reader is None:
                    messagebox.showinfo("file error","File type not supported")

                else:
                    x = []
                    y = []
                    for row in reader:
                        x.append(row['Year'])
                        y.append(row['Incidents'])

                # defines the scale of the figure generated
                f = Figure(figsize=(5, 5), dpi=100)

                # typeconversion for incident values
                inci = list(map(int, y))

                # store the value of x axis and y axis
                objects = x
                y_pos = np.arange(len(objects))
                performance = inci

                # Plot the bar
                plt.bar(y_pos, performance, align='center', alpha=0.5)
                # Inser ticks,labels, and titles
                plt.xticks(y_pos, objects)
                plt.ylabel('Usage')
                plt.title('Usage/ year')

                # Show the plot
                plt.show()

                # defines where the canvas will store thing
                canvas = FigureCanvasTkAgg(f, root)
                canvas.show()

                # Tool bar for zoom, save and aditional analysis.
                toolbar = NavigationToolbar2TkAgg(canvas, root)
                toolbar.update()
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        except:
            FileNotFoundError: \
                print("Wrong file or file path")

    '''
	HomeWindow defines the title of the application and
	welcomes the user to the dashboard. User has the option to upload csv file
	for analysis.
	'''

    def HomeWindow():
        # withdraw.Tk()
        root = Tk()
        width = 600
        height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)

        # MenuBar
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Close")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)

        # Location of the MenuBar
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

        # Button
        b = Button(root, text="Visaulize data", width=30, pady=30, font=(12), command=lambda: main.plotGraph())
        b.place(x=180, y=160)

        root.mainloop()
