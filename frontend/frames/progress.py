from msilib.schema import RadioButton
from tkinter import BOTTOM, CENTER, StringVar, ttk
from tkinter import messagebox, Canvas
from tkinter.font import Font
import tkinter as tk
import datetime
import random

dataList = [{"id":"123","status":"Progressing","datetime":"2021-09-08 11:12:20"},{"id":"123","status":"Completed","datetime":"2021-09-08 11:12:20"},]
validationList = []

def sendValidationList():
    pass

class status(tk.Frame):
    def __init__(self, parent):
        super(status,self).__init__()
        self.parent=parent
    
        s1 = ttk.Style()
        s1.configure('bluetab.TFrame', background = "#4285f4")
        sectionframe = ttk.Frame(self,style='bluetab.TFrame')

        title = ttk.Label(sectionframe,text="Progress",font=("ibm plex sans", 30,'bold'),background="#4285f4",foreground="white")
        title.pack()
        sb = ttk.Scrollbar(sectionframe)
        sb.pack(side = 'right', fill = 'y')
        sectionframe.pack(side='top', fill='both', expand=True)

        emailButton={}

        def sel(c):
            if c not in validationList:
                validationList.append(c)
            else:
                validationList.remove(c)
            print(validationList)

        rb=[]
        #Each email item is a button
        for i in dataList:
            emailItemFrame = ttk.Frame(sectionframe,style='bluetab.TFrame',padding=2)

            displaycontent = i["datetime"]+"\t\t"+i["id"]+"\t\t"+i["status"]+"\t\t\t\t\t"

            s = ttk.Style()
            emailDisplay = ttk.Label(emailItemFrame, text=displaycontent, background="#ecf3ff",font=("ibm plex sans", 18))
            emailDisplay.grid(row = 0, column = 0, sticky = tk.NSEW)
            emailItemFrame.pack(side='top', fill='both')

            # emailButton[i["id"]] = ttk.Checkbutton(emailItemFrame, text=displaycontent, command=lambda c=i: sel(c["id"]))
            # emailButton[i["id"]].grid(row = 0, column = 0, sticky = tk.NSEW)


