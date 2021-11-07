from tkinter import *
from tkinter import ttk
from main import generatePass

root = Tk()

root.geometry("480x360")
root.title("Password Generator")

mainfrm = ttk.Frame(root, padding = 20)
mainfrm.grid()


def clicked():
    text_result.set("")
    sampleText = generatePass()
    text_result.set(str(sampleText))
    
    

text_result = StringVar()
text_result.set("Password")    


label_pass = ttk.Label(mainfrm, textvariable=text_result).grid(column=0, row=3)
ttk.Label(mainfrm, text="Click to generate your password!").grid(column=0, row=0)
ttk.Button(mainfrm, text = "Generate Password", command = clicked).grid(column = 0, row = 1)
ttk.Button(mainfrm, text="Quit", command=root.destroy).grid(column=0, row=2)


#labelframe
frame = ttk.LabelFrame(mainfrm, text = "My Frame ", pad = 5)
frame.grid(column = 1, row = 1, padx = 5, pady = 5)
ttk.Label(frame, text = "Created Passwords", pad = 5).grid(column=1, row = 1)
ttk.Label(frame, text = "Created Passwords", pad = 5).grid(column=1, row = 2)
ttk.Label(frame, text = "Created Passwords", pad = 5).grid(column=1, row = 3)
ttk.Label(frame, text = "Created Passwords", pad = 5).grid(column=1, row = 4)
ttk.Label(frame, text = "Created Passwords", pad = 5).grid(column=1, row = 5)



root.mainloop()