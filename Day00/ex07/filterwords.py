from sys import argv
import string

j = 0
if len(argv) != 3:
    print("ERROR")
while j < len(argv[2]):
    if argv[2][j].isdigit() == False and argv[2][j] != '+':
        print("ERROR")
        exit()
    j += 1

split = argv[1].split()
while (1):
    check = 0
    for i in split:
        for j in i:
            if j in string.punctuation:
                new = i.replace(j, "")
                tmp = split.index(i)
                split.remove(i)
                split.insert(tmp, new)
                check += 1
                break
    if check == 0:
        break

ret = []
for i in split:
    if len(i) > int(argv[2]):
        ret.append(i)
print(ret)