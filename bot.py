import string
import time
from random import choice

password = input("Quel est le mot de passe ? ")
lettersinput = input("Combien de lettres ? ")
timechrono = 0
lettersinput = int(lettersinput)
wordletters = ["a"]


searching = True

while searching :

    for letter in range(lettersinput):
        if letter == 0 :
            wordletters[0] = choice(string.ascii_lowercase)
        else :
            wordletters.append(choice(string.ascii_lowercase))


    passwordfound = "".join(wordletters)
    time.sleep(0.01)
    timechrono += 0.01

    if passwordfound == password :
        searching = False
        print("Password is " + passwordfound +", completed in " + str(timechrono) +" seconds")
    else :
        print(passwordfound + " failed")

    wordletters = ["a"]

input("enter to exit")