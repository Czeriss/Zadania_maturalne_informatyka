file1 = open("dane1.txt", "r")
file2 = open("dane2.txt", "r")

file1 = file1.readlines()
file2 = file2.readlines()

def read(list):
    newList = []
    for line in list:
        newList.append(line.strip().split())
    return newList

def main():
    list1 = read(file1)
    list2 = read(file2)
    answer = 0
    listIndex = []
    for i in range(len(list1)):
        digitFromList1 = set(list1[i])
        digitFromList2 = set(list2[i])
        if digitFromList1 == digitFromList2:
            listIndex.append(i+1)
            answer+=1

    print("W plikach znajduję się %d ciągów w tym samym wierszy, które składają się z tych samych liczb" % answer)
    print("Numery wierszy: ", listIndex)
main()