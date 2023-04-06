p1 = open("napisy.txt", "r")
lines = p1.readlines()

def read():
    list=[]
    for line in lines:
        list.append(line.strip())
    return list

def main():

    list = read()
    dublenumber=[]
    for line in list:
        count = 0
        table = []
        for letter in line:
            if letter.isdigit():
                count+=1
                table.append(int(letter))
        dl = len(table)
        if dl%2==1:
            dl-=1

        for i in range(0,dl,2):
            number1 = str(table[i])
            number2 = str(table[i+1])
            answer=number1+number2
            dublenumber.append(int(answer))

    answer = ""
    for number in dublenumber:
       if number>=65 and number<=90:
        answer+=chr(number)
        if answer[-1] == "X" and answer[-2]=="X" and answer[-3]=="X":
            break


    print(answer)


main()