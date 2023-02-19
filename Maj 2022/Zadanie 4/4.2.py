import math
"""Znajdź w pliku liczby.txt:
liczbę, która ma w rozkładzie najwięcej czynników pierwszych (podaj tę liczbę oraz liczbę
jej czynników pierwszych)
liczbę, która ma w rozkładzie najwięcej różnych czynników pierwszych (podaj tę liczbę
oraz liczbę jej różnych czynników pierwszych)"""
p1=open("liczby.txt", "r")
def liczba():
    liczba=p1.readline()
    liczba=liczba.strip()
    liczba = int(liczba)
    return liczba
def czynnikisuma(liczba):
    licziki_suma=[]
    licziki_rozne=[]
    i = 2
    while liczba>1:
        if liczba%i==0:
            liczba=liczba/i
            licziki_suma.append(i)
            if i not in licziki_rozne:
                licziki_rozne.append(i)
        else:
            i+=1
    return licziki_suma
def czynnikirozne(liczba):
    licziki_suma=[]
    licziki_rozne=[]
    i = 2
    while liczba>1:
        if liczba%i==0:
            liczba=liczba/i
            licziki_suma.append(i)
            if i not in licziki_rozne:
                licziki_rozne.append(i)
        else:
            i+=1
    return  licziki_rozne
def main():
    maxsuma=0
    sumaliczba=0
    maxroznica=0
    roznicaliczba=0
    for n in range(200):
        czytaj = liczba()
        print(czytaj)
        suma=czynnikisuma(czytaj)
        suma=len(suma)

        roznica=czynnikirozne(czytaj)
        roznica=len(roznica)

        if suma >= maxsuma:
            maxsuma=suma
            sumaliczba=czytaj
        if roznica >= maxroznica:
            maxroznica=roznica
            roznicaliczba=czytaj
    print(sumaliczba," ",maxsuma,"  ",roznicaliczba," ",maxroznica)
main()
