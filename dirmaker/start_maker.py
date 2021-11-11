import tkinter as tk
from tkinter.constants import BOTH, NW, TOP, X, Y
import tkinter.scrolledtext as st
import os 
import subprocess
from datetime import datetime
window = tk.Tk()
window.title("File Directory Maker")

#v0.1.3

def createdir():
    '''The directory maker is here'''
    
    fl_path = entry.get()
    fl_tree = textb.get("1.0", tk.END)
    print(fl_tree)
    
    box = []
    tempvar = ''
    for letter in fl_tree :
        print(letter)
        if letter=="\n" :
            box.append(tempvar)
            tempvar = ''
            continue
        elif letter!="\n":
            tempvar = (tempvar + letter)

    for thing in box :
        path = os.path.join(fl_path, thing)
        if not os.path.exists(path) : 
            thetime = datetime.now()
            os.makedirs(path)
            log_sc_txt.configure(state='normal')
            log_sc_txt.insert("1.0", f'| Created Directory {path} at {thetime} |')
            log_sc_txt.configure(state='disabled')


def cl_log():
    '''clears the currently logged label contents'''
    log_sc_txt.configure(state='normal')
    log_sc_txt.delete("1.0", tk.END)
    log_sc_txt.configure(state='disabled')
        
def update_app():
     os.system('update.cmd')
    
def log_to_file():
    logfile = open("logfile.txt", "a")
    logtext = log_sc_txt.get("1.0", tk.END)
    timestamp = datetime.now()    
    L = ['_________\n', f'{logtext}\n', f'Logged at {timestamp}\n', '_______\n']
    logfile.writelines(L) 
    logfile.close()


dir_frame = tk.Frame(
    master=window,
    relief=tk.FLAT,
    borderwidth=1,
    width=50,
    height=25
)

dir_txt_frame = tk.Frame(
    master=window,
    relief=tk.SUNKEN,
    borderwidth=5,
    width=50,
    height=25
)

log_frame = tk.Frame(
    master=dir_frame,
    relief=tk.FLAT,
    borderwidth=1,
    width=50,
    height=2,
    bg="green"
)

log2_frame = tk.Frame(
    master=dir_frame,
    relief=tk.SUNKEN,
    borderwidth=2,
    width=25,
    height=21,
    bg="green"
)


button = tk.Button(
    master=dir_frame,
    text="Create Directory",
    width=50,
    height=2,
    bg="green",
    fg="yellow",
    command=createdir
)

clear_log = tk.Button(
    master=log_frame,
    text="Clear Log Box",
    width=25,
    height=2,
    bg="red",
    fg="white",
    command=cl_log
    
)
log_sc_txt = st.ScrolledText(
    master=log2_frame,
    width=42,
    height=20,
    bg="blue",
    fg="white",
    
        
)

backup_log = tk.Button(
    master=log_frame,
    text="Backup Log to File",
    width=25,
    height=2,
    bg="blue",
    fg="white",
    command=log_to_file
)

entry = tk.Entry(
    master=dir_frame,
    fg="black",
    bg="white",
    width=50
)
textb = tk.Text(
    master=dir_txt_frame,
    fg="black",
    width=50,
    height=25
)

#menu top bar
menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
editmenu = tk.Menu(menu)
helpmenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="hello i do nothing")
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Find Word")
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Update", command=update_app)

#packaging
log_sc_txt.configure(state='disabled')
log_sc_txt.pack(pady=3, padx=3, fill=BOTH)
clear_log.pack(side=tk.LEFT)
backup_log.pack(side=tk.LEFT)
entry.pack(pady=5, side=tk.TOP)
button.pack(side=tk.TOP, fill=X)
log_frame.pack(side=tk.TOP, fill=tk.BOTH)
log2_frame.pack(fill=tk.BOTH)
textb.pack()
entry.insert(0, "Parent Directory Name")

dir_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
dir_txt_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

window.mainloop()
