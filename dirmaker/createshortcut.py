import os, winshell
from win32com.client import Dispatch

desktop = winshell.desktop() #base directory for desktop

path = os.path.join(desktop, "Run Directory Maker.lnk")  # the shortcuts path

wDir = os.getcwd() #get the current directory

target = os.path.join(wDir, "runapp.cmd")            

iconpath = os.path.join(wDir, "icon.ico")

shell = Dispatch('WScript.Shell') #dunno what this does

shortcut = shell.CreateShortCut(path) #created shortcut 

shortcut.Targetpath = target

shortcut.WorkingDirectory = wDir

shortcut.IconLocation = iconpath

shortcut.save() #saves the shortcut
