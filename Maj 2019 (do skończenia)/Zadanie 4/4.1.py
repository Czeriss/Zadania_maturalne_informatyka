from math import *

file = open("liczby.txt", "r")
file = file.readlines()

def read():
    list =[]
    for line in file:
        list.append(int(line))
    return list

def ispow3(digit):
    if float.is_integer(log(digit ,3)):
        return True

def main():
    count = 0
    list = read()

    for line in list:
        if ispow3(line):
            count += 1

    print("W pliku jest %d liczb, które są potęgami liczby 3" % count)



main()