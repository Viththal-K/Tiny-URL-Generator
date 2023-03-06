from tkinter import *
import pyshorteners

root = Tk()

root.title("URL Shortner")
root.geometry("300x150")
root.resizable(0,0)

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_ent.get())
    short_ent.insert(0, short_url)

long_lbl = Label(root, text="Enter Long URL")
long_lbl.place(x=100,y=10)

long_ent = Entry(root, width=40)
long_ent.place(x=30,y=30)

btn = Button(root, text="Generate Tiny URL", command=shorten, width=20)
btn.place(x=70,y=60)

short_lbl = Label(root, text="Shortened URL")
short_lbl.place(x=100,y=90)

short_ent = Entry(root, width=40)
short_ent.place(x=30,y=110)

root.mainloop()