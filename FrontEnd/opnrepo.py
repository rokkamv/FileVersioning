from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from ttkthemes import ThemedTk
from pathlib import Path
import os

window = ThemedTk(theme="radiance")
window.title("Open Repository")
#window.geometry('500x200')
uname=sys.argv[1]
lbl=Label(window,text="Select the path:")
lbl.grid(column=0,row=30)


def btn_brow():
    #Select filename
    fname=filedialog.askopenfilename(initialdir="C:/Users/V/Desktop/ConMan/Repos",title="Select File")
    lbl=Label(window,text=fname)
    lbl.grid(column=5,row=30)
    end=fname.rfind('/',0,fname.rfind('/'))
    start=fname.rfind('/',0,end)
    fol=fname[start+1:end][5:]
    # print(fol)
    # print(fname)
    #Load the file in txteditor
    thand=open(fname).read()
    p=Path('C:/Users/V/Desktop/ConMan/Repos/repo_'+fol+'/'+uname)
    if not os.path.exists('C:/Users/V/Desktop/ConMan/Repos/repo_'+fol+'/'+uname):
        os.mkdir("C:/Users/V/Desktop/ConMan/Repos/repo_"+fol+"/"+uname)
    def btn_open():
        os.system("txteditor.py "+fol+" "+uname+" "+thand)
    btn=Button(window,text="Open",command=btn_open)
    btn.grid(column=25,row=150)
        #Get the content of txteditor

btn=Button(window,text="Browse...",command=btn_brow)
btn.grid(column=25,row=30)
# txtpath = Entry(window,width=30)
# txtpath.grid(column=1, row=30)

    # os.system("cd ..;cd Backend;"+"g++ -Wall -Wextra openrepoc.cpp;"+"a "+)
def btn_exit():
    exit()
# btn=Button(window,text="Open",command=btn_open)
# btn.grid(column=25,row=150)
btn=Button(window,text="Cancel",command=btn_exit)
btn.grid(column=50,row=150)



window.mainloop()
