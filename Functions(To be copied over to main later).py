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


def toascii(n):
    answer = []
    for letters in range(0, len(n)):
        answer.append(ord(n[letters]))
    return answer


def frominttoascii(n):
    for numbers in range(0, len(n)):
        n[numbers] = chr(int(n[numbers]))