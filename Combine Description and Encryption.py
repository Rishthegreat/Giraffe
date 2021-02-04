from tkinter import *
from tkinter import messagebox
import clipboard
import os
import sys

import tkinter as tk


# pathway/code/bases/twodig/onedig/ciphersused/length of pathway

def retrieve_input():
    global textBox, buttonCommit
    inputValue = textBox.get("1.0", "end-1c")
    global code
    code = inputValue
    buttonCommit.destroy()
    textBox.destroy()
    b_encode.place(relx=0, rely=0, relheight=1, relwidth=0.5)
    b_decode.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)
    print(code)


def isthere(s, j):
    if j == 'digit':
        return any(i.isdigit() for i in s)
    elif j == 'lowletter':
        return any(i.islower() for i in s)


def nolowletter(d):
    return any(i.islower() for i in d)


def num_there(s):
    return any(i.isdigit() for i in s)


def split(word):
    return [char for char in word]


def listToString(oflist):
    str1 = ""
    return (str1.join(oflist))


def newdigits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


def ascii():
    global code, pathway, currentvalue, lastcompletedfunc, string, newset, bases, twodig, onedig
    string = code
    help = []
    code = split(code)
    for item in range(0, len(code)):
        code[item] = str(ord(code[item]))
        help.append(code[item])
    for item in range(0, len(help)):
        help[item] = int(help[item])
        if newdigits(help[item]) == 2:
            twodig.append(str(item))
            twodig.append(",")
        if newdigits(help[item]) == 1:
            onedig.append(str(item))
            onedig.append(",")
        help[item] = str(help[item])
    code = listToString(help)
    onedig.append(";")
    twodig.append(";")
    print(code)
    print(twodig)
    print(onedig)
    actual = "Ascii, numbers"
    pathway.append("a")
    print(pathway)
    lastcompletedfunc = "ascii"
    currentvalue = 1
    newset = 0
    bases.append("10")
    bases.append(",")


def notascii():
    global code, pathway, lastcompletedfunc, string, currentvalue, twodig, onedig

    # string = code

    code = code.split(" ")
    help = []
    print(code)
    for item in code:
        item = chr(int(item))
        print(item)
        help.append(item)
    print(help)
    code = "".join(help)
    print(code)
    currentvalue = 0
    pathway.append("n")
    lastcompletedfunc = "notascii"
    actual = "notascii, letters"


# messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")


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
                return str(orignal[n1])
            else:
                return str(tobase1(n1 // base, base) + orignal[(n1 % base)])

        return str(tobase1(answerint, finbase))
    else:
        return str(answerint)


def beforetobase():
    global code, pathway, currentvalue, bases

    def inputforconversion():
        global code, currentvalue, bases
        base = int(enterbox.get("1.0", "end-1c"))
        entbase.destroy()
        enterbox.destroy()
        code = tobase(code, int(bases[len(bases) - 2]), int(base))
        print(code)
        tobasewindow.destroy()
        pathway.append("b")
        bases.append(str(base))
        bases.append(",")
        print(pathway)
        print(bases)
        currentvalue = 2

    if currentvalue == 0:
        messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")
    else:
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
    if isthere(code, 'digit') and not isthere(code, 'lowletter'):
        cipher = "áéíóúüñ¿¡€ëïमपजट"
        digits = "1234567890ABCDEF"
        instring = code
        word = ""
        Final_code = ""
        answer = instring
        length = len(instring)
        Final_sentence = ""
        final = ""
        if answer == instring:
            for counter in range(0, length):
                Final_code = (cipher[digits.index(instring[counter])])
                Final_code = ''.join(Final_code)
                final = final + Final_code
        print(final)
        code = final
        print(code)
        currentvalue = 2
        pathway.append("d")
        ciphersused.append("1")
        actual = "octal, numbers"
    else:
        if "," in code or "." in code or "?" in code or "!" in code or "(" in code or ";" in code or ":" in code:
            cipher = "बगहदजडपरकतचटमनवलसयஆஈஊஐஏளறனடணஅஇஉஎகபமதநயௌஓஒவஙலரழБГДЁЖИЙКЛПФУЦЧШЩЪЫЬЭЮЯѣѳѵé"
            digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890,.?;:!$() "
            instring = code
            word = ""
            Final_code = ""
            final = ""
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
            pathway.append("d")
            ciphersused.append("2")
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
            final = ""
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
            pathway.append("d")
            ciphersused.append("3")
            actual = "cipher, accents"


def show():
    messagebox.showinfo(Title=None, message=code)


def complete():
    global code, pathway, bases, twodig, onedig, cipherused, b_encode, b_decode, b_ascii, b_nascii, b_octal, b_cipher, b_dontclick, b_check, b_complete, b_functions, b_nothing, textBox, buttonCommit
    x = "/"
    showcode = [listToString(pathway), code, x, listToString(bases), x, listToString(twodig), x, listToString(onedig),
                x, listToString(ciphersused), x, str(len(pathway))]
    finalcode = listToString(showcode)
    clipboard.copy(finalcode)
    messagebox.showinfo(Title=None, message="Your code is " + finalcode + " and it has been copied to your clipboard")
    code = ""
    pathway, bases, twodig, onedig, cipherused = [], [], [], [], []
    b_ascii.destroy()
    b_nascii.destroy()
    b_octal.destroy()
    b_cipher.destroy()
    b_dontclick.destroy()
    b_check.destroy()
    b_complete.destroy()
    b_functions.destroy()
    b_nothing.destroy()
    create_buttons()
    textBox = Text(root)
    textBox.place(relx=0.125, rely=0, relheight=0.3, relwidth=0.75)
    buttonCommit = Button(root, text="Upload text to be encoded or decoded, then click this button to continue",
                          command=retrieve_input)
    buttonCommit.place(relx=0.125, rely=0.5, relheight=0.4, relwidth=0.75)


def Eashan():
    global code
    code = "Eashan"


def replace():
    def retrieve_input2():
        global code
        inputValue = textboxx.get("1.0", "end-1c")
        code = inputValue
        ButtonCommitx.destroy()
        textboxx.destroy()
        TK.destroy()
        print(code)

    global code
    code = ""
    TK = tk.Tk()
    TK.geometry("600x400")
    textboxx = Text(TK)
    textboxx.place(relx=0.125, rely=0, relheight=0.3, relwidth=0.75)
    ButtonCommitx = Button(TK, text="Apply your new words", command=retrieve_input2)
    ButtonCommitx.place(relx=0.125, rely=0.5, relheight=0.4, relwidth=0.75)
    TK.mainloop()


def decode():
    global code, decode_code, b_encode, b_decode, textBox, buttonCommit

    def a():
        global decode_code, thereisonedig, thereistwodig
        thereisonedig = False
        thereistwodig = False
        onedigsp = decode_onedig[-1]
        twodigsp = decode_twodig[-1]
        codetemp = []
        codeindex = 0
        coderange = 0
        if len(onedigsp) > 1:
            onedigsp = onedigsp.split(",")
            onedigsp.pop()
            thereisonedig = True
        if len(twodigsp) > 1:
            twodigsp = twodigsp.split(",")
            twodigsp.pop()
            thereistwodig = True
        for index in range(0, len(onedigsp)):
            onedigsp[index] = int(onedigsp[index])
        for index in range(0, len(twodigsp)):
            twodigsp[index] = int(twodigsp[index])
        while coderange < len(decode_code):
            if thereisonedig and codeindex in onedigsp:
                codetemp.append(decode_code[coderange:(coderange + 1)])
                coderange += 1
            elif thereistwodig and codeindex in twodigsp:
                codetemp.append(decode_code[coderange:(coderange + 2)])
                coderange += 2
            else:
                codetemp.append(decode_code[coderange:(coderange + 3)])
                coderange += 3
            codeindex += 1
        for index in range(0, len(codetemp)):
            codetemp[index] = chr(int(codetemp[index]))
        decode_code = listToString(codetemp)

    code = code.split("/")
    decode_pathway = []
    decode_code = code[0]
    decode_bases = code[1]
    decode_twodig = code[2]
    decode_onedig = code[3]
    decode_cipherused = code[4]
    decode_lenpath = int(code[5])
    for index in range(0, decode_lenpath):
        decode_pathway.append(decode_code[index])
    decode_code = decode_code[decode_lenpath:]
    decode_onedig = decode_onedig.split(";")
    decode_twodig = decode_twodig.split(";")
    decode_onedig.pop()
    decode_twodig.pop()
    decode_bases = decode_bases.split(",")
    decode_bases.pop()
    for y in range((len(decode_pathway) - 1), -1, -1):
        if decode_pathway[y] == "a":
            a()
            decode_onedig.pop()
            decode_twodig.pop()
            decode_bases.pop()
            print(decode_code)
        elif decode_pathway[y] == "b":
            decode_code = tobase(str(decode_code), int(decode_bases[len(decode_bases) - 1]),
                                 int(decode_bases[len(decode_bases) - 2]))
            decode_bases.pop()
        elif decode_pathway[y] == "c":
            decode_cipherused = decode_cipherused.split()
            if decode_cipherused[-1] == '1':
                cipher = "áéíóúüñ¿¡€ëïमपजट"
                digits = "1234567890ABCDEF"
                instring = decode_code
                word = ""
                Final_code = ""
                final = ""
                answer = instring
                length = len(instring)
                Final_sentence = ""
                if answer == instring:
                    for counter in range(0, length):
                        Final_code = (digits[cipher.index(instring[counter])])
                        Final_code = ''.join(Final_code)
                        final = final + Final_code
                    decode_code = final
            elif decode_cipherused[-1] == '2':
                cipher = "बगहदजडपरकतचटमनवलसयஆஈஊஐஏளறனடணஅஇஉஎகபமதநயௌஓஒவஙலரழБГДЁЖИЙКЛПФУЦЧШЩЪЫЬЭЮЯѣѳѵé"
                digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890,.?;:!$() "
                instring = decode_code
                word = ""
                Final_code = ""
                final = ""
                answer = instring
                length = len(instring)
                Final_sentence = ""
                if answer == instring:
                    for counter in range(0, length):
                        Final_code = (digits[cipher.index(instring[counter])])
                        Final_code = ''.join(Final_code)
                        final = final + Final_code
                    decode_code = final
            elif decode_cipherused[-1] == '3':
                cipher = "1234567890áéíóúüñ¿¡[]/,.;':!@#$%^&*()_+=-?><ùûÿ€«»—æ"
                letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                instring = decode_code
                word = ""
                Final_code = ""
                answer = instring
                length = len(instring)
                Final_sentence = ""
                final = ""
                if answer == instring:
                    for counter in range(0, length):
                        Final_code = (letters[cipher.index(instring[counter])])
                        Final_code = ''.join(Final_code)
                        final = final + Final_code
                    decode_code = final
        elif decode_pathway[y] == "f":

        elif decode_pathway[y] == "s":

        elif decode_pathway[y] == "f":

    print(decode_code)
    messagebox.showinfo(Title=None, message="The decoded characters is: " + decode_code)
    b_encode.destroy()
    b_decode.destroy()
    create_buttons()
    textBox = Text(root)
    textBox.place(relx=0.125, rely=0, relheight=0.3, relwidth=0.75)
    buttonCommit = Button(root, text="Upload text to be encoded or decoded, then click this button to continue",
                          command=retrieve_input)
    buttonCommit.place(relx=0.125, rely=0.5, relheight=0.4, relwidth=0.75)


def yell():
    print(code)
    global b_encode, b_decode, b_ascii, b_nascii, b_octal, b_cipher, b_dontclick, b_check, b_complete, b_functions, b_nothing
    b_encode.destroy()
    b_decode.destroy()
    root.title("Start making your code, the parentheses says what each conversion does")
    root.geometry("1000x1000")
    b_ascii.place(relx=0, rely=0, relheight=(1 / 3), relwidth=(1 / 3))
    b_nascii.place(relx=(1 / 3), rely=0, relheight=(1 / 3), relwidth=(1 / 3))
    b_octal.place(relx=(2 / 3), rely=0, relheight=(1 / 3), relwidth=(1 / 3))
    b_cipher.place(relx=0, rely=(1 / 3), relheight=(1 / 3), relwidth=(1 / 3))
    b_check.place(relx=(2 / 3), rely=(1 / 3), relheight=(1 / 3), relwidth=(1 / 3))
    b_complete.place(relx=0, rely=(2 / 3), relheight=(1 / 3), relwidth=(1 / 3))
    b_functions.place(relx=(1 / 3), rely=(2 / 3), relheight=(1 / 3), relwidth=(1 / 3))
    b_nothing.place(relx=(2 / 3), rely=(2 / 3), relheight=(1 / 3), relwidth=(1 / 3))


def create_buttons():
    global b_encode, b_decode, b_ascii, b_nascii, b_octal, b_cipher, b_dontclick, b_check, b_complete, b_functions, b_nothing
    b_encode = Button(root, text="Encode", fg="blue", command=yell)
    b_decode = Button(root, text="Decode", fg="green", command=decode)
    b_ascii = Button(root, text="convert to ascii (Letters to Numbers)", fg="blue", command=ascii)
    b_nascii = Button(root, text="convert to letters from ascii (Numbers (base 10) to letters)", fg="blue",
                      command=notascii)
    b_octal = Button(root, text="Convert to any base (Numbers to Numbers)", fg="blue", command=beforetobase)
    b_cipher = Button(root, text="Run your code through a cipher (Anything)", fg="blue", command=runthroughcipher)
    b_check = Button(root, text="See what the current status of your code is", fg="blue", command=show)
    b_complete = Button(root, text="Find your completed code", fg="blue", command=complete)
    b_functions = Button(root, text="See all the Functions", fg="blue", command=Eashan)
    b_nothing = Button(root, text="Restart", fg="blue", command=replace)


root = tk.Tk()
French = Button()
German = Button()
Spanish = Button()
language = ""
root.geometry("600x400")
output = []
bases = []
onedig = []
twodig = []
ciphersused = []
b_encode = Button()
b_decode = Button()
b_ascii = Button()
b_nascii = Button()
b_octal = Button()
b_cipher = Button()
b_dontclick = Button()
b_check = Button()
b_complete = Button()
b_functions = Button()
b_nothing = Button()
buttonCommit = Button()
textBox = Text()

textBox = Text(root)
textBox.place(relx=0.125, rely=0, relheight=0.3, relwidth=0.75)
buttonCommit = Button(root, text="Upload text to be encoded or decoded, then click this button to continue",
                      command=retrieve_input)
buttonCommit.place(relx=0.125, rely=0.5, relheight=0.4, relwidth=0.75)

create_buttons()

code = ""
decode_code = ""
currentvalue = ""
pathway = []
lastcompletedfunc = ""
actual = ""

# when currentvalue equals 0, then it is only in letter form, when it is 1 it is only in numbers, when it is 2 it is in
# both letters and numbers (non base 10 integer)
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
