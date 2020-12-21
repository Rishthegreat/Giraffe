f = open(r"C:\Users\MJPV\Documents\code.txt","r")
content = str(f.read())
newcontent = list(content)
print(content)
for item in newcontent:
    string = ''
    final = ''
    ascii = item
    for x in ascii:
        string += oct(ord(x))
    instring = string
    string = list(string.split("0o"))
    for x in range(0, len(string)):
        string[x] = "0o" + string[x]
    string.pop(0)
    cipher = "áéíóúüñ¿¡"
    digits = "12345670o"
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
final = str(final)
y = final.replace("¿¡á", "a")
final = y.replace("¿¡ó", "b")
y = final.replace("aóú", "c")
final = y.replace("aúó", "d")