p1 = open("pary.txt", "r")
lines = p1.readlines()

def read():
    list=[]
    for line in lines:
        list.append(line.strip())
    return list

def firstNumber():
    list = []
    for i in range(2,100):
        isFirst = True
        for n in range(2,i):
            if i%n==0:
                isFirst = False
        if isFirst:
            list.append(i)
    return list

def main():
    list = read()
    listFirst = firstNumber()
    for line in list:
        number = int(line[:2])
        if number%2==0:
            isbreak=False
            for first1 in listFirst:
                first1 = int(first1)
                if first1 > number:
                    break
                for first2 in listFirst:
                    first2 = int(first2)
                    if first1+first2==number:
                        print(number,  first1, first2)
                        isbreak = True
                        break
                    if isbreak:
                        break

main()
