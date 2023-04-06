from math import *

p1 = open("liczby.txt", "r")
write = open("wynik_1.txt","w")

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

def main():
    list = read()

    for letter in list:
        if letter >=100 and letter<=5000:
            if isFirst(letter):
                toWrite=str(letter)
                write.write(toWrite)
                write.write("\n")

main()


