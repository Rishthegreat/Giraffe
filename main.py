import enchant


def convert(string):
    return list(string.split(" "))


def length(something):
    return len(something)


d = enchant.Dict("en_US")
answer = convert(input("Enter a sentence: ").lower())


def checking(dictionary):
    check = 0
    for indexes in range(0, length(dictionary)):
        if d.check(dictionary[indexes]):
            check += 1
        else:
            check -= 1
    return check


cipher = "qwertyuiopasdfghjklzxcvbnm1234567890,:/.?!"
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890,:/.?!"
word = ""
Final_sentence = ""
Final_word = []
notenglish = True
if checking(answer) == length(answer):
    for counter in range(0, length(answer)):
        word = answer[counter]
        Final_word = []
        for counter2 in range(0, length(word)):
            Final_word += cipher[alphabet.index(word[counter2])]
        Final_sentence += "".join(Final_word) + " "
else:
    sentence_check = answer
    while notenglish:
        Final_sentence = ""
        for counter in range(0, length(sentence_check)):
            word = sentence_check[counter]
            Final_word = []
            for counter2 in range(0, length(word)):
                Final_word += alphabet[cipher.index(word[counter2])]
            Final_sentence += "".join(Final_word) + " "
        sentence_check = convert(Final_sentence)
        sentence_check.pop()
        if checking(sentence_check) == length(sentence_check):
            notenglish = False
        print(Final_sentence)

print(Final_sentence)




# cipher[2] is string at the 3rd place
# cipher.index(q) will return a value of 0
# cipher.replace("q", "elephant") will replace q with elephant
# use len to find the length of a string
