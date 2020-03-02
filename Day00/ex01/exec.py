import sys

string = []
gnirts = []
uplo = ""
count = 0
for arg in sys.argv:
    string.append(arg)
    count +=  1
string.remove("exec.py")
for i in string:
    gnirts.append(i[::-1])
for i in gnirts:
    for a in i:
        if (a.isupper()) == True:
            uplo += a.lower()
        elif (a.islower()) == True:
            uplo += a.upper()
        else:
            uplo += a
    if 2 < count:
        uplo += ' '
        count -= 1
x = " ".join(uplo)
if count > 1:
    print (uplo)
