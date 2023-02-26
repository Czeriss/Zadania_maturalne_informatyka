"""Trójka (x, y, z) jest dobra, jeśli y jest wielokrotnością x, natomiast z jest wielokrotnością y
(czyli x dzieli y, a y dzieli z) oraz x, y, z są różne.
a) Podaj, ile jest dobrych trójek wśród liczb występujących w pliku liczby.txt. Zapisz
wszystkie dobre trójki do pliku trojki.txt, każdą w osobnym wierszu.
Uwaga: Liczby z trójki nie muszą występować w pliku liczby.txt w kolejnych
wierszach, a ich kolejność w tym pliku może być dowolna.
b) Podaj, ile jest dobrych piątek wśród liczb występujących w pliku liczby.txt
"""

p1 = open("liczby.txt", "r")
zapis = open("trojki.txt", "w")
zapis.write("Dobre trojki:\n")

def readAllLines():
    list = []
    read = p1.readlines()
    for intiger in read:
        intiger = intiger.strip()
        intiger = int(intiger)
        list.append(intiger)
    return list


def trojki():
    licznik=0
    list = readAllLines()
    for int1 in list:
        for int2 in list:
            for int3 in list:
                if int2%int1==0 and int3%int2==0 and int1 != int2 and int2 != int3:
                    licznik+=1
                    (int1, int2, int3) = (str(int1), str(int2), str(int3))
                    zapis.writelines([int1, int2, int3])
                    (int1, int2, int3) = (int(int1), int(int2), int(int3))
    p1.close()
    zapis.close()
    print("Znalazłem ",licznik," dobrych trójek")


p2 = open("liczby.txt", "r")

def readAllLines1():
    list = []
    read = p2.readlines()
    for intiger in read:
        intiger = intiger.strip()
        intiger = int(intiger)
        list.append(intiger)
    return list

def piatki():
    licznik = 0
    list = readAllLines1()
    for five1 in list:
        for five2 in list:
            if five1%five2==0 and five1 > five2:
                for five3 in list:
                    if five2%five3==0 and five2 > five3:
                        for five4 in list:
                            if five3%five4==0 and five3 > five4:
                                for five5 in list:
                                    if five4%five5==0 and five4 > five5:
                                        licznik+=1

    print("W pliku jest ",licznik, "dobrych piątek")
    p2.close()

trojki()
piatki()
