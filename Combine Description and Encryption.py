import tkinter
from tkinter import *
from tkinter import messagebox

import tkinter as tk

root = tk.Tk()
x = ""
currentvalue = 0


def quit(self):
    self.root.destroy()

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    x = inputValue
    buttonCommit.destroy()
    textBox.destroy()
    messagebox.showinfo(Title=None, message="Close out of window to continue")
    print(x)


textBox=Text(root, height=4, width=40)
textBox.pack()
buttonCommit=Button(root, height=10, width=60, text="Upload text to be encoded or decoded, then click this button to continue",
                    command=lambda: retrieve_input())
buttonCommit.pack()

mainloop()

x = x
currentvalue = 0

def ascii():
    if currentvalue = 0:
        x = ord(x)
        print(x)
        currentvalue = "letters"


def yell():
    messagebox.showinfo(Title=None, message="This will begin encrypting your code")
    b_encode.destroy()
    b_decode.destroy()
    root = window
    root.title("Start making your code, the parentheses says what each conversion does")
    root.geometry("800x800")
    b_ascii = Button(topFrame, text="convert to ascii (Letters to Numbers)", fg="blue", command=ascii)
    b_ascii.config(height=25, width=45)
    b_ascii.pack(side=LEFT)
    b_octal = Button(topFrame, text="convert to octal (Numbers to Numbers)", fg="blue", command=octal)
    b_octal.config(height=25, width=45)
    b_octal.pack(side=LEFT)


window = Tk()


topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

b_encode = Button(topFrame, text="Encode", fg="blue", command=yell)
b_decode = Button(topFrame, text="Decode", fg="green")
b_encode.config(height=25, width=45)
b_decode.config(height=25, width=45)

b_encode.pack(side=LEFT)
b_decode.pack(side=LEFT)

window.mainloop()
