import tkinter as tk
from tkinter import *

# Developer Imports
import main

top = tk.Tk()
top.resizable(0, 0)
top.title('Enter Userid')


#use this for button click
def button_call_back():
    print("callback worked!")
    #get the input
    user_id = myEntry.get()
    main.run(user_id)
    if user_id.strip() != "":
        print(user_id)
        myEntry.delete(0, tk.END)


def cancel_call_back():
    print("cancel")
    top.destroy()


btn_ok = tk.Button(top, text ="Ok", command = button_call_back)
btn_cancel = tk.Button(top, text ="Cancel", command = cancel_call_back)
top.geometry("500x100")
label = tk.Label(top, text = "UserId")
label.pack()

myEntry = tk.Entry(top, width=200)
myEntry.focus()
myEntry.bind("<Return>", button_call_back)
myEntry.pack(padx=15)

btn_ok.pack(side=tk.LEFT, padx=15)
btn_cancel.pack(side=tk.RIGHT, padx=15)

#display this on error response, one problem you need to import MessageBox, glux chem hanum sra importneric
#messagebox.showwarning("Warning","Warning message")

top.mainloop()

