from math import *

file = open("liczby.txt", "r")
file = file.readlines()

def read():
    list =[]
    for line in file:
        list.append(int(line))
    return list

def silnia(digit):
    sil = 1
    for i in range(1,digit+1):
        sil *=i
    return sil


def main():
    list = read()

    for word in list:
        silSum = 0

        for digit in str(word):
            silSum += silnia(int(digit))

        if word == silSum:
            print(word)

main()