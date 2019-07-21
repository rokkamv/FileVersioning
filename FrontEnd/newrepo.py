from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
import os

window = ThemedTk(theme="radiance")
uname=sys.argv[1]
window.title("New Repository")

#window.geometry('500x200')

lbl=Label(window,text="Enter the new file name:")
lbl.grid()
txtfname = Entry(window,width=30)
txtfname.grid(column=10)
# fol=txtfname.get()

# lbl=Label(window,text="Enter the path of folder:",font=("Times New Roman",20))
# lbl.grid(column=0,row=50)
# txtfpath = Entry(window,width=30)
# txtfpath.grid(column=1, row=50)

def btn_submit():
    os.system("g++ -Wall -Wextra C:\\Users\\V\\Desktop\\ConMan\\BackEnd\\newrepoc.cpp && a "+txtfname.get()+" "+uname)
    # os.system("g++ -Wall -Wextra newrepo.cpp")
    # os.system("a "+txtfname.get())
    exit()
def btn_exit():
    exit()
btn=Button(window,text="Submit",command=btn_submit)
btn.grid(column=25,row=150)
btn=Button(window,text="Cancel",command=btn_exit)
btn.grid(column=50,row=150)

window.mainloop()
