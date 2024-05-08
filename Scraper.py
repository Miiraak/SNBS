import requests
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup

f = open("scraper_output.txt", "a", encoding="utf-8")


def scrap():
    url = EntryURL.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.find(EntryType.get(), id=EntryID.get())
    f.write(text.get_text())


# Création fenêtre
root = Tk()
root.title("SNBS")
root.geometry("300x130")
root.resizable(height=False, width=False)
frm = ttk.Frame(root, padding=10)
frm.grid()

# Zone URL
ttk.Label(frm, text="URL :").grid(column=0, row=0)
EntryURL = Entry(frm, width=34)
EntryURL.grid(column=1, row=0, pady=5)

# Zone Type
ttk.Label(frm, text="Type HTML :").grid(column=0, row=2)
EntryType = Entry(frm, width=34)
EntryType.grid(column=1, row=2, pady=5)

# Zone ID
ttk.Label(frm, text="ID :").grid(column=0, row=3)
EntryID = Entry(frm, width=34)
EntryID.grid(column=1, row=3)

# Button scrap
ButtonScrap = Button(root, text="Scrap", command=scrap)
ButtonScrap.grid(column=0, row=1)

root.mainloop()
f.close()
