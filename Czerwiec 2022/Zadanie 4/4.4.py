#plik wyświetla wartość pow1/pow2 niezgodną z kartą odpwoeidzi. Zgodnie z punktacją zadanie jest zrobione na 3/4ptk
p1=open("dane.txt","r")
baza=open("dane.txt","r")
def bazawiersze():
    sum=[]
    wiersze=baza.readlines()
    for wiersz in wiersze:
        wiersz = wiersz.strip()
        sum.append(wiersz)
    return sum
def czytaj():
    wiersz=p1.readline()
    wiersz = wiersz.strip()
    return wiersz
def main():
    sprawdzone = []
    pow1 = 0
    pow2 = 0
    pow3 = 0
    wszystkie=bazawiersze()
    for i in range(100):
        liczba =czytaj()
        licznik=0
        for n in range(i+1,100):
            if liczba == wszystkie[n] and liczba not in sprawdzone:
                licznik+=1
        if licznik == 0:
            pow1 += 1
        elif licznik==1:
            pow2+=1
        elif licznik==2:
            pow3+=1
        else:
            continue
        sprawdzone.append(liczba)
    print("W danym pliku znajduje się ",pow1," różnych liczb, ",pow2," liczb, które powtarzają się tylko 2 razy i ",pow3," liczb, które powtarzają się 3 razy")
main()
