from math import *

p1 = open("pierwsze.txt", "r")
lines = p1.readlines()

write = open("wynik_3.txt","w")

def read():
    list=[]
    for line in lines:
        list.append(int(line))
    return list

def toDoList(number):
    listNumber = []
    number = str(number)
    for letter in number:
        listNumber.append(int(letter))
    return listNumber

def main():
    count = 0
    list = read()
    for number in list:
        listNumber = toDoList(number)
        while len(listNumber) > 1:
            sum = fsum(listNumber)
            sum = int(sum)
            sum = str(sum)
            listNumber = []
            for number in sum:
                listNumber.append(int(number))
        if sum=="1":
            count+=1
    answer = "W pliku jest %d liczb, których waga = 1" % count
    write.write(answer)

main()