plik=open("napisy.txt","r")
wiersze = plik.readlines()
haslo=""
for wiersz in wiersze:
    wiersz = wiersz.strip()
    palindrom1= wiersz + wiersz[0]
    palindrom2= wiersz[-1]+wiersz
    if palindrom1 == palindrom1[::-1]:
        haslo+=palindrom1[25]
    elif palindrom2 == palindrom2[::-1]:
        haslo+=palindrom2[25]
print(haslo)
