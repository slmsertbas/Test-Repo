from tkinter import *
from tkinter import ttk
from main import generatePass

root = Tk()

root.geometry("480x360")
root.title("Password Generator")

frm = ttk.Frame(root, padding=30)
frm.grid()

sampleText = generatePass()

def clicked():
    a = ttk.Label(frm, text = sampleText).grid(column=0, row=3)
    

ttk.Label(frm, text="Click to generate your password!").grid(column=0, row=0)
ttk.Button(frm, text = "Generate Password", command = clicked).grid(column = 0, row = 1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)



root.mainloop()