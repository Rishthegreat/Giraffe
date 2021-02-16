from tkinter import *
from tkinter import messagebox
import clipboard
from PIL import ImageTk, Image
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


# procedure to get a user input and store it for later processing

def isthere(s, j):
    if j == 'digit':
        return any(i.isdigit() for i in s)
    elif j == 'lowletter':
        return any(i.islower() for i in s)


# procedure to see if two things match

def nolowletter(d):
    return any(i.islower() for i in d)


# procedure to see if there are any lowercase letters in the code

def num_there(s):
    return any(i.isdigit() for i in s)


# procedure to see if there are any numbers in the code

def split(word):
    return [char for char in word]


def listToString(oflist):
    str1 = ""
    return (str1.join(oflist))


# converts a list into a string

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


# converts a string into ascii code

def calc():
    global code, pathway, lastcompletedfunc, string, currentvalue, twodig, onedig, bases, operations

    def add1():
        global code, pathway, lastcompletedfunc, string, currentvalue, twodig, onedig, bases, operations, inputValue

        def actadd():
            global code, pathway, lastcompletedfunc, string, currentvalue, twodig, onedig, bases, operations, inputValue
            inputValue = ntextBox.get("1.0", "end-1c")
            inputValue = int(inputValue)
            code = int(code)
            code += inputValue
            inputValue = str(inputValue)
            for item in inputValue:
                pathway.append(item)
            pathway.append("z")
            code = str(code)
            code = str(tobase(code, 10, int(bases[-2])))
            add2.destroy()
            ntextBox.destroy()
            addwin.destroy()

        add.destroy()
        subtract.destroy()
        multiply.destroy()
        divide.destroy()
        newind.destroy()
        addwin = tk.Tk()
        addwin.geometry("600x400")
        add2 = Button(addwin, text="commit addition", command=actadd)
        ntextBox = Text(addwin)
        add2.place(relx=0.125, rely=0.5, relheight=0.4, relwidth=0.75)
        ntextBox.place(relx=0.125, rely=0, relheight=0.3, relwidth=0.75)

    def subtract1():
        global code, pathway, lastcompletedfunc, string, currentvalue, twodig, onedig, bases, operations, inputValue

        def actsub():
            global code, pathway, lastcompletedfunc, string, currentvalue, twodig, onedig, bases, operations, inputValue
            inputValue = stextBox.get("1.0", "end-1c")
            inputValue = int(inputValue)
            code = int(code)
            code -= inputValue
            inputValue = str(inputValue)
            for item in inputValue:
                pathway.append(item)
            pathway.append("y")
            code = str(code)
            code = str(tobase(code, 10, int(bases[-2])))
            sub2.destroy()
            stextBox.destroy()
            subwin.destroy()
            print(code)

        add.destroy()
        subtract.destroy()
        multiply.destroy()
        divide.destroy()
        newind.destroy()
        subwin = tk.Tk()
        sub2 = Button(subwin, text="commit addition", command=actsub)
        stextBox = Text(subwin)
        subwin.geometry("600x400")
        sub2.place(relx=0.125, rely=0.5, relheight=0.4, relwidth=0.75)
        stextBox.place(relx=0.125, rely=0, relheight=0.3, relwidth=0.75)
        print(code)

    def multiply1():
        global code, pathway, lastcompletedfunc, string, currentvalue, twodig, onedig, bases, operations, inputValue

        def actmul():
            global code, pathway, lastcompletedfunc, string, currentvalue, twodig, onedig, bases, operations, inputValue
            inputValue = mtextBox.get("1.0", "end-1c")
            inputValue = int(inputValue)
            code = int(code)
            code *= inputValue
            code = str(code)
            code = str(tobase(code, 10, int(bases[-2])))
            inputValue = str(inputValue)
            for item in inputValue:
                pathway.append(item)
            pathway.append("x")
            mul2.destroy()
            mtextBox.destroy()
            mulwin.destroy()

        add.destroy()
        subtract.destroy()
        multiply.destroy()
        divide.destroy()
        newind.destroy()
        mulwin = tk.Tk()
        mul2 = Button(mulwin, text="commit addition", command=actmul)
        mtextBox = Text(mulwin)
        mulwin.geometry("600x400")
        mul2.place(relx=0.125, rely=0.5, relheight=0.4, relwidth=0.75)
        mtextBox.place(relx=0.125, rely=0, relheight=0.3, relwidth=0.75)
        print(code)

    def divide1():
        global code, pathway, lastcompletedfunc, string, currentvalue, twodig, onedig, bases, operations, inputValue

        def actdiv():
            global code, pathway, lastcompletedfunc, string, currentvalue, twodig, onedig, bases, operations, inputValue
            inputValue = dtextBox.get("1.0", "end-1c")
            inputValue = int(inputValue)
            code = int(code)
            if code % inputValue != 0:
                messtext = "Your code is " + str(code) + " and this is not divisible by " + str(inputValue)
                messagebox.showinfo(message=messtext)
                code = str(tobase(code, 10, int(bases[-2])))
            else:
                code /= inputValue
                code = str(int(code))
                code = str(tobase(code, 10, int(bases[-2])))
                inputValue = str(inputValue)
                for item in inputValue:
                    pathway.append(item)
                pathway.append("w")
                div2.destroy()
                dtextBox.destroy()
                divwin.destroy()
        add.destroy()
        subtract.destroy()
        multiply.destroy()
        divide.destroy()
        newind.destroy()
        divwin = tk.Tk()
        div2 = Button(divwin, text="commit addition", command=actdiv)
        dtextBox = Text(divwin)
        divwin.geometry("600x400")
        div2.place(relx=0.125, rely=0.5, relheight=0.4, relwidth=0.75)
        dtextBox.place(relx=0.125, rely=0, relheight=0.3, relwidth=0.75)
        print(code)

    # string = code
    if bases[-2] != 10:
        code = int(tobase(code, int(bases[-2]), 10))
    else:
        code = int(code)
    newind = tk.Tk()
    newind.geometry("600x400")
    add = Button(newind, text="Add a number", command=add1)
    subtract = Button(newind, text="Subtract a number", command=subtract1)
    multiply = Button(newind, text="Multiply a number", command=multiply1)
    divide = Button(newind, text="Divide a number", command=divide1)
    add.place(relx=0, rely=0, relheight=0.5, relwidth=0.5)
    subtract.place(relx=0.5, rely=0, relheight=0.5, relwidth=0.5)
    multiply.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.5)
    divide.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)


# messagebox.showinfo(Title=None, message="Not possible, please reread what will be changed by this button")


def tobase(n, currbase, finbase):
    n = str(n)    # n is the number that needs to be converted to another base
    currbase = int(currbase)
    original = "0123456789ABCDEF"
    answerint = 0
    referencenums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for x in range((len(n) - 1), -1, -1):
        answerint += (referencenums[original.index(n[x])]) * (currbase ** ((len(n) - 1) - x))   # Converts the number into base 10
    if finbase != 10:
        def tobase1(n1, base):
            if n1 < base:
                return str(original[n1])
            else:
                return str(tobase1(n1 // base, base) + original[(n1 % base)])   # Converts the number into the base that the user inputs (as a parameter called finbase)

        return str(tobase1(answerint, finbase))   # return type string
    else:
        return str(answerint)    # return type string


# converts a number to a different base

def beforetobase():
    global code, pathway, currentvalue, bases

    def inputforconversion():
        global code, currentvalue, bases
        currentbase = int(bases[-2])
        finalbase = int(enterbox.get("1.0", "end-1c"))
        code = tobase(code, currentbase, finalbase)
        entbase.destroy()
        enterbox.destroy()
        print(code)
        tobasewindow.destroy()
        pathway.append("b")
        bases.append(str(finalbase))
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
        pathway.append("c")
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
            pathway.append("c")
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
            pathway.append("c")
            ciphersused.append("3")
            actual = "cipher, accents"


# runs the code through a cipher


def show():
    messagebox.showinfo(Title=None, message=code)


def complete():
    global code, pathway, bases, twodig, onedig, cipherused, b_encode, b_decode, b_ascii, b_nascii, b_octal, b_cipher, b_dontclick, b_check, b_complete, b_functions, b_nothing, textBox, buttonCommit, Logo2
    x = "/"
    showcode = [listToString(pathway), str(code), x, listToString(bases), x, listToString(twodig), x,
                listToString(onedig),
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
    Logo2.destroy()
    create_buttons()
    textBox = Text(root)
    textBox.place(relx=0.125, rely=0, relheight=0.3, relwidth=0.75)
    buttonCommit = Button(root, text="Upload text to be encoded or decoded, then click this button to continue",
                          command=retrieve_input)
    buttonCommit.place(relx=0.125, rely=0.5, relheight=0.4, relwidth=0.75)


def function1():
    global code, language, French, Spanish, German, Numbers, pathway, code, bInLow, bInUp, bInNum, indextouse

    def toanotherlang(lower, upper, nums):
        global code
        code = list(code)  # Making the variable code a list so that it is easier to work with in the code
        lowletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z"]
        upperletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "W", "X", "Y", "Z"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if language == "French":
            pathway.append("f")
        elif language == "German":
            pathway.append(
                "g")  # Appending the corresponding letter for each language to pathway so that the during decoding, correct decoding functions will be executed
        elif language == "Spanish":
            pathway.append("s")
        for codeitem in range(0, len(code)):  # Iterating through every index of the list code
            for lowitem in range(0, len(lowletters)):
                if lowletters[lowitem] == code[
                    codeitem]:  # Iterates through all indexes of the uppercase and checks whether any of them match the current index of code
                    code[codeitem] = lower[
                        lowitem]  # If it matches, then it is replaced with the corresponding index of the items in the selected language
                    break
            for upitem in range(0, len(upperletters)):
                if upperletters[upitem] == code[
                    codeitem]:  # Iterates through all indexes of the uppercase and checks whether any of them match the current index of code
                    code[codeitem] = upper[
                        upitem]  # If it matches, then it is replaced with the corresponding index of the items in the selected language
                    break
            for numitem in range(0, len(numbers)):
                if numbers[numitem] == code[
                    codeitem]:  # Iterates through all indexes of the digits and checks whether any of them match the current index of code
                    code[codeitem] = nums[
                        numitem]  # If it matches, then it is replaced with the corresponding index of the items in the selected language
                    break
        code = listToString(code)  # A custom created function that converts the list back into a string
        print(code)  # Prints out the result

    def french():
        global language
        language = "French"
        lowerconversion = ["ah", "bey", "cay", "day", "euh", "eff", "jay", "ash", "ei", "gee", "kah", "el", "em", "en",
                           "oh", "pay", "cou", "air", "es", 'tay', "ou", "vay", "doublevay", "eeks", "egrecke", "zed"]
        upperconversion = []
        for item in lowerconversion:
            upperconversion.append(item.swapcase())
        print(upperconversion)
        numberconversion = ["Cero", "Un", "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf"]
        French.destroy()
        Spanish.destroy()
        German.destroy()
        Numbers.destroy()
        toanotherlang(lowerconversion, upperconversion, numberconversion)

    def spanish():
        global language
        language = "Spanish"
        French.destroy()
        Spanish.destroy()
        German.destroy()
        Numbers.destroy()
        upperconversion = []
        lowerconversion = ["ah", "be", "ce", "de", "eh", "efe", "ge", "hache", "ii", "jota", "ca", "ele", "eme", "ene",
                           "oh", "pe", "cu", "ere", "ese", "te", "uh", "ve", "dobleve", "equis", "igriega", "zeta"]
        for item in lowerconversion:
            upperconversion.append(item.swapcase())
        print(upperconversion)
        numberconversion = ["Cero", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"]
        toanotherlang(lowerconversion, upperconversion, numberconversion)

    def german():
        global language
        language = "German"
        French.destroy()
        Spanish.destroy()
        German.destroy()
        Numbers.destroy()
        upperconversion = []
        lowerconversion = ["ah", "be", "ce", "de", "eh", "efe", "ge", "ha", "ii", "jot", "ka", "el", "em", "en",
                           "oh", "pe", "ku", "er", "es", "te", "oo", "vau", "ve", "iks", "opsilon", "zet"]
        for item in lowerconversion:
            upperconversion.append(item.swapcase())
        numberconversion = ["Null", "Eins", "Zwei", "Drei", "Vier", "Funf", "Sechs", "Sieben", "Acht", "Neun"]
        toanotherlang(lowerconversion, upperconversion, numberconversion)

    Numbers = tk.Tk()
    Numbers.geometry("600x400")
    French = Button(Numbers, text="French", command=french)
    Spanish = Button(Numbers, text="Spanish", command=spanish)
    German = Button(Numbers, text="German", command=german)
    French.place(relwidth=(1 / 3), relheight=1, relx=0, rely=0)
    Spanish.place(relwidth=(1 / 3), relheight=1, relx=(1 / 3), rely=0)
    German.place(relwidth=(1 / 3), relheight=1, relx=(2 / 3), rely=0)
    Numbers.mainloop()


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
    global code, decode_code, b_encode, b_decode, textBox, buttonCommit, CanUpNum, CanNum, Nothing, numstem

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

    def toeng(lowerconversion, upperconversion, numberconversion):
        global decode_code
        lowletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z"]
        upperletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                        "S",
                        "T", "U", "V", "W", "X", "Y", "Z"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        indextouse = 0
        finalcode = []
        indexincrease = 2
        CanUpNum = True
        CanNum = False
        Nothing = False
        decode_code = list(decode_code)
        while indextouse <= len(decode_code) - 1:
            Value = decode_code[indextouse:(indextouse + 1)]
            Value = listToString(Value)
            if Value in lowletters or Value in upperletters or Value in numbers:
                Value = decode_code[indextouse:(indextouse + indexincrease)]
                Value = listToString(Value)
                for lowitem in range(0, len(lowerconversion)):
                    if Value == lowerconversion[lowitem]:
                        finalcode.append(lowletters[lowitem])
                        indextouse += indexincrease
                        indexincrease = 2
                        CanUpNum = False
                        CanNum = False
                        Nothing = False
                        break
                    else:
                        CanUpNum = True
                        Nothing = True
                if CanUpNum:
                    for upitem in range(0, len(upperconversion)):
                        if Value == upperconversion[upitem]:
                            finalcode.append(upperletters[upitem])
                            indextouse += indexincrease
                            indexincrease = 2
                            CanNum = False
                            Nothing = False
                            break
                        else:
                            CanNum = True
                            Nothing = True
                if CanNum:
                    for numitem in range(0, len(numberconversion)):
                        if Value == numberconversion[numitem]:
                            finalcode.append(numbers[numitem])
                            indextouse += indexincrease
                            indexincrease = 2
                            Nothing = False
                            break
                        else:
                            Nothing = True
                if Nothing:
                    indexincrease += 1
            else:
                indextouse += 1
                finalcode.append(Value)
                continue
        decode_code = listToString(finalcode)

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
    totalen = len(decode_pathway)
    currindex = 0
    numstouse = []
    numstem = []
    print(len(numstem))
    beginningindex = 0
    first = True
    print(decode_pathway)
    while totalen != currindex:
        if decode_pathway[currindex].isdigit():
            numstem.append(decode_pathway[currindex])
            if first:
                beginningindex = currindex
                first = False
            currindex += 1
            totalen = len(decode_pathway)
        else:
            if len(numstem) != 0:
                print(decode_pathway[currindex])
                numstouse.append(listToString(numstem))
                numstem = []
                first = True
                del decode_pathway[beginningindex:currindex]
                currindex = 0
                totalen = len(decode_pathway)
            else:
                currindex += 1
                totalen = len(decode_pathway)
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
            lowerconversion = ["ah", "bey", "cay", "day", "euh", "eff", "jay", "ash", "ei", "gee", "kah", "el", "em",
                               "en",
                               "oh", "pay", "cou", "air", "es", 'tay', "ou", "vay", "doublevay", "eeks", "egrecke",
                               "zed"]
            upperconversion = []
            for item in lowerconversion:
                upperconversion.append(item.swapcase())
            print(upperconversion)
            numberconversion = ["Cero", "Un", "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf"]
            toeng(lowerconversion, upperconversion, numberconversion)
        elif decode_pathway[y] == "s":
            upperconversion = []
            lowerconversion = ["ah", "be", "ce", "de", "eh", "efe", "ge", "hache", "ii", "jota", "ca", "ele", "eme",
                               "ene",
                               "oh", "pe", "cu", "ere", "ese", "te", "uh", "ve", "dobleve", "equis", "igriega", "zeta"]
            for item in lowerconversion:
                upperconversion.append(item.swapcase())
            numberconversion = ["Cero", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"]
            toeng(lowerconversion, upperconversion, numberconversion)
        elif decode_pathway[y] == "g":
            upperconversion = []
            lowerconversion = ["ah", "be", "ce", "de", "eh", "efe", "ge", "ha", "ii", "jot", "ka", "el", "em", "en",
                               "oh", "pe", "ku", "er", "es", "te", "oo", "vau", "ve", "iks", "opsilon", "zet"]
            for item in lowerconversion:
                upperconversion.append(item.swapcase())
            numberconversion = ["Null", "Eins", "Zwei", "Drei", "Vier", "Funf", "Sechs", "Sieben", "Acht", "Neun"]
            toeng(lowerconversion, upperconversion, numberconversion)
        elif decode_pathway[y] == "z":
            decode_code = int(tobase(decode_code, int(decode_bases[-1]), 10))
            decode_code -= int(numstouse[0])
            numstouse.pop(0)
            decode_code = str(tobase(decode_code, 10, int(decode_bases[-1])))
        elif decode_pathway[y] == "y":
            currentbase = int(decode_bases[-1])
            decode_code = int(tobase(decode_code, currentbase, 10))
            decode_code += int(numstouse[0])
            numstouse.pop(0)
            finalbase = currentbase
            decode_code = str(tobase(decode_code, 10, finalbase))
        elif decode_pathway[y] == "x":
            decode_code = int(tobase(decode_code, int(decode_bases[-1]), 10))
            decode_code /= int(numstouse[0])
            decode_code = int(decode_code)
            numstouse.pop(0)
            decode_code = str(tobase(decode_code, 10, int(decode_bases[-1])))
        elif decode_pathway[y] == "w":
            decode_code = int(tobase(decode_code, int(decode_bases[-1]), 10))
            decode_code *= int(numstouse[0])
            decode_code = int(decode_code)
            numstouse.pop(0)
            decode_code = str(tobase(decode_code, 10, int(decode_bases[-1])))

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
    global b_encode, b_decode, b_ascii, b_nascii, b_octal, b_cipher, b_dontclick, b_check, b_complete, b_functions, b_nothing, Logo2
    b_encode.destroy()
    b_decode.destroy()
    root.title("Start making your code, the parentheses says what each conversion does")
    root.geometry("1000x1000")
    b_ascii.place(relx=0, rely=0, relheight=(1 / 3), relwidth=(1 / 3))
    b_nascii.place(relx=(1 / 3), rely=0, relheight=(1 / 3), relwidth=(1 / 3))
    b_octal.place(relx=(2 / 3), rely=0, relheight=(1 / 3), relwidth=(1 / 3))
    b_cipher.place(relx=0, rely=(1 / 3), relheight=(1 / 3), relwidth=(1 / 3))
    b_check.place(relx=(1 / 3), rely=(2 / 3), relheight=(1 / 3), relwidth=(1 / 3))
    b_complete.place(relx=0, rely=(2 / 3), relheight=(1 / 3), relwidth=(1 / 3))
    b_functions.place(relx=(2 / 3), rely=(1 / 3), relheight=(1 / 3), relwidth=(1 / 3))
    b_nothing.place(relx=(2 / 3), rely=(2 / 3), relheight=(1 / 3), relwidth=(1 / 3))
    Logo2.place(relx=(1 / 3), rely=(1 / 3), relheight=(1 / 3), relwidth=(1 / 3))


def create_buttons():
    global b_encode, b_decode, b_ascii, b_nascii, b_octal, b_cipher, b_dontclick, b_check, b_complete, b_functions, b_nothing, Logo, Logo1, Logo2
    b_encode = Button(root, text="Encode", fg="blue", command=yell)
    b_decode = Button(root, text="Decode", fg="green", command=decode)
    b_ascii = Button(root, text="convert to ascii (Letters to Numbers)", fg="blue", command=ascii)
    b_nascii = Button(root, text="Math Functions", fg="blue",
                      command=calc)
    b_octal = Button(root, text="Convert to any base (Numbers to Numbers)", fg="blue", command=beforetobase)
    b_cipher = Button(root, text="Run your code through a cipher (Anything)", fg="blue", command=runthroughcipher)
    b_check = Button(root, text="See what the current status of your code is", fg="blue", command=show)
    b_complete = Button(root, text="Find your completed code", fg="blue", command=complete)
    b_functions = Button(root, text="Change language", fg="blue", command=function1)
    b_nothing = Button(root, text="Restart", fg="blue", command=replace)
    Logo = Image.open("Logo.png")
    Logo1 = ImageTk.PhotoImage(Logo)
    Logo2 = Label(root, image=Logo1)
    Logo2.image = Logo1


root = tk.Tk()
French = Button()
German = Button()
Spanish = Button()
language = ""
lowerconversion = []
upperconversion = []
numberconversion = []
root.geometry("600x400")
output = []
bases = []
onedig = []
twodig = []
numstem = []
ciphersused = []
operations = []
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
Logo = Image.open("Logo.png")
Logo1 = ImageTk.PhotoImage(Logo)
Logo2 = Label(image=Logo1)
Logo2.image = Logo1
buttonCommit = Button()
textBox = Text()
bInLow = False
bInUp = False
bInNum = False
CanUpNum = True
Nothing = False
CanNum = True
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
inputValue = ""

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