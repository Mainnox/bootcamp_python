from sys import argv
argv.remove("operations.py")
if (len(argv) == 0):
    print("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")
    exit(0)
if (len(argv) != 2):
    print("Wrong numbers of arguments")
    exit(0)
for i in argv[0]:
    if (i.isdigit() == False):
        print("InputError: only numbers")
        exit(0)
for i in argv[1]:
    if (i.isdigit() == False):
        print("InputError: only numbers")
        exit(0)
print("Sum:         " + str(int(argv[0]) + int(argv[1])))
print("Difference:  " + str(int(argv[0]) - int(argv[1])))
print("Product:     " + str(int(argv[0]) * int(argv[1])))
if (int(argv[0]) == 0 or int(argv[1]) == 0):
    print("Quotient:    ERROR (div by zero)")
    print("Remainder:   ERROR (modulo by zero)")
else:
    print("Quotient:    " + str(int(argv[0]) / int(argv[1])))
    print("Remainder:   " + str(int(argv[0]) % int(argv[1])))