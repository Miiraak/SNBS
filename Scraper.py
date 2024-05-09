import os
import requests
from tkinter.filedialog import askdirectory
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup


def choice_folder():
    Path = askdirectory(title='Select Folder')  # shows dialog box and return the path
    EntryPath.insert(END, f"{Path}")


def next_page():
    frmF.grid_forget()
    frmS.pack()


def scrap():
    fullPath = os.path.join(EntryPath.get(), EntryFileName.get() + ".txt")
    url = EntryURL.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.find(EntryType.get(), id=EntryID.get())
    f = open(fullPath, "a")
    f.write(text.get_text())
    f.close()


# _______________________________________________________________________
# Création fenêtre
root = Tk()
root.title("SNBS")
root.geometry("300x115")
root.resizable(height=False, width=False)

# ________________________________________________________________________
# Frame file
frmF = ttk.Frame(root, padding=9)
frmF.grid()

# Label et entry file name
ttk.Label(frmF, text="File Name :").grid(column=0, row=0)
EntryFileName = Entry(frmF, width=34)
EntryFileName.grid(column=1, row=0, pady=10)

# Label et entry folder path
ttk.Label(frmF, text="Save folder :").grid(column=0, row=1)
EntryPath = Entry(frmF, width=34)
EntryPath.grid(column=1, row=1, pady=5)


# Boutton choix dossier
ButtonChoix = Button(frmF, text="Select", command=choice_folder)
ButtonChoix.grid(column=0, row=2, pady=5)

# Boutton Next
ButtonChoix = Button(frmF, text="Next", command=next_page)
ButtonChoix.grid(column=1, row=2)

# _________________________________________________________________________


# Frame scrap
frmS = ttk.Frame(root, padding=10)
frmS.grid()

# Zone URL
ttk.Label(frmS, text="URL :").grid(column=0, row=0)
EntryURL = Entry(frmS, width=34)
EntryURL.grid(column=1, row=0, pady=5)

# Zone Type
ttk.Label(frmS, text="Type HTML :").grid(column=0, row=2)
EntryType = Entry(frmS, width=34)
EntryType.grid(column=1, row=2, pady=5)

# Zone ID
ttk.Label(frmS, text="ID :").grid(column=0, row=3)
EntryID = Entry(frmS, width=34)
EntryID.grid(column=1, row=3)

# Button scrap
ButtonScrap = Button(frmS, text="Scrap", command=scrap)
ButtonScrap.grid(column=1, row=4)

# _________________________________________________________

frmS.grid_forget()
root.mainloop()
