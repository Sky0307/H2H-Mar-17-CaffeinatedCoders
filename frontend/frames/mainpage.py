from tkinter import BOTH, Tk,ttk
import tkinter as tk
from frames.mailbox import mailBox
from frames.datavalidation import dataValidation
from frames.progress import status

class mainPage(tk.Frame):
    def __init__(self, parent) -> None:
        super(mainPage,self).__init__()

        style = ttk.Style(parent)
        style.configure('lefttab.TNotebook', tabposition='ws', tabmargins=[2, 5, 2, 0])
        # Mysky = "#4285f4"
        # Myyellow = "#356cc7"

        # style = ttk.Style(parent)

        # style.theme_create( "dummy", parent="alt", settings={
        #         "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0], "tabposition":'ws' } },
        #         "TNotebook.Tab": {
        #             "configure": {"padding": [100, 100], "background": Myyellow },
        #             "map":       {"background": [("selected", Mysky)],
        #                         "expand": [("selected", [1, 1, 1, 0])] } } } )

        # style.theme_use("dummy")

        nb = ttk.Notebook(parent)
        nb.add(mailBox(parent), text="Mailbox")
        nb.add(dataValidation(parent), text="Validation")
        nb.add(status(parent), text="Progress")

        nb.pack(expand=1, fill=BOTH)

    