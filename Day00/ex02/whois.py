from sys import argv

if (len(argv) >= 2):
    if (len(argv) == 2):
        if (argv[1].isdigit() == True):
            if (int(argv[1]) == 0):
                print("I'm Zero.")
            elif (int(argv[1]) % 2 == 0):
                print ("I'm Even.")
            else:
                print("I'm Odd.")
        else:
            print("ERROR")
    else:
        print("ERROR")
