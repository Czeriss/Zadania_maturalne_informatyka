file1 = open("identyfikator.txt", "r")
file1 = file1.readlines()

baseLetter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
baseNumber=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]


def read():
    list = []
    for id in file1:
        id = id.strip()
        list.append(id)
    return list

def main():
    list = read()
    print("Podane identyfikatory są niepoprawne: ")
    for id in list:
        control = [7,3,1,7,3,1,7,3]
        new_number = []
        sum = 0
        toIdenty = int(id[3])


        letters=id[:3]
        numbers=id[4:]

        for letter in letters:
            tym = baseLetter.index(letter)
            tym = baseNumber[tym]
            new_number.append(tym)

        for numer in numbers:
           new_number.append(int(numer))

        for i in range(len(new_number)):
            sum+=new_number[i]*control[i]

        if sum%10!=toIdenty:
            print(id, end="\t")

main()