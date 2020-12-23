from tkinter import *

window = Tk()

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

b_encode = Button(topFrame, text="Encode", fg="blue")
b_decode = Button(topFrame, text="Decode", fg="green")

b_encode.pack(side=LEFT)
b_decode.pack(side=LEFT)

window.mainloop()