import tkinter as tk
from tkinter import *
import matplotlib
import subprocess
matplotlib.use("TkAgg")
from tkinter import ttk
import MySQLdb
import matplotlib.pyplot as plt
from matplotlib import  style
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",  # your username
                     passwd="secret",  # your password
                     db="abhivasu")  # name of the data base

cur = db.cursor()

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

class plotdata(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"Sensor Networking")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label = "Quit",command = quit)
        filemenu.add_separator()
        menubar.add_cascade(label = "File",menu = filemenu)
        tk.Tk.config(self,menu = menubar)

        self.frames = {}
        #00A3E0 title

        for F in(StartPage,plothourdata) :
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def livefunc():
    subprocess.call("live plot.py", shell=True)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sensor Networking", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Live Graph",
                            command = livefunc)
        button1.pack(pady=8)
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        canvas = FigureCanvasTkAgg(f, self)
        def plot_hour():

            f.clear()
            a = f.add_subplot(111)
            n = w1.get()
            m = w2.get()
            n = int(n)
            m = int(m)
            x = []
            y = []
            for i in range(n, m + 1):
                cur.execute("select value from averagedata where hour = %s", (i,))
                row = cur.fetchone()
                lastrec = row[0]
                x.append(i)
                y.append(lastrec)
            a.plot(x,y)
            canvas.show()
            toolbar = NavigationToolbar2TkAgg(canvas,self)
            toolbar.update()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        w1 = Scale(self, from_=0, to=12, tickinterval=1,orient = HORIZONTAL,activebackground ="#00A3E0",label = "From",
        length = 300, width = 20        )
        w1.set(0)
        w1.pack()
        w2 = Scale(self, from_=0, to=12, tickinterval=1, orient=HORIZONTAL,activebackground ="#00A3E0",label = "To",
                   length =300,width =20)
        w2.set(0)
        w2.pack()
        ttk.Button(self, text='Show', command=plot_hour).pack(pady=15)

class plothourdata(tk.Frame) :

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Second Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


app = plotdata()
app.mainloop()