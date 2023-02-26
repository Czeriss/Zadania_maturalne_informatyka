plik1 = open("identyfikator.txt","r")
plik2 = open("4.1_zapisz.txt", "w")


def  wiersze():
    wiersze = plik1.readlines()
    return wiersze
def sumuj(liczba):
    suma=0
    for inti in liczba:
        suma+=int(inti)
    return suma


def main():
    suma = 0
    najwiekszyId=""
    for wiersz in wiersze():
        liczby_wiersz = wiersz[3:9]
        tym = sumuj(liczby_wiersz)
        if tym > suma:
            suma = tym
            najwiekszyId=wiersz
        elif tym==suma:
            najwiekszyId+=wiersz
    plik2.write(najwiekszyId)


main()