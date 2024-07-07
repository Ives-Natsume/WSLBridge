import tkinter as tk
from tkinter import scrolledtext
from lib import *


# handler
def on_copy_win_to_linux():
    winFilePath = entry_win_file.get()
    linuxTargetPath = entry_linux_path.get()
    result = cp_win_to_linux(winFilePath, linuxTargetPath)
    text_result.insert(tk.END, result + "\n")

def on_copy_linux_to_win():
    linuxFilePath = entry_linux_file.get()
    winTargetPath = entry_win_path.get()
    result = cp_linux_to_win(linuxFilePath, winTargetPath)
    text_result.insert(tk.END, result + "\n")

def on_winPath_to_linuxPath():
    win_path = entry_win_path.get()
    result = winPath_to_linuxPath(win_path)
    text_result.insert(tk.END, result + "\n")

def on_mv_win_to_linux():
    winFilePath = entry_win_file.get()
    linuxTargetPath = entry_linux_path.get()
    result = mv_win_to_linux(winFilePath, linuxTargetPath)
    text_result.insert(tk.END, result + "\n")

def on_mv_linux_to_win():
    linuxFilePath = entry_linux_file.get()
    winTargetPath = entry_win_path.get()
    result = mv_linux_to_win(linuxFilePath, winTargetPath)
    text_result.insert(tk.END, result + "\n")


# gui
root = tk.Tk()
root.title("W&L Bridge")

root.iconbitmap('app_icon.ico')


# input zone
input_zone = tk.Frame(root)
input_zone.pack()

label_win_file = tk.Label(input_zone, text="Windows File Path:")
label_win_file.pack(anchor= "w")

entry_win_file = tk.Entry(input_zone, width=80)
entry_win_file.pack(anchor= "w")

label_linux_path = tk.Label(input_zone, text="Linux Target Path:")
label_linux_path.pack(anchor= "w")

entry_linux_path = tk.Entry(input_zone, width=80)
entry_linux_path.pack(anchor= "w")

label_linux_file = tk.Label(input_zone, text="Linux File Path:")
label_linux_file.pack(anchor= "w")

entry_linux_file = tk.Entry(input_zone, width=80)
entry_linux_file.pack(anchor= "w")

label_win_path = tk.Label(input_zone, text="Windows Target Path:")
label_win_path.pack(anchor= "w")

entry_win_path = tk.Entry(input_zone, width=80)
entry_win_path.pack(anchor= "w")


# output zone
output_zone = tk.Frame(root)
output_zone.pack(pady= 20)


label_text = tk.Label(output_zone, text="Command Output:")
label_text.pack(anchor= "w")
text_result = scrolledtext.ScrolledText(output_zone, width=78, height=20)
#text_result["font"] = custom_font
text_result.pack(anchor= "w")



# operate zone
operate_zone = tk.Frame(root)
operate_zone.pack()


# cp button
cp_zone = tk.Frame(operate_zone)
cp_zone.pack(side="left",padx=10, pady= 20)

button_copy_win_to_linux = tk.Button(cp_zone, text="Copy Windows File to Linux", command=on_copy_win_to_linux)
button_copy_win_to_linux.pack()

button_copy_linux_to_win = tk.Button(cp_zone, text="Copy Linux File to Windows", command=on_copy_linux_to_win)
button_copy_linux_to_win.pack()


# mv button
mv_zone = tk.Frame(operate_zone)
mv_zone.pack(side="left",padx=10, pady= 20)

button_mv_win_to_linux = tk.Button(mv_zone, text="Move Windows File to Linux", command= on_mv_win_to_linux)
button_mv_win_to_linux.pack()

button_mv_linux_to_win = tk.Button(mv_zone, text="Move Linux File to Windows", command= on_mv_linux_to_win)
button_mv_linux_to_win.pack()


# style transfer button
transfer_zone = tk.Frame(operate_zone)
transfer_zone.pack(side= "top",padx=10, pady= 20)

button_winPath_to_linuxPath = tk.Button(transfer_zone, text="Win Path to Linux Path", command= on_winPath_to_linuxPath)
button_winPath_to_linuxPath.pack(side= "top")


root.mainloop()
