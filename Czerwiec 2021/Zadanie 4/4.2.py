plik=open("przyklad.txt","r")
wiersze = plik.readlines()
i=0
haslo=""
for n in range(19, len(wiersze),20):
    haslo+=(wiersze[n][i])
    i+=1
print(haslo)