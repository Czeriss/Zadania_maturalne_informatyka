"""Trójka (x, y, z) jest dobra, jeśli y jest wielokrotnością x, natomiast z jest wielokrotnością y
(czyli x dzieli y, a y dzieli z) oraz x, y, z są różne.
a) Podaj, ile jest dobrych trójek wśród liczb występujących w pliku liczby.txt. Zapisz
wszystkie dobre trójki do pliku trojki.txt, każdą w osobnym wierszu.
Uwaga: Liczby z trójki nie muszą występować w pliku liczby.txt w kolejnych
wierszach, a ich kolejność w tym pliku może być dowolna.
b) Podaj, ile jest dobrych piątek wśród liczb występujących w pliku liczby.txt
"""

p1 = open("liczby.txt", "r")
p2 = open("liczby.txt", "r")
p3 = open("liczby.txt", "r")
zapis = open("trojki.txt", "w")

def czytaj_wiersz():
    czytaj = p1.readline()
    czytaj = czytaj.strip()
    return czytaj
def wiersz2():
    wiersze=p2.readlines()
    list=[]
    for wiersz in wiersze:
        wiersz=wiersz.strip()
        list.append(wiersz)
    return list
def wiersz3():
    wiersze=p3.readlines()
    list=[]
    for wiersz in wiersze:
        wiersz=wiersz.strip()
        list.append(wiersz)
    return list
def zamiana(s1):
    s1=str(s1)
    s1+=" "
    return s1
def odmiana(s1):
    s1=int(s1)
    return s1
def trojki():
    licznik=0
    k2 = wiersz2()
    k3 = wiersz3()
    zapis.write("Dobre trojki:\n")
    for i in range(200):
        k1=czytaj_wiersz()
        k1=int(k1)
        for szukana2 in k2:
            szukana2=int(szukana2)
            if szukana2%k1==0 and szukana2 > k1:
                for szukana3 in k3:
                    szukana3=int(szukana3)
                    if szukana3%szukana2==0 and szukana3 > szukana2 :
                        k1=zamiana(k1)
                        szukana2=zamiana(szukana2)
                        szukana3=zamiana(szukana3)
                        zapis.writelines([k1, szukana2, szukana3])
                        zapis.write("\n")
                        k1=odmiana(k1)
                        szukana2=odmiana(szukana2)
                        licznik+=1
    p1.close()
    p2.close()
    p3.close()
    zapis.close()
    print("Znalazłem ",licznik," dobrych trójek")
trojki()
pi1 = open("liczby.txt", "r")
pi2 = open("liczby.txt", "r")
pi3 = open("liczby.txt", "r")
pi4 = open("liczby.txt", "r")
pi5 = open("liczby.txt", "r")
def czytaj_wierszP():
    czytaj = pi1.readline()
    czytaj = czytaj.strip()
    return czytaj
def wiersz2P():
    wiersze=pi2.readlines()
    list=[]
    for wiersz in wiersze:
        wiersz=wiersz.strip()
        list.append(wiersz)
    return list
def wiersz3P():
    wiersze=pi3.readlines()
    list=[]
    for wiersz in wiersze:
        wiersz=wiersz.strip()
        list.append(wiersz)
    return list
def wiersz4P():
    wiersze=pi4.readlines()
    list=[]
    for wiersz in wiersze:
        wiersz=wiersz.strip()
        list.append(wiersz)
    return list
def wiersz5P():
    wiersze=pi5.readlines()
    list=[]
    for wiersz in wiersze:
        wiersz=wiersz.strip()
        list.append(wiersz)
    return list
def piatki():
    licznikP = 0
    k2P = wiersz2P()
    k3P = wiersz3P()
    k4P = wiersz4P()
    k5P = wiersz5P()
    for i in range(200):
        szukana1P = czytaj_wierszP()
        szukana1P = int(szukana1P)
        for szukana2P in k2P:
            szukana2P = int(szukana2P)
            if szukana1P%szukana2P==0 and szukana1P > szukana2P:
                for szukana3P in k3P:
                    szukana3P = int(szukana3P)
                    if szukana2P%szukana3P==0 and szukana2P > szukana3P:
                        for szukana4P in k4P:
                            szukana4P = int(szukana4P)
                            if szukana3P%szukana4P==0 and szukana3P > szukana4P:
                                for szukana5P in k5P:
                                    szukana5P = int(szukana5P)
                                    if szukana4P%szukana5P==0 and szukana4P > szukana5P:
                                        licznikP+=1
    print("Znalazłem ",licznikP," dobrych piątek")
piatki()