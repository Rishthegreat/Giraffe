string = ''
final = ''
ascii = input('Enter sentence: ')
for x in ascii:
   string += oct(ord(x))
instring = string
string = list(string.split("0o"))
for x in range(0, len(string)):
   string[x] = "0o" + string [x]
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
        Final_code =(cipher[digits.index(instring[counter])])
        Final_code = ''.join(Final_code)
        #print(Final_code)
        final = final+Final_code
y = final.replace("¿¡á", "a")
final = y.replace("¿¡ó", "b")
y = final.replace("aóú", "c")
final = y.replace("aúó", "d")
print(final)

while totalen != currindex:
    if decode_pathway[currindex] == "0" or decode_pathway[currindex] == "1" or decode_pathway[currindex] == "2" or \
            decode_pathway[currindex] == "3" or \
            decode_pathway[currindex] == "4" or decode_pathway[currindex] == "5" or decode_pathway[
        currindex] == "6" or decode_pathway[currindex] == "7" or decode_pathway[currindex] == "8" or decode_pathway[
        currindex] == "9":
        numstem.append(decode_pathway[currindex])
        if first:
            beginningindex = currindex
            first = False
    if decode_pathway[currindex].islower:
        if len(numstem) != 0:
            print(decode_pathway[currindex])
            numstouse.append(listToString(numstem))
            numstem = []
            first = True
            del decode_pathway[beginningindex:currindex]
    currindex += 1
    totalen = len(decode_pathway)