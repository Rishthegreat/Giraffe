import tkinter as tk


def encoder():
    decode.destroy()
    encode.destroy()
    choose.destroy()


def decoder():
    decode.destroy()
    encode.destroy()
    choose.destroy()


def moveon():
    global userinput
    userinput = e.get("1.0", "end-1c")
    e.destroy()
    eorc.destroy()
    encode.place(relx=0, rely=0.25, relwidth=0.5, relheight=0.75)
    decode.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.75)
    choose.place(relx=0, rely=0, relheight=0.25, relwidth=1)


def convertascii(x):
    conascii = []
    for index in range(0, len(x)):
        conascii.append(ord(x[index]))
    return conascii


def toBase(n, base):
    convertBase = "0123456789ABCDEF"
    if n < base:
        return convertBase[n]
    else:
        return toBase(n // base, base) + convertBase[n % base]


root = tk.Tk()
root.title("Encoder/Decoder Program")
root.geometry("600x400")
decode = tk.Button(root, text="decode", foreground="red", font=50, command=decoder)
encode = tk.Button(root, text="Encode", foreground="blue", font=50, command=encoder)
eorc = tk.Button(root, text="Click to Encode or Decode", foreground="black", font=50, background="pink", command=moveon)
choose = tk.Label(root, text="Choose to encode or decode", font=50)
e = tk.Text(root)
e.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.4)
eorc.place(relx=0.125, rely=0.5, relwidth=0.75, relheight=0.4)

root.mainloop()
