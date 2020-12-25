string = input('Enter sentence: ')
cipher = "áéíóúüñ¿¡"
digits = "12345670o"
tobedecypted = ""
y = string.replace("d", "aúó")
string = y.replace("c", "aóú")
y = string.replace("b", "¿¡ó")
string = y.replace("a", "¿¡á")
for x in range(0, len(string)):
    tobedecypted += digits[cipher.index(string[x])]
string = tobedecypted
string = list(string.split("0o"))
for x in range(0, len(string)):
   string[x] = "0o" + string [x]
string.pop(0)
for x in range(0, len(string)):
    string[x] = chr(int(str(string[x]), 8)) 
print("".join(string))
