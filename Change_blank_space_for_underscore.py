# pip install tk
import os
from os import listdir
from os.path import isfile, join
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
folder_path = filedialog.askdirectory()

files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
print (files)

# all_files = os.listdir(folder_path)
# print (all_files)

for i in range(len(files)):
    newname = files[i].replace(" ", "_")
    os.rename(folder_path + "\\" + files[i], f"{folder_path}\\{newname}")
print (files)