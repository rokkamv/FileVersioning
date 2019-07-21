from tkinter import *
from tkinter.scrolledtext import ScrolledText
import os
import subprocess
from time import localtime, strftime

window = Tk()
fol=sys.argv[1]
uname=sys.argv[2]
window.title("repo_"+fol)
# if(len(sys.argv)>3):
text=sys.argv[3]

textPad = ScrolledText(window)
textPad.pack(fill='both', expand=True)

# if(len(sys.argv)>3):
textPad.insert(INSERT,text)
filname=fol+'_'+uname+'_'+strftime("%d-%m-%Y_%Hh%Mm%Ss", localtime())
def btn_exit():
    exit()
def btn_save():
    edtxt=textPad.get(1.0,END)
    f=open("C:/Users/V/Desktop/ConMan/Repos/repo_"+fol+"/"+uname+"/"+filname+".txt","w+")
    f.write(edtxt)
    # if(edtxt!=text):
    #     edtxt=textPad.get(1.0,END)
    #     os.system("g++ C:\\Users\\V\\Desktop\\ConMan\\BackEnd\\openrepoc.cpp && a "+fol+" "+edtxt+" "+uname)
    exit()
def btn_commit():
    edtxt=textPad.get(1.0,END)
    f=open("C:/Users/V/Desktop/ConMan/Repos/repo_"+fol+"/"+fol+"/"+filname+".txt","w+")
    f.write(edtxt)
    fu=open("C:/Users/V/Desktop/ConMan/Repos/repo_"+fol+"/"+uname+"/"+filname+".txt","w+")
    fu.write(edtxt)
    # if(edtxt!=text):
    #     edtxt=textPad.get(1.0,END)
    #     print(edtxt)
    #     flag='c'
    #     subprocess.call(["g++", "C:\\Users\\V\\Desktop\\ConMan\\BackEnd\\openrepoc.cpp"]) # OR gcc for c program
    #     subprocess.call("a "+fol+" "+edtxt+" "+uname+" "+flag)
        # os.system("g++ C:\\Users\\V\\Desktop\\ConMan\\BackEnd\\openrepoc.cpp && a "+fol+" "+edtxt+" "+uname+" "+flag)
    exit()
menu = Menu(window)
window.config(menu=menu)
menu.add_command(label="Commit", command=btn_commit)
menu.add_command(label="Save", command=btn_save)
menu.add_command(label="Exit", command=btn_exit)
# text="123456789"

textPad.pack()

window.mainloop()
