import tkinter as tk
from tkinter.constants import BOTH, NW, TOP, X, Y
import tkinter.scrolledtext as st
import os 
import subprocess
window = tk.Tk()
window.title("File Directory Maker")

#test


def createdir():
    '''The directory creator is here'''
    fl_path = entry.get()
    fl_tree = textb.get("1.0", tk.END)
    
    log_sc_txt.configure(state='normal')
    log_sc_txt.insert("1.0", fl_tree)
    log_sc_txt.configure(state='disabled')
    
    print(str(fl_tree))
    print(str(fl_path))
    
    
    counter = 0
    for line in fl_tree :
        
        counter += 1
        if line[0] == "-":
            newline = line[1:-1]
        else:
            newline = line[:-1]

        path = os.path.join(fl_path, newline)

        if line[0] != "-" :
            
            if os.path.exists(path) == "True" :
                print("the path exists")
                continue
            
            elif os.path.exists(path) == "False" :
                
                os.makedirs(path)
                print(f'made file directory {path}')

        elif line[0] == "-" :
            try:
                print('smth')
            except OSError.args :
                print("error")

def cl_log():
    '''clears the currently logged label contents'''
    log_sc_txt.configure(state='normal')
    log_sc_txt.delete("1.0", tk.END)
    log_sc_txt.configure(state='disabled')
        
def update_app():
     os.system('update.cmd')
    


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
    fg="white"
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





log_sc_txt.configure(state='disabled')
log_sc_txt.pack(pady=3, padx=3, fill=BOTH)
clear_log.pack(side=tk.LEFT)
backup_log.pack(side=tk.LEFT)
entry.pack(pady=5, side=tk.TOP)
button.pack(side=tk.TOP, fill=X)
log_frame.pack(side=tk.TOP, fill=tk.BOTH)
log2_frame.pack(fill=tk.BOTH)
textb.pack()
entry.insert(0, "Directory name")


dir_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
dir_txt_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)





window.mainloop()








