def text_analyzer(string = "Bijour"):
    """
    Ta grosse mere la reine des putes
    """
    countupper = 0
    countlower = 0
    countspace = 0
    countpunctuation = 0
    globalcount = 0
    if (string == "Bijour"):
        print("What is the text to analyze?")
        string = input()
    for i in string:
        if (i.isupper() == True):
            countupper += 1
        elif (i.islower() == True):
            countlower += 1
        elif (i.isspace() == True):
            countspace += 1
        else:
            countpunctuation += 1
        globalcount = countspace + countlower + countupper + countpunctuation
    print("The text contains " + str(globalcount) + " characters:")
    print("- " + str(countupper) + " upper letters")
    print("- " + str(countlower) + " lower letters")
    print("- " + str(countpunctuation) + " punctuation marks")
    print("- " + str(countspace) + " space")