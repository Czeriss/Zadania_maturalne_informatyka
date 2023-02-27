p1 = open("sygnaly.txt","r")


def read():
    list = []
    lines = p1.readlines()
    for line in lines:
        list.append(line.strip())
    return list

def main():
    list = read()
    answers = []
    for line in list:
        min = None
        isTrue = True
        for letter in line:
            forNow = ord(letter)

            if min == None:
                min = forNow

            if forNow < min:
                min = forNow

            if forNow > min+10:
                isTrue = False
                continue

        if isTrue:
            answers.append(line)

    for answer in answers:
        print(answer)










main()