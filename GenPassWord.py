# goal : X char password, random, not twice the same char
from random import randint

def genPass(length=20):
    liste_char = ["a","b","c","d","e","f","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x",
    "y","z","0","1","2","3","4","5","6","7","8","9","@","ù","%","$","£"]
    password = []
    while len(password) < length:
        index = randint(0,len(liste_char)-1)
        test = randint(0,1)
        if liste_char[index] not in "".join(password):
            if test == 0:
                password.append(liste_char[index])
            else:
                password.append(liste_char[index].upper())
    password = "".join(password)
    return password

genPass()
