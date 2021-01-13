from tkinter import *
from tkinter import messagebox

import tkinter as tk



root = tk.Tk()
coolFrame = Frame(root)
coolFrame.pack()
notFrame = Frame(root)
notFrame.pack(side=BOTTOM)
output = []
# pathway is what happened

code = ""
currentvalue = ""
pathway = []
lastcompletedfunc = ""
actual = ""

def quit(self):
    self.root.destroy()


def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    global code
    code = inputValue
    buttonCommit.destroy()
    textBox.destroy()
    root.destroy()
    messagebox.showinfo(Title=None, message="Close out of window to continue")
    print(code)


textBox=Text(coolFrame, height=4, width=40)
textBox.pack()
buttonCommit=Button(notFrame, height=10, width=60, text="Upload text to be encoded or decoded, then click this button to continue",
                    command=lambda: retrieve_input())
buttonCommit.pack()

root.mainloop()

# when currentvalue equals 0, then it is only in letter form, when it is 1 it is only in numbers, when it is 2 it is in
# both letters and numbers (octal)
currentvalue = 0
newset = ""
newset = 0
string = ""
digits = ""
instring = ""
help = [] = ""
cipher = ""
currbase = 10


def num_there(s):
    return any(i.isdigit() for i in s)


def split(word):
    return [char for char in word]


def listToString(oflist):
    str1 = " "

    return (str1.join(oflist))


def ascii():
    global code, pathway, currentvalue, lastcompletedfunc, string, newset
    if newset == currentvalue:
        string = code
        help = []
        code = split(code)
        print(code)
        for item in code:
            item = ord(item)
            print(item)
            item = str(item)
            help.append(item)
        print(help)
        code = help
        print(code)
        code = listToString(code)
        print(code)
        actual = "Ascii, numbers"
        pathway = pathway + "a"
        lastcompletedfunc = "ascii"
        currentvalue = 1
        newset = 0


    else:
        messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")


def notascii(pathway=pathway, lastcompletedfunc = lastcompletedfunc, string=string, currentvalue=1):
    global code
    if newset != currentvalue:
        string = code
        code = split(code)
        help = []
        print(code)
        for item in code:
            item = chr(item)
            print(item)
            help.append(item)
        print(help)
        code = help
        print(code)
        code = listToString(code)
        print(code)
        currentvalue = 0
        pathway = pathway + "n"
        lastcompletedfunc = "notascii"
        actual = "notascii, letters"
    else:
        messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")


def tobase(n, currbase, finbase):
    n = str(n)
    orignal = "0123456789ABCDEF"
    answerint = 0
    converted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for x in range((len(n) - 1), -1, -1):
        answerint += (converted[orignal.index(n[x])]) * (currbase ** ((len(n) - 1) - x))
    if finbase != 10:
        def tobase1(n1, base):
            orignal = "0123456789ABCDEF"
            if n1 < base:
                return orignal[n1]
            else:
                return tobase1(n1 // base, base) + orignal[(n1 % base)]

        return tobase1(answerint, finbase)
    else:
        return answerint

def beforetobase():
    global code, pathway
    def inputforconversion():
        global code
        base = int(enterbox.get("1.0","end-1c"))
        entbase.destroy()
        enterbox.destroy()
        code = code.split(" ")
        print(code)
        for index in range(0, len(code)):
            code[index] = tobase(code[index], 10, base)
        print(code)
        code = listToString(code)
        print(code)
        tobasewindow.destroy()
    tobasewindow = tk.Tk()
    tobasewindow.geometry("600x400")
    entbase = tk.Button(tobasewindow, text="Enter the base you want to convert to and then click this button.", command=inputforconversion)
    enterbox = tk.Text(tobasewindow)
    enterbox.place(relwidth=0.5, relheight=0.25, relx=0.25, rely=0)
    entbase.place(relwidth=0.75, relheight=0.4, relx=0.125, rely=0.45)
    print(code)
    tobasewindow.mainloop()



def runthroughcipher():
    global code, currentvalue, pathway
    if num_there(code):
        if "o" in code:
            cipher = "áéíóúüñ¿¡"
            digits = "12345670o"
            instring = code
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
            code = final
            print(code )
            currentvalue = 2
            pathway = pathway + "d"
            actual = "octal, numbers"
        else:
            cipher = "áéíóúüñ¿¡€"
            digits = "1234567890"
            instring = code
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
            code = final
            print(code)
            currentvalue = 2
            pathway = pathway + "o"
            actual = "octal, numbers"
    else:
        cipher = "1234567890áéíóúüñ¿¡[]/,.;':!@#$%^&*()_+=-?><ùûÿ€«»—æ"
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        instring = code
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
        code = final
        print(code)
        currentvalue = 3
        pathway = pathway + "d"
        actual = "cipher, accents"


def tell():
    messagebox.showinfo(Title=None, message=actual)


def show():
    messagebox.showinfo(Title=None, message=code)


def yell():
    messagebox.showinfo(Title=None, message="This will begin encrypting your code")
    print(code)
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
    b_octal = Button(topFrame, text="convert to any base (Numbers to Numbers)", fg="blue", bg = "red", command=beforetobase)
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
