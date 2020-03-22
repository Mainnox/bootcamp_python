from sys import argv

morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '--.',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.' 
}

argv.pop(0)
for i in argv:
    for j in i:
        if j.isalnum() == False:
            print("ERROR")
            exit()
print(argv)
count = 0
count2 = 0
for i in argv:
    i = i.lower()
    for j in i:
        print(morse[j], end= '')
        print(' ', end = '')
        count += 1
    if count2 < len(argv) - 1:
        print('/ ', end='')
    count2 += 1
