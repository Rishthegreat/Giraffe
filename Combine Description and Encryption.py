import tkinter
from tkinter import *
from tkinter import messagebox

import tkinter as tk

root = tk.Tk()
x = ""
currentvalue = ""
pathway = ""
lastcompletedfunc = ""
actual = ""

def quit(self):
    self.root.destroy()

def other_function():
    global x
    print(x)
    print(x)

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    global x
    x = inputValue
    buttonCommit.destroy()
    textBox.destroy()
    messagebox.showinfo(Title=None, message="Close out of window to continue")
    print(x)
    print(x)
    other_function()
    print(x)
    print(x)


textBox=Text(root, height=4, width=40)
textBox.pack()
buttonCommit=Button(root, height=10, width=60, text="Upload text to be encoded or decoded, then click this button to continue",
                    command=lambda: retrieve_input())
buttonCommit.pack()

mainloop()

x = x
currentvalue=0
newset = ""
newset = 0
string = ""
cipher = ""
digits = ""
instring = ""
help = []


def num_there(s):
    return any(i.isdigit() for i in s)


def split(word):
    return [char for char in word]


def listToString(oflist):
    str1 = " "

    return (str1.join(oflist))


def ascii(currentvalue=currentvalue, pathway=pathway, lastcompletedfunc = lastcompletedfunc, string = string, x=x):
    if newset == currentvalue:
        string = x
        x = split(x)
        print(x)
        for item in x:
            item = ord(item)
            print(item)
            item = str(item)
            help.append(item)
        print(help)
        x = help
        print(x)
        x = listToString(x)
        print(x)
        actual = "Ascii, numbers"
        print(actual)
        currentvalue = 1
    else:
        messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")


def notascii(currentvalue=currentvalue, pathway=pathway, lastcompletedfunc = lastcompletedfunc, string=string):
    if newset != currentvalue:
        x = string
        string = str(string)
        x = chr(string)
        print(x)
        currentvalue = 1
        pathway = pathway + "a"
        lastcompletedfunc = "ascii"
        actual = "ascii, letters"
    else:
        messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")


def octal(currentvalue=currentvalue, x=x, pathway=pathway, lastcompletedfunc=lastcompletedfunc):
    if newset != currentvalue:
        x = oct(x)
        print(x)
        currentvalue == 1
        pathway = pathway + "8"
        lastcompletedfunc = "octal"
        actual = "octal, numbers"
    else:
        messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")


def runthroughcipher(currentvalue=currentvalue, x=x, pathway=pathway):
    if num_there(x):
        if "o" in x:
            cipher = "áéíóúüñ¿¡"
            digits = "12345670o"
            instring = x
            word = ""
            Final_code = ""
            answer = instring
            length = len(instring)
            Final_sentence = ""
            if answer == instring:
                for counter in range(0, length):
                    Final_code = (cipher[digits.index(instring[counter])])
                    Final_code = ''.join(Final_code)
                    # print(Final_code)
                    final = final + Final_code
            print(final)
            x = final
            print(x)
            currentvalue = 2
            pathway = pathway + "d"
            actual = "octal, numbers"
        else:
            cipher = "áéíóúüñ¿¡€"
            digits = "1234567890"
            instring = x
            word = ""
            Final_code = ""
            answer = instring
            length = len(instring)
            Final_sentence = ""
            if answer == instring:
                for counter in range(0, length):
                    Final_code = (cipher[digits.index(instring[counter])])
                    Final_code = ''.join(Final_code)
                    # print(Final_code)
                    final = final + Final_code
            print(final)
            x = final
            print(x)
            currentvalue = 2
            pathway = pathway + "o"
            actual = "octal, numbers"
    else:
        cipher = "1234567890áéíóúüñ¿¡[]/,.;':!@#$%^&*()_+=-?><ùûÿ€«»—æ"
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        instring = x
        word = ""
        Final_code = ""
        answer = instring
        length = len(instring)
        Final_sentence = ""
        if answer == instring:
            for counter in range(0, length):
                Final_code = (cipher[letters.index(instring[counter])])
                Final_code = ''.join(Final_code)
                # print(Final_code)
                final = final + Final_code
        print(final)
        x = final
        print(x)
        currentvalue = 3
        pathway = pathway + "d"
        actual = "cipher, accents"


def tell():
    messagebox.showinfo(Title=None, message=actual)


def show():
    messagebox.showinfo(Title=None, message=x)


def yell():
    messagebox.showinfo(Title=None, message="This will begin encrypting your code")
    print(x)
    b_encode.destroy()
    b_decode.destroy()
    root = window
    root.title("Start making your code, the parentheses says what each conversion does")
    root.geometry("1600x1600")
    b_ascii = Button(topFrame, text="convert to ascii (Letters to Numbers)", fg="blue", command=ascii)
    b_ascii.config(height=25, width=45)
    b_ascii.pack(side=LEFT)
    b_ascii = Button(topFrame, text="convert to letters from ascii (Numbers to letters (note octal will not work))", fg="blue", command=notascii)
    b_ascii.config(height=25, width=45)
    b_ascii.pack(side=LEFT)
    b_octal = Button(topFrame, text="convert to octal (Numbers to Numbers)", fg="blue", command=octal)
    b_octal.config(height=25, width=45)
    b_octal.pack(side=LEFT)
    b_cipher = Button(topFrame, text="run your code through a cipher (Anything)", fg="blue", command=runthroughcipher)
    b_cipher.config(height=25, width=45)
    b_cipher.pack(side=LEFT)
    b_dontclick = Button(topFrame, text="Last function applied", fg="blue", command=tell)
    b_dontclick.config(height=25, width=45)
    b_dontclick.pack(side=LEFT)
    b_check = Button(topFrame, text="See what the current status of your code is", fg="blue", command=show)
    b_check.config(height=25, width=45)
    b_check.pack(side=LEFT)


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
