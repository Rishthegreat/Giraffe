from tkinter import *
from tkinter import messagebox

import tkinter as tk


def retrieve_input():
    inputValue = textBox.get("1.0", "end-1c")
    global code
    code = inputValue
    buttonCommit.destroy()
    textBox.destroy()
    b_encode.place(relx=0, rely=0, relheight=1, relwidth=0.5)
    b_decode.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)
    print(code)


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
        for item in code:
            item = ord(item)
            item = str(item)
            help.append(item)
        code = help
        code = listToString(code)
        print(code)
        actual = "Ascii, numbers"
        pathway.append("a")
        print(pathway)
        lastcompletedfunc = "ascii"
        currentvalue = 1
        newset = 0


    else:
        messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")


def notascii():
    global code, pathway, lastcompletedfunc, string, currentvalue
    currentvalue = 1
    if newset != currentvalue:
        string = code
        code = split(code)
        help = []
        print(code)
        for item in code:
            item = chr(int(item))
            print(item)
            help.append(item)
        print(help)
        code = help
        print(code)
        code = listToString(code)
        print(code)
        currentvalue = 0
        pathway.append("n")
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
        base = int(enterbox.get("1.0", "end-1c"))
        entbase.destroy()
        enterbox.destroy()
        code = code.split(" ")
        for index in range(0, len(code)):
            code[index] = tobase(code[index], 10, base)
        code = listToString(code)
        print(code)
        tobasewindow.destroy()
        pathway.append("b" + str(base))
        print(pathway)

    tobasewindow = tk.Tk()
    tobasewindow.geometry("600x400")
    entbase = tk.Button(tobasewindow, text="Enter the base you want to convert to and then click this button.",
                        command=inputforconversion)
    enterbox = tk.Text(tobasewindow)
    enterbox.place(relwidth=0.5, relheight=0.25, relx=0.25, rely=0)
    entbase.place(relwidth=0.75, relheight=0.4, relx=0.125, rely=0.45)
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
                    final = final + Final_code
            print(final)
            code = final
            print(code)
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
    print(code)
    b_encode.destroy()
    b_decode.destroy()
    root.title("Start making your code, the parentheses says what each conversion does")
    root.geometry("1000x800")
    b_ascii = Button(root, text="convert to ascii (Letters to Numbers)", fg="blue", command=ascii)
    b_ascii.place(relx=0, rely=0, relheight=0.5, relwidth=(1 / 3))
    b_ascii = Button(root, text="convert to letters from ascii (Numbers (base 10) to letters)", fg="blue",
                     command=notascii)
    b_ascii.place(relx=(1 / 3), rely=0, relheight=0.5, relwidth=(1 / 3))
    b_octal = Button(root, text="convert to any base (Numbers to Numbers)", fg="blue", command=beforetobase)
    b_octal.place(relx=(2 / 3), rely=0, relheight=0.5, relwidth=(1 / 3))
    b_cipher = Button(root, text="run your code through a cipher (Anything)", fg="blue", command=runthroughcipher)
    b_cipher.place(relx=0, rely=0.5, relheight=0.5, relwidth=(1 / 3))
    b_dontclick = Button(root, text="Last function applied", fg="blue", command=tell)
    b_dontclick.place(relx=(1 / 3), rely=0.5, relheight=0.5, relwidth=(1 / 3))
    b_check = Button(root, text="See what the current status of your code is", fg="blue", command=show)
    b_check.place(relx=(2 / 3), rely=0.5, relheight=0.5, relwidth=(1 / 3))


root = tk.Tk()
root.geometry("600x400")
output = []

b_encode = Button(root, text="Encode", fg="blue", command=yell)
b_decode = Button(root, text="Decode", fg="green")

code = ""
currentvalue = ""
pathway = []
lastcompletedfunc = ""
actual = ""

textBox = Text(root)
textBox.place(relx=0.125, rely=0, relheight=0.3, relwidth=0.75)
buttonCommit = Button(root, text="Upload text to be encoded or decoded, then click this button to continue",
                      command=retrieve_input)
buttonCommit.place(relx=0.125, rely=0.5, relheight=0.4, relwidth=0.75)

# when currentvalue equals 0, then it is only in letter form, when it is 1 it is only in numbers, when it is 2 it is in
# both letters and numbers (octal)
currentvalue = 0
newset = ""
newset = 0
string = ""
digits = ""
instring = ""
help = []
cipher = ""
currbase = 10

root.mainloop()
