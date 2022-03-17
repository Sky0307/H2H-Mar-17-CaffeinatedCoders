from msilib.schema import RadioButton
from tkinter import BOTTOM, CENTER, StringVar, ttk
from tkinter import messagebox, Canvas
from tkinter.font import Font
import tkinter as tk
import datetime
import random
from data_extraction import DataExtraction
from data_validation import DataValidation

dataList = [{"id":123,"company":"ABC","product":"test-test-test-test-test-123dss","quantity":123,"datetime":"2021-09-08 11:12:20"},{"id":234,"company":"ABC","product":"test-test-dndd-test-test-test","quantity":465,"datetime":"2021-09-08 11:12:20"},]
validationList = []

def sendValidationList():
    dv = DataValidation()
    dv.write_to_database(validationList)

def getExList():
    de = DataExtraction()
    dataList.extend(de.extract_data_from_excel())

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
        #sb.config(command=sectionframe.xview)
        sectionframe.pack(side='top', fill='both', expand=True)
        buttonframe = ttk.Frame(self,style='bluetab.TFrame')

        header = ttk.Label(sectionframe,text="{:5s}\t{:30s}\t{:40s}\t{:5s}".format("ID","Company","Product","Quantity"),font=("ibm plex sans", 18,'bold'),background="#4285f4",foreground="white")
        header.pack()
        getExList()

        def getList(scf):
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
                print(i)
                emailItemFrame = ttk.Frame(scf,style='bluetab.TFrame',padding=2)

                displaycontent = "{:5s}\t{:20s}\t{:40s}\t{:5s}\t\t\t\t\t".format(str(i["id"]),i["company"],i["product"],str(i["quantity"]))
                emailDisplay = ttk.Label(emailItemFrame, text=displaycontent)
                emailDisplay.grid(row = 0, column = 0, sticky = tk.NSEW)
                emailItemFrame.pack(side='top', fill='both')

                s = ttk.Style()
                s.configure("email.TCheckbutton",background="#ecf3ff",font=("ibm plex sans", 16),padding=2)
                emailButton[i["id"]] = ttk.Checkbutton(emailItemFrame, text=displaycontent, command=lambda c=i: sel(c),style='email.TCheckbutton')
                emailButton[i["id"]].grid(row = 0, column = 0, sticky = tk.NSEW)

        getList(sectionframe)

        validateButton = ttk.Button(buttonframe,text="Validate", command = sendValidationList)
        #extractButton.pack(side='bottom', fill='both', expand=False
        #buttonframe.grid_configure()
        validateButton.pack(side='right')
        #extractButton.grid(row=buttonframe.grid_size()[1],column=buttonframe.grid_size()[0])
        buttonframe.pack(side=BOTTOM,fill='x')
    
    
    