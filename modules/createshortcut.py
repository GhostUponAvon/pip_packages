import os, winshell
from win32com.client import Dispatch


desktop = winshell.desktop() #base directory for desktop


path = os.path.join(desktop, "Run Directory Maker.lnk")  # the shortcuts path

path2 = os.getcwd() #get the current directory

path_w_ext = os.path.join(path2, "runapp.cmd")


target = path_w_ext


wDir = path2                 


icon = path_w_ext    #.cmd


shell = Dispatch('WScript.Shell') #dunno what this does


shortcut = shell.CreateShortCut(path) #created shortcut 


shortcut.Targetpath = target


shortcut.WorkingDirectory = wDir


shortcut.IconLocation = icon  


shortcut.save() #saves the shortcut
