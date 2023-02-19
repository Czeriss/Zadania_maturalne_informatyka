"""Podaj, ile jest w pliku liczby.txt takich liczb, których cyfry pierwsza i ostatnia są takie
same. Zapisz tę z nich, która występuje w pliku liczby.txt jako pierwsza.
W pliku z danymi jest co najmniej jedna taka liczba."""
p1=open("liczby.txt", "r")
suma=0
def czytaj_i_porownaj():
    #odczytuje wiersz z pliku przyklad/liczby
    czytaj=p1.readline()
    #usuwa białe znaki
    czytaj=czytaj.strip()
    #wyznacza długość wierszu
    dl=len(czytaj)
    #porównuje czy element tablicy
    if czytaj[0] == czytaj[(dl-1)]:
        #zwtaca liczbę
        return czytaj
def main():
    suma=0
    wypisz_raz=True
    for i in range(200):
        liczba=czytaj_i_porownaj()
        if liczba != None:
            suma+=1
            if wypisz_raz == True:
                wypisz_raz=liczba
    print("W pliku znajduję się ",suma," liczb, w których cyfra pierwsza i ostatnia jest taka sama.\nPierwszą taką liczbą jest:", wypisz_raz)
main()