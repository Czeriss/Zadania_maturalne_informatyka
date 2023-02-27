p1 = open("sygnaly.txt", "r")
lines = p1.readlines()

def read():
    list=[]
    for line in lines:
        list.append(line.strip())
    return list


def main():
    list = read()
    maxletter= 0
    answerWord = ""
    for word in list:
        tableWord=[]
        for letter in word:
            if letter not in tableWord:
                tableWord.append(letter)
        tymMax = len(tableWord)
        if tymMax > maxletter:
            (maxletter, answerWord) = (tymMax, word)
    print(maxletter, answerWord)

main()
