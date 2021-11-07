from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=26, borderwidth=5)
e.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

text_result = StringVar()
text_result.set("")
label_result = Label(root, textvariable=text_result, width=8, borderwidth=5, relief="sunken").grid(column=2, row=0,padx=10, pady=10)


# Actions

def button_click(number):
    num = e.get()
    e.delete(0, END)
    e.insert(0, str(num) + str(number))


def button_clear():
    e.delete(0, END)
    e.insert(0, "")
    text_result.set("")


def button_addition():
    global num1
    num1 = e.get()
    e.delete(0, END)


def button_result():
    number = e.get()
    result = int(num1) + int(number)
    e.delete(0, END)
    final_result = str(result)
    text_result.set(final_result)


# Buttons

button_1 = Button(root, text="1", padx=30, pady=15, borderwidth=3, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=15, borderwidth=3, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=15, borderwidth=3, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=15, borderwidth=3, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=15, borderwidth=3, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=15, borderwidth=3, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=15, borderwidth=3, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=15, borderwidth=3, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=15, borderwidth=3, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=15, borderwidth=3, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=29, pady=15, borderwidth=3, command=button_addition)
button_result = Button(root, text="=", padx=76, pady=15, borderwidth=3, command=button_result)
button_clear = Button(root, text="CC", padx=72, pady=15, borderwidth=3, command=button_clear)

# Putting Buttons into grid formation

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_result.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()
