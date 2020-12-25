from tkinter import *
from tkinter import messagebox
root = Tk()

x = ""
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    x = inputValue
    buttonCommit.destroy()
    textBox.destroy()
    messagebox.showinfo(Title=None, message="Close out of window to continue")
    print(x)

textBox = Text(root, height=4, width=40)
textBox.pack()
buttonCommit=Button(root, height=10, width=60, text="Upload text to be encoded or decoded, then click this button to continue",
                    command=lambda: retrieve_input())
buttonCommit.pack()

mainloop()


def ascii():
    ord(x)


def ascii1():
    b_ascii = Button(topFrame, text="convert to ascii", fg="blue", command=ascii)


def yell():
    messagebox.showinfo(Title=None, message="This will begin encrypting your code")
    b_encode.destroy()
    b_decode.destroy()
    ascii1


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
