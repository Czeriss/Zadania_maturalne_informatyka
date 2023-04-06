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
        parzyste1=0
        parzyste2=0
        nieparzyste1=0
        nieparzyste2=0

        for digit in list1[i]:
            if int(digit)%2==1:
                nieparzyste1+=1
            else:
                parzyste1+=1

        for digit in list2[i]:
            if int(digit)%2==1:
                nieparzyste2+=1
            else:
                parzyste2+=1

        if nieparzyste1==5 and nieparzyste2==5:
            answer+=1

    print("W %d ciągów znajduję się po 5 liczb parzystych i nieparzystych"% answer )
main()