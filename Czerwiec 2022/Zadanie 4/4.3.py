p1=open("dane.txt","r")
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
        m+=liczba[i]
    return m
for i in range(100):
    wiersz=czytaj()
    liczba=petla()
    dl=len(liczba)
    odbicie=rev(dl)
    odbicie = int(odbicie)
    liczba = int(liczba)
    for fr in range(2,int(liczba/2)):
        odp1=False
        if liczba%fr==0:
            odp1=True
            break
    for sc in range(2,int(odbicie/2)):
        odp2=False
        if odbicie%sc==0:
            odp2=True
            break
    if odp1==False and odp2==False:
        print(liczba)