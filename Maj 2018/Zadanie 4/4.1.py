p1 = open("sygnaly.txt", "r")
lines = p1.readlines()

def read():
    list=[]
    for line in lines:
        list.append(line.strip())
    return list


def main():
    list = read()
    answer=""
    for i in range(39, 1000, 40):
        word = list[i]
        answer+=word[9]

    print(answer)

main()
