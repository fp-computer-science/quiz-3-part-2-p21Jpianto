# Author: JAP (amdg) 1/12/2021

import random


def clone_maker():
    user = input("Would you like to make a clone? Put Y for yes, N for no.")
    if user == "Y":
        clone = "CT-" + str((random.randint(1, 9999)))
        print("New clone trooper name: " + clone)
    elif user == "y":
        "CT-" + str(random.randint(1, 9999))
        print("New clone trooper name: " + clone)
    else:
        print("Alright commander.")

    while True:
        user = input("Wanna make another one? Y for yes N for no")
        if user == 'Y':
            print(clone_maker())
        elif user == 'y':
            print(clone_maker())
        else:
            break


clone_maker()
