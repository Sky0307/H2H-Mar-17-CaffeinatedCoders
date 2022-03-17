from msilib.schema import RadioButton
from tkinter import BOTTOM, CENTER, StringVar, ttk
from tkinter import messagebox, Canvas
from tkinter.font import Font
import tkinter as tk
import datetime
import random
from turtle import bgcolor

emailItemList = [{"id":"1","title":"Request of hahah","sender":"ABC","datetime":"2021-09-08 11:12:20"},{"id":"2","title":"Request of ABC","sender":"ABC","datetime":"2021-09-08 11:12:20"},]
extractList = []

def sendExtractionList():
    pass

class mailBox(tk.Frame):
    def __init__(self, parent):
        super(mailBox,self).__init__()
        self.parent=parent
    
        s1 = ttk.Style()
        s1.configure('bluetab.TFrame', background = "#4285f4")
        sectionframe = ttk.Frame(self,style='bluetab.TFrame')

        title = ttk.Label(sectionframe,text="Mail Box",font=("ibm plex sans", 30,'bold'),background="#4285f4",foreground="white")
        title.pack()
        sb = ttk.Scrollbar(sectionframe)
        sb.pack(side = 'right', fill = 'y')
        sectionframe.pack(side='top', fill='both', expand=True)
        buttonframe = ttk.Frame(self,style='bluetab.TFrame')

        emailButton={}

        def sel(c):
            if c not in extractList:
                extractList.append(c)
            else:
                extractList.remove(c)
            print(extractList)

        rb=[]
        #Each email item is a button
        for i in emailItemList:
            emailItemFrame = ttk.Frame(sectionframe,padding=2,style='bluetab.TFrame')

            # displaycontent = i["datetime"]+"\t\t\t"+i["title"]+"\t\t\t"+i["sender"]
            # emailDisplay = ttk.Label(emailItemFrame, text=displaycontent)
            # emailDisplay.grid(row = 0, column = 0, sticky = tk.NSEW)
            emailItemFrame.pack(side='top', fill='x')
            #emailItemFrame.grid(row = 0, column = 0, sticky = tk.NSEW)
            var = StringVar()
            s = ttk.Style()
            s.configure("email.TCheckbutton",background="#ecf3ff",font=("ibm plex sans", 18),padding=2)
            emailButton[i["id"]] = ttk.Checkbutton(emailItemFrame, text=i["datetime"]+"\t"+i["title"]+"\t\t"+i["sender"]+"\t\t\t", command=lambda c=i: sel(c["id"]),style='email.TCheckbutton')
            emailButton[i["id"]].grid(row = 0, column = 0, sticky = tk.NSEW)

        extractButton = ttk.Button(buttonframe,text="Extract", command = sendExtractionList)
        extractButton.pack(side='right')
        #buttonframe.grid_configure()
        #extractButton.grid(column=2,row=0)
        #extractButton.grid(row=buttonframe.grid_size()[1],column=buttonframe.grid_size()[0])
        buttonframe.pack(side=BOTTOM,fill='x')

