from msilib.schema import RadioButton
from tkinter import BOTTOM, CENTER, StringVar, ttk
from tkinter import messagebox, Canvas
from tkinter.font import Font
import tkinter as tk
import datetime
import random

dataList = [{"id":"123","company":"ABC","product":"123dss","quantity":"ABC","datetime":"2021-09-08 11:12:20"},{"id":"234","company":"ABC","product":"dndd","quantity":"ABC","datetime":"2021-09-08 11:12:20"},]
validationList = []

def sendValidationList():
    pass

class dataValidation(tk.Frame):
    def __init__(self, parent):
        super(dataValidation,self).__init__()
        self.parent=parent
    
        s1 = ttk.Style()
        s1.configure('bluetab.TFrame', background = "#4285f4")
        sectionframe = ttk.Frame(self,style='bluetab.TFrame')

        title = ttk.Label(sectionframe,text="Data Validation",font=("ibm plex sans", 30,'bold'),background="#4285f4",foreground="white")
        title.pack()
        sb = ttk.Scrollbar(sectionframe)
        sb.pack(side = 'right', fill = 'y')
        sectionframe.pack(side='top', fill='both', expand=True)
        buttonframe = ttk.Frame(self,style='bluetab.TFrame')

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

            displaycontent = i["datetime"]+"\t"+i["company"]+"\t\t"+i["product"]+"\t\t"+i["quantity"]+'\t\t\t'
            emailDisplay = ttk.Label(emailItemFrame, text=displaycontent)
            emailDisplay.grid(row = 0, column = 0, sticky = tk.NSEW)
            emailItemFrame.pack(side='top', fill='both')

            s = ttk.Style()
            s.configure("email.TCheckbutton",background="#ecf3ff",font=("ibm plex sans", 18),padding=2)
            emailButton[i["id"]] = ttk.Checkbutton(emailItemFrame, text=displaycontent, command=lambda c=i: sel(c["id"]),style='email.TCheckbutton')
            emailButton[i["id"]].grid(row = 0, column = 0, sticky = tk.NSEW)
    

        validateButton = ttk.Button(buttonframe,text="Validate", command = sendValidationList)
        #extractButton.pack(side='bottom', fill='both', expand=False
        #buttonframe.grid_configure()
        validateButton.pack(side='right')
        #extractButton.grid(row=buttonframe.grid_size()[1],column=buttonframe.grid_size()[0])
        buttonframe.pack(side=BOTTOM,fill='x')

