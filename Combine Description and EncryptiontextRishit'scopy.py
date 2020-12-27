import tkinter as tk


def encoder():
    decode.destroy()


root = tk.Tk()
root.title("Encoder/Decoder Program")
root.geometry("600x400")
decode = tk.Button(root, text="decode", foreground="red", font=50)
encode = tk.Button(root, text="Encode", foreground="blue", font=50, command=encoder())

encode.place(relx=0, relwidth=0.5, relheight=1)
decode.place(relx=0.5, relwidth=0.5, relheight=1)
root.mainloop()
