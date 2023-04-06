p1 = open("przyklad.txt", "r")
lines = p1.readlines()

def read():
    list=[]
    for line in lines:
        list.append(line.strip())
    return list

def main():
    list = read()
    count = 0
    for line in list:
        for letter in line:
            if letter.isdigit():
                count+=1
    print(count)

main()