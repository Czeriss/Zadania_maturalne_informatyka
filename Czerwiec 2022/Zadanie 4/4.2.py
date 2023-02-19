p1=open("dane.txt","r")
max=0
maxliczba=0
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
    literka = int(literka)
    liczba_odjac_odbicie = literka-liczba
    liczba_odjac_odbicie= abs(liczba_odjac_odbicie)
    if liczba_odjac_odbicie > max:
        max=liczba_odjac_odbicie
        maxliczba=literka
print("Największa wartość bezwzględna liczby - odbicie jest z\nLiczba:",maxliczba,"\nA wartość bezwzględna różnicy liczby i jej odbicia wynosi:",max)

