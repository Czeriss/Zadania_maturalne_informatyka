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
    for i in range(len(list1)):
        if list1[i][-1] == list2[i][-1]:
            answer+=1

    print("Ostatnia liczba w obu ciągach pojawiła się %d razy" % answer)
main()