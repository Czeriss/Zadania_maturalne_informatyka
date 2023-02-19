p1=open("dane.txt","r")
odbicie=[]
def czytaj():
    wiersze=p1.readline()
    wiersze=wiersze.split()
    return wiersze
def petla():
    for literka in wiersz:
        return literka
def rev(dl):
    m = ""
    for i in reversed(range(dl)):
        m+=literka[i]
    return m

for i in range(100):
    wiersz=czytaj()
    literka=petla()
    dl=len(literka)
    liczba=rev(dl)
    liczba = int(liczba)
    if liczba%17==0:
        print("Podane odbicie liczby ",literka," jest liczbą podzielną przez 17")
        odbicie.append(liczba)
print(odbicie)



