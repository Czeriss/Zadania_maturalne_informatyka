from math import *
p1 = open("pierwsze.txt", "r")
lines = p1.readlines()

def read():
    list=[]
    for line in lines:
        line = int(line)
        list.append(line)
    return list

def isFirst(letter):
    letterSqrt = sqrt(letter)
    letterSqrt = int(letterSqrt)+1

    for i in range(2, letterSqrt):
        if letter%i==0:
            return False
    return True

def wspak(letter):
    answer = ""
    strLetter = str(letter)
    letterLen = len(strLetter)
    for i in reversed(range(letterLen)):
        answer +=strLetter[i]
    return answer

def main():
    list = read()
    for letter in list:
        wspakLetter = int(wspak(letter))

        if isFirst(wspakLetter):
            print(wspakLetter)

main()