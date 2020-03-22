from random import randint
import os

def header():
    print("\t*******************************************")
    print("\t***           GUESSING GAME            ****")
    print("\t*******************************************\n")
    print("This is an interactive guessing game !")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")

random = randint(1, 99)
os.system('clear')
header()
temp = 1
while (1):
    count = 0
    print("What's your guess between 1 and 99?")
    put = input()
    if not put:
        continue
    if put == "exit":
        exit()
    for i in put:
        if i.isdigit() == False:
            count += 1
    if count != 0:
        print("Just type a number ffs.")
        continue
    if int(put) < random:
        print("Too low.")
        temp += 1
        continue
    elif int(put) > random:
        print("Too big.")
        temp += 1
        continue
    else:
        os.system('clear')
        print("GG !\nYou find the magic number in " + str(temp) + " attempts.\nYou rock !")
        break
