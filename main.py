import tkinter as tk
from tkinter import ttk
import os
from frontend.frames.mainpage import mainPage

dir_path = os.path.dirname(os.path.realpath(__file__)) # Get the current file location
os.chdir(dir_path)  # Change current working directory


# Define a main class
class Main (tk.Tk):

    def __init__(self, *args):
        tk.Tk.__init__(self, *args)

        # Make a Image object and use its geometry to set the height and width of main window
        #startImage = tk.PhotoImage(file=r"todo")
        #self.geometry("%dx%d+0+0" % (startImage.width(), startImage.height()))
        self.geometry("960x720+0+0")
        self.resizable(False, False)
        self.grid()

        self.tk.call("source", "./frontend/Azure-ttk-theme-main/azure.tcl")

        # Then set the theme you want with the set_theme procedure
        self.tk.call("set_theme", "light")

        # Open the mainPage frame (from frames.py) as default when Main is called
        a=mainPage(self)
        a.pack(fill='both')



# Call Main window and loop it
n = Main()

def update():
        n.after(1000, update) # run itself again after 1000 ms

    # run first time
update()

n.mainloop()

