from tkinter import *
from tkinter import messagebox

import tkinter as tk



root = tk.Tk()
coolFrame = Frame(root)
coolFrame.pack()
notFrame = Frame(root)
notFrame.pack(side=BOTTOM)



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
    root.destroy()
    messagebox.showinfo(Title=None, message="Close out of window to continue")
    print(x)
    print(x)
    other_function()
    print(x)
    print(x)


textBox=Text(coolFrame, height=4, width=40)
textBox.pack()
buttonCommit=Button(notFrame, height=10, width=60, text="Upload text to be encoded or decoded, then click this button to continue",
                    command=lambda: retrieve_input())
buttonCommit.pack()

root.mainloop()

x = x
# when currentvalue equals 0, then it is only in letter form, when it is 1 it is only in numbers, when it is 2 it is in
# both letters and numbers (octal)
currentvalue = 0
newset = ""
newset = 0
string = ""
digits = ""
instring = ""
help = []= ""
cipher = ""
currbase = 10


def num_there(s):
    return any(i.isdigit() for i in s)


def split(word):
    return [char for char in word]


def listToString(oflist):
    str1 = " "

    return (str1.join(oflist))


def ascii(currentvalue=currentvalue, pathway=pathway, lastcompletedfunc = lastcompletedfunc, string = string, x=x,
          newset=0):
    if newset == currentvalue:
        string = x
        help = []
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
        pathway = pathway + "a"
        lastcompletedfunc = "ascii"
        currentvalue = 1
        newset = 0
    else:
        messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")


def notascii(pathway=pathway, lastcompletedfunc = lastcompletedfunc, string=string, x=x, currentvalue=1):
    if newset != currentvalue:
        string = x
        x = split(x)
        help = []
        print(x)
        for item in x:
            item = chr(item)
            print(item)
            help.append(item)
        print(help)
        x = help
        print(x)
        x = listToString(x)
        print(x)
        currentvalue = 0
        pathway = pathway + "n"
        lastcompletedfunc = "notascii"
        actual = "notascii, letters"
    else:
        messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")


def tobase(x, currbase, finbase):
    newstring = x
    newwind = tk.Tk()
    textBox = Text(newwind, height=4, width=40)
    textBox.pack()
    buttonCommit = Button(newwind, height=10, width=60,
                          text="Upload text to be encoded or decoded, then click this button to continue",
                          command=lambda: retrieve_input())
    buttonCommit.pack()

    root.mainloop()
    finbase = x
    newstring = str(newstring)
    orignal = "0123456789ABCDEF"
    answerint = 0
    converted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for x in range((len(newstring) - 1), -1, -1):
        answerint += (converted[orignal.index(newstring[x])]) * (currbase ** ((len(newstring) - 1) - x))
    if finbase != 10:
        def tobase1(n1, base):
            orignal = "0123456789ABCDEF"
            if n1 < base:
                return orignal[n1]
            else:
                return tobase1(n1 // base, base) + orignal[(n1 % base)]

        x = tobase1(answerint, finbase)
        currbase = finbase
    else:
        x = answerint
        currbase = finbase



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
    root.attributes("-fullscreen", True)
    root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
    root.title("Start making your code, the parentheses says what each conversion does")
    root.geometry("1920x1080")
    b_ascii = Button(topFrame, text="convert to ascii (Letters to Numbers)", fg="blue", command=ascii)
    b_ascii.config(height=25, width=45)
    b_ascii.pack(side=LEFT)
    b_ascii = Button(topFrame, text="convert to letters from ascii (Numbers to letters (note octal will not work))", fg="blue", command=notascii)
    b_ascii.config(height=25, width=45)
    b_ascii.pack(side=LEFT)
    b_octal = Button(topFrame, text="convert to any base (Numbers to Numbers)", fg="blue", bg = "red", command=tobase)
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