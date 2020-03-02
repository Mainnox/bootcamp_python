def tamer(str):
    print ("Tamer")

def text_analyzer(string):
    countupper = 0
    countlower = 0
    countspace = 0
    countpunctuation = 0
    globalcount = 0
    for i in string:
        if (i.isupper() == True):
            countupper += 1
        elif (i.islower() == True):
            countlower += 1
        elif (i.isspace() == True):
            countspace += 1
        else:
            countpunctuation += 1
        globalcount = countspace + countlower + countupper + countspace + countpunctuation
    print ("The text countains" , str(globalcount) , "characters:\n-" , str(countupper)) 