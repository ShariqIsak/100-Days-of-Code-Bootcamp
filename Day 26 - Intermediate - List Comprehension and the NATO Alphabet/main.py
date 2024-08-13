with open("file1.txt") as data1:
    data1 = data1.readlines()
    data1 = [int(n) for n in data1]
    print(data1)

with open("file2.txt") as data2:
    data2 = data2.readlines()
    data2 = [int(n) for n in data2]
    print(data2)


result = [n for n in data1 if [x for x in data2 if n == x]]

print(result)