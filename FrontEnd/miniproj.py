from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
import os

window = ThemedTk(theme="radiance")
# window.style=Style()
# window.style.theme_use('plastik')
window.title("File Versioning System")

lbl=Label(window,text="VC LOGIN")
lbl.grid(column=0,row=0)
#window.geometry('500x200')

lbl=Label(window,text="Username")
lbl.grid(column=0,row=30)
txtlog = Entry(window,width=30)
txtlog.grid(column=1, row=30)

# lbl=Label(window,text="Password")
# lbl.grid(column=0,row=50)
# txtpass = Entry(window,width=30)
# txtpass.grid(column=1, row=50)

def btn_login():
    window.withdraw()
    os.system("userwin.py "+txtlog.get())
    exit()
def btn_exit():
    exit()

btn=Button(window,text="Login",command=btn_login)
btn.grid(column=25,row=150)
btn=Button(window,text="Cancel",command=btn_exit)
btn.grid(column=50,row=150)

window.mainloop()
