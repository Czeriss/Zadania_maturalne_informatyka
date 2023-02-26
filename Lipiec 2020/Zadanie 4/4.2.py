file1 = open("identyfikator.txt", "r")
file1 = file1.readlines()


def read():
    list = []
    for id in file1:
        id = id.strip()
        list.append(id)
    return list

def main():
    list = read()
    pandolin = []

    for id in list:
        isTrueletter = False
        isTrueNumber = False
        letters = id[:3]
        numbers = id[3:]

        if letters[0] == letters[-1]:
             isTrueletter = True
        if numbers[0] == numbers[-1] and numbers[1] == numbers[-2] and numbers[2] == numbers[-3]:
            isTrueNumber = True

        if isTrueletter == True or isTrueNumber == True:
            pandolin.append(id)

    for answer in pandolin:
        print(answer, end="\t")

main()