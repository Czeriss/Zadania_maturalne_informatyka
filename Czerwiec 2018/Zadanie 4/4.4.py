file1 = open("dane1.txt", "r")
file2 = open("dane2.txt", "r")
answer = open("wynik4_4.txt", "w")
file1 = file1.readlines()
file2 = file2.readlines()

def read(list):
    newList = []
    for line in list:
        newList.append(line.strip().split())
    return newList

def merge(list):
    if len(list)>1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i+=1
            else:
                list[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            list[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            list[k] = right[j]
            j+=1
            k+=1


def main():
    list1 = read(file1)
    list2= read(file2)
    for i in range(len(list1)):
        newList = []
        for digit in list1[i]:
            newList.append(int(digit))
        for digit in list2[i]:
            newList.append(int(digit))
        merge(newList)

        for digit in newList:
            tosave = "%d " %digit
            answer.write(tosave)
        answer.write("\n")

main()
