from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
import os

window = ThemedTk(theme="radiance")
uname=sys.argv[1]
window.title("User Window")

lbl=Label(window,text="Hello, "+uname+"!")
lbl.grid(column=0,row=0)
#window.geometry('500x200')

def btn_newrepo():
    os.system("newrepo.py "+uname)
def btn_opnrepo():
    os.system("opnrepo.py "+uname)
def btn_exit():
    exit()
btn=Button(window,text="Create New Repository",command=btn_newrepo)
btn.grid(column=10,row=50)
btn=Button(window,text="Open an Existing Repository",command=btn_opnrepo)
btn.grid(column=10,row=100)
btn=Button(window,text="Exit",command=btn_exit)
btn.grid(column=10,row=150)

window.mainloop()
